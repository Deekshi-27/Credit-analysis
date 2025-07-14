from flask import Flask, render_template, request
import pandas as pd
from catboost import CatBoostClassifier
import joblib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        input_data = {key: request.form.getlist(key) if request.form.getlist(key) and key == 'Payment_Behaviour' else request.form[key] for key in request.form}

        # Define categorical and numerical columns
        categorical = ['Payment_of_Min_Amount', 'Payment_Behaviour', 'Month', 'type_of_loan', 'Credit_History_Age']
        numerical = ['Age', 'Annual_Income', 'Monthly_Inhand_Salary', 'Num_Bank_Accounts', 'Num_Credit_Card', 'Interest_Rate',
                     'Num_of_Loan', 'Delay_from_due_date', 'Num_of_Delayed_Payment', 'Changed_Credit_Limit',
                     'Num_Credit_Inquiries', 'Outstanding_Debt', 'Credit_Utilization_Ratio', 'Total_EMI_per_month',
                     'Amount_invested_monthly', 'Monthly_Balance']

        # Convert input to dataframe and correct types
        new_data = pd.DataFrame([input_data])
        for col in numerical:
            new_data[col] = pd.to_numeric(new_data[col])

        # Handle the list of Payment_Behaviour values
        if 'Payment_Behaviour' in new_data.columns:
            # You might need to adjust how you handle multiple selections
            # depending on how your model was trained.
            # For now, let's join the selected behaviors into a single string.
            new_data['Payment_Behaviour'] = new_data['Payment_Behaviour'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
            new_data['Payment_Behaviour'] = new_data['Payment_Behaviour'].astype('category')

        for col in [c for c in categorical if c != 'Payment_Behaviour']:
            new_data[col] = new_data[col].astype('category')

        # Load model and encoder
        model = CatBoostClassifier()
        model.load_model('credit_model.cbm')
        le = joblib.load('label_encoder.pkl')

        # Predict
        predictions = model.predict(new_data[categorical + numerical])
        predictions = le.inverse_transform(predictions.astype(int))
        predicted_score = predictions[0]

        return render_template('/form.html', prediction=predicted_score, inputs=input_data)

if __name__ == '__main__':
    app.run(debug=True)