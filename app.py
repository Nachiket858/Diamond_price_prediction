import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from flask import Flask, render_template, request
from src.pipelines.prediction_pipeline import Custom_data,predictPipeline  # Ensure these are implemented correctly
import numpy as np

app = Flask(__name__)

# Route for the input form
@app.route("/", methods=["GET"])
def index():
    return render_template("home.html")

# Route for predicting the price
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Collect data from the form
        data = Custom_data(
            carat=float(request.form["carat"]),
            cut=request.form["cut"],
            color=request.form["color"],
            clarity=request.form["clarity"],
            depth=float(request.form["depth"]),
            table=float(request.form["table"]),
            x=float(request.form["x"]),
            y=float(request.form["y"]),
            z=float(request.form["z"])
        )

        # Convert input data to a DataFrame
        pred_df = data.get_data_as_df()
        print(pred_df)

        # Use the prediction pipeline to predict the price
        predict_pipeline = predictPipeline()
        prediction = predict_pipeline.predict(pred_df)

        return render_template('home.html',prediction=prediction)
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
