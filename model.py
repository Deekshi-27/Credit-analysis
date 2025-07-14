# train_model.py
import pandas as pd
from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

def preprocess_data(df):
    categorical = ['Payment_of_Min_Amount', 'Payment_Behaviour', 'Month', 'type_of_loan', 'Credit_History_Age']
    numerical = ['Age', 'Annual_Income', 'Monthly_Inhand_Salary', 'Num_Bank_Accounts', 'Num_Credit_Card', 'Interest_Rate',
                 'Num_of_Loan', 'Delay_from_due_date', 'Num_of_Delayed_Payment', 'Changed_Credit_Limit',
                 'Num_Credit_Inquiries', 'Outstanding_Debt', 'Credit_Utilization_Ratio', 'Total_EMI_per_month',
                 'Amount_invested_monthly', 'Monthly_Balance']

    df[categorical] = df[categorical].fillna('Unknown')
    df[numerical] = df[numerical].fillna(df[numerical].mean())

    le = LabelEncoder()
    df['Credit_Score'] = le.fit_transform(df['Credit_Score'])

    X = df[categorical + numerical]
    y = df['Credit_Score']
    return X, y, le, categorical, numerical

def train_model(file_path='customer_data.csv', model_path='credit_model.cbm', encoder_path='label_encoder.pkl'):
    df = pd.read_csv('customer_data.csv')
    X, y, le, categorical, numerical = preprocess_data(df)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    model = CatBoostClassifier(iterations=500, depth=6, learning_rate=0.1, cat_features=categorical, verbose=100)
    model.fit(X_train, y_train)

    model.save_model(model_path)
    joblib.dump(le, encoder_path)

    print(f"Model saved to {model_path}")
    print(f"Label encoder saved to {encoder_path}")

if __name__ == "__main__":
    train_model()
