from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load your pre-trained model
with open('fraud_detection_model.pkl', 'rb') as f:
    model = pickle.load(f)

# LabelEncoder logic (must match training)
type_mapping = {
    'CASH_IN': 0,
    'CASH_OUT': 1,
    'DEBIT': 2,
    'PAYMENT': 3,
    'TRANSFER': 4
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input values
        step = int(request.form['step'])
        tx_type = request.form['type'].strip().upper()
        amount = float(request.form['amount'])
        oldbalanceOrg = float(request.form['oldbalanceOrg'])
        newbalanceOrig = float(request.form['newbalanceOrig'])
        oldbalanceDest = float(request.form['oldbalanceDest'])
        newbalanceDest = float(request.form['newbalanceDest'])

        # Manual encoding for type
        if tx_type not in type_mapping:
            return render_template('index.html', prediction_text=f"Unknown transaction type: {tx_type}")
        type_encoded = type_mapping[tx_type]

        # Derived features
        zero_balance_flag = int(oldbalanceOrg == 0)
        amount_to_balance_ratio = amount / (oldbalanceOrg + 1e-6)
        amount_to_balance_ratio = min(amount_to_balance_ratio, 10)

        # Prepare input DataFrame
        input_data = pd.DataFrame([{
            'step': step,
            'type': type_encoded,
            'amount': amount,
            'oldbalanceOrg': oldbalanceOrg,
            'newbalanceOrig': newbalanceOrig,
            'oldbalanceDest': oldbalanceDest,
            'newbalanceDest': newbalanceDest,
            'zero_balance_flag': zero_balance_flag,
            'amount_to_balance_ratio': amount_to_balance_ratio
        }])

        # Make prediction
        prediction = model.predict(input_data)[0]
        result = "Fraudulent Transaction" if prediction == 1 else "Legitimate Transaction"

        return render_template('index.html', prediction_text=f'Prediction: {result}')

    except Exception as e:
        return f"Error: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)