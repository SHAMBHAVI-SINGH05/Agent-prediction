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
            # Convert form input into the encoded values used during training.
            date_input = int(request.form.get("Date"))
            if 1 <= date_input <= 7:
                encoded_date = date_input - 1
            elif 0 <= date_input <= 6:
                encoded_date = date_input
            else:
                raise ValueError("Date must be between 1 and 7 for this dataset.")

            day_input = int(request.form.get("Day"))
            day_mapping = {
                1: 1,  # Monday
                2: 5,  # Tuesday
                3: 6,  # Wednesday
                4: 4,  # Thursday
                5: 0,  # Friday
                6: 2,  # Saturday
                7: 3   # Sunday
            }
            if day_input not in day_mapping:
                raise ValueError("Day must be 1-7, corresponding to Monday-Sunday.")
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
