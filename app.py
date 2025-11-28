from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("model/house_price_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # parse inputs
        age = float(request.form.get("age", "0"))
        bedrooms = float(request.form.get("bedrooms", "0"))
        area = float(request.form.get("area", "0"))

        # basic validation
        if any(x < 0 for x in (age, bedrooms, area)):
            return render_template("index.html", prediction_text="Error: inputs must be non-negative numbers")

        # Build a DataFrame with explicit feature names so order doesn't break
        # model.feature_names_in_ is available for sklearn models trained in modern versions
        if hasattr(model, "feature_names_in_"):
            cols = list(model.feature_names_in_)
        else:
            # fallback to known order used when training: area, bedrooms, age
            cols = ["area", "bedrooms", "age"]

        row = {"area": area, "bedrooms": bedrooms, "age": age}
        # ensure the columns are in the same order as model expects
        features_df = pd.DataFrame([[row.get(c, 0) for c in cols]], columns=cols)

        # predict
        pred = model.predict(features_df)[0]
        prediction = round(float(pred), 2)

        return render_template("index.html", prediction_text=f"Predicted Price: ₹{prediction}")

    except Exception as e:
        # Log the error server-side if you add logging; for now return a friendly message
        return render_template("index.html", prediction_text=f"Error making prediction: {e}")


if __name__ == "__main__":
    app.run(debug=True)
