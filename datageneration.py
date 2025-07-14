# generate_data.py
import pandas as pd
import numpy as np

def generate_customer_data(file_path='customer_data.csv'):
    data = {
        'Month': np.random.choice(range(1, 13), 100),
        'Age': np.random.randint(18, 70, 100),
        'ID': np.random.randint(1000, 9999, 100),
        'Customer_ID': np.random.randint(1000000, 9999999, 100),
        'Name': np.random.choice(['Alice', 'Bob', 'Charlie', 'David', 'Eve'], 100),
        'SSN': np.random.randint(100000000, 999999999, 100),
        'type_of_loan': np.random.choice(['Personal', 'Home', 'Auto', 'Education'], 100),
        'Credit_History_Age': np.random.choice(['< 1 Year', '1 Year', '2 Years', '3 Years'], 100),
        'Annual_Income': np.random.uniform(20000, 120000, 100).round(2),
        'Monthly_Inhand_Salary': np.random.uniform(1000, 10000, 100).round(2),
        'Num_Bank_Accounts': np.random.randint(1, 5, 100),
        'Num_Credit_Card': np.random.randint(1, 6, 100),
        'Interest_Rate': np.random.uniform(3, 25, 100).round(2),
        'Num_of_Loan': np.random.randint(0, 5, 100),
        'Delay_from_due_date': np.random.randint(0, 30, 100),
        'Num_of_Delayed_Payment': np.random.randint(0, 10, 100),
        'Changed_Credit_Limit': np.random.uniform(0, 5000, 100).round(2),
        'Num_Credit_Inquiries': np.random.randint(0, 5, 100),
        'Outstanding_Debt': np.random.uniform(500, 15000, 100).round(2),
        'Credit_Utilization_Ratio': np.random.uniform(0, 1, 100).round(2),
        'Payment_of_Min_Amount': np.random.choice(['Yes', 'No', 'NM'], 100),
        'Total_EMI_per_month': np.random.uniform(500, 5000, 100).round(2),
        'Amount_invested_monthly': np.random.uniform(100, 2000, 100).round(2),
        'Payment_Behaviour': np.random.choice([
            'High_spent_Small_value_payments', 'Low_spent_Large_value_payments',
            'Low_spent_Medium_value_payments', 'Low_spent_Small_value_payments',
            'High_spent_Medium_value_payments', 'High_spent_Large_value_payments'], 100),
        'Monthly_Balance': np.random.uniform(5000, 10000, 100).round(2),
        'Credit_Score': np.random.choice(['Good', 'Standard', 'Poor'], 100)
    }

    df = pd.DataFrame(data)
    df.to_csv('cust_data.csv', index=False)
    print(f"Data saved to ")

if __name__ == "__main__":
    generate_customer_data()
