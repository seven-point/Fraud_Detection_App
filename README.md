# 💸 Fraud Detection Web App (Flask + Machine Learning)

This is a simple yet powerful fraud detection system built using **Flask** and a pre-trained machine learning model. It takes user-input transaction details and predicts whether the transaction is **fraudulent** or **legitimate**.

---

## 🔍 Features

- Input transaction details via a web form
- Manual feature engineering (e.g., amount-to-balance ratio)
- Manual label encoding of transaction type
- Real-time prediction with a trained fraud detection model
- Clean and minimal HTML interface
- Ready for deployment

---

## 🧠 Model Details

The model was trained on a real-world financial transactions dataset with ~6.3 million rows and 11 features, including:

- `step` (time of transaction)
- `type` (transaction type)
- `amount`, `oldbalanceOrg`, `newbalanceOrig`
- `oldbalanceDest`, `newbalanceDest`
- Derived features like `zero_balance_flag`, `amount_to_balance_ratio`

---

## 🚀 How to Run Locally

### 1. Clone the repository

bash
git clone https://github.com/your-username/fraud-detection-app.git
cd fraud-detection-app

2. Install dependencies
Make sure Python 3.7+ is installed. Then:

bash
pip install -r requirements.txt

3. Add your trained model
Place your fraud_model.pkl (pickle file of your trained ML model) inside the project folder.

4. Run the Flask app
bash
python app.py
The app will be available at http://127.0.0.1:5000/.
