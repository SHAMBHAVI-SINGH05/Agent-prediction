from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle
import joblib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.normpath(os.path.join(BASE_DIR, "..", "static"))

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

# Load model and scaler
model_path = os.path.join(BASE_DIR, "..", "lasso_model.pkl")
scaler_path = os.path.join(BASE_DIR, "..", "agent_scaler.pkl")
model = joblib.load(model_path)
with open(scaler_path, "rb") as f:
    scaler = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def predict():
    prediction = None
    error = None
    graph_generated = False  # Track graph creation

    if request.method == "POST":
        try:
            feature_names = [
                "Date", "Day", "Hour", "Temperature (°C)", "Rain", "Holiday",
                "Offer Active", "Competitor", "Orders", "Promised Time (min)",
                "Actual Time (min)", "Delivered On Time", "Early By (min)",
                "Delay By (min)", "Timing Deviation Cost", "Company_JioMart",
                "Company_Swiggy", "Company_Zepto", "Traffic Level_Low",
                "Traffic Level_Medium", "Order Type_Food", "Order Type_Grocery",
                "Area Type_Urban"
            ]
            # Convert dataset-style form input into the encoded values used by the trained model.
            date_input = request.form.get("Date")
            date_mapping = {
                "2024-06-01": 0,
                "2024-06-02": 1,
                "2024-06-03": 2,
                "2024-06-04": 3,
                "2024-06-05": 4,
                "2024-06-06": 5,
                "2024-06-07": 6,
            }
            if date_input not in date_mapping:
                raise ValueError("Date must be one of 2024-06-01 through 2024-06-07.")
            encoded_date = date_mapping[date_input]

            day_input = request.form.get("Day")
            day_mapping = {
                "Monday": 1,
                "Tuesday": 5,
                "Wednesday": 6,
                "Thursday": 4,
                "Friday": 0,
                "Saturday": 2,
                "Sunday": 3,
            }
            if day_input not in day_mapping:
                raise ValueError("Day must be one of Monday-Sunday.")
            encoded_day = day_mapping[day_input]

            sample_values = [
                encoded_date,
                encoded_day,
                int(request.form.get("Hour")),
                float(request.form.get("Temperature")),
                int(request.form.get("Rain")),
                int(request.form.get("Holiday")),
                int(request.form.get("Offer")),
                int(request.form.get("Competitor")),
                int(request.form.get("Orders")),
                int(request.form.get("Promised")),
                int(request.form.get("Actual")),
                int(request.form.get("Delivered")),
                int(request.form.get("Early")),
                int(request.form.get("Delay")),
                int(request.form.get("Cost")),
                int(request.form.get("JioMart")),
                int(request.form.get("Swiggy")),
                int(request.form.get("Zepto")),
                int(request.form.get("TrafficLow")),
                int(request.form.get("TrafficMedium")),
                int(request.form.get("Food")),
                int(request.form.get("Grocery")),
                int(request.form.get("Urban"))
            ]
            sample = pd.DataFrame([sample_values], columns=feature_names)

            # Predict
            scaled_input = scaler.transform(sample)
            pred = model.predict(scaled_input)[0]
            prediction = round(pred)

            # Generate a dummy graph (replace this with real y_test and y_pred if needed)
            y_test = list(range(50))
            y_pred = [i + np.random.randint(-3, 3) for i in y_test]  # simulated output

            plt.figure(figsize=(8, 5))
            plt.plot(y_test, label="Actual", marker='o')
            plt.plot(y_pred, label="Predicted", marker='x')
            plt.title("Actual vs Predicted Delivery Agents")
            plt.xlabel("Sample Index")
            plt.ylabel("Delivery Agents")
            plt.legend()
            plt.tight_layout()

            # Save plot to the configured static folder
            graph_path = os.path.join(app.static_folder, "graph_actual_vs_predicted.png")
            plt.savefig(graph_path)
            plt.close()
            graph_generated = True

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template("form.html", prediction=prediction, graph=graph_generated, error=error)

if __name__ == "__main__":
    app.run(debug=True)
