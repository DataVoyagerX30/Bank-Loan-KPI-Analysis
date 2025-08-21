
import pandas as pd
from datetime import datetime

file_path = 'financial_loan.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')
df['issue_date'] = pd.to_datetime(df['issue_date'])
current_month = datetime.now().month
current_year = datetime.now().year
df_mtd = df[(df['issue_date'].dt.month == current_month) & (df['issue_date'].dt.year == current_year)]

print('Total Loan Applications:', len(df))
print('MTD Loan Applications:', len(df_mtd))
print('Total Funded Amount:', df['loan_amount'].sum())
print('MTD Total Funded Amount:', df_mtd['loan_amount'].sum())
print('Total Amount Received:', df['total_payment'].sum())
print('MTD Total Amount Received:', df_mtd['total_payment'].sum())
print('Average Interest Rate:', df['int_rate'].mean())
print('Average DTI:', df['dti'].mean())

bad_loans = df[df['loan_status'] == 'Charged Off']
print('Bad Loan Applications:', len(bad_loans))
print('Bad Loan Application Percentage:', (len(bad_loans) / len(df)) * 100)
print('Bad Loan Funded Amount:', bad_loans['loan_amount'].sum())
print('Bad Loan Total Received Amount:', bad_loans['total_payment'].sum())

good_loans = df[df['loan_status'] == 'Fully Paid']
print('Good Loan Applications:', len(good_loans))
print('Good Loan Application Percentage:', (len(good_loans) / len(df)) * 100)
print('Good Loan Funded Amount:', good_loans['loan_amount'].sum())
print('Good Loan Total Received Amount:', good_loans['total_payment'].sum())
