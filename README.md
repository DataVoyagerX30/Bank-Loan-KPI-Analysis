
# Bank Loan Analysis — Python Project

## 🎯 Objective
The goal of this project is to analyze key performance indicators (KPIs) from a bank’s loan dataset to assess lending performance, borrower behavior, and loan quality. By examining metrics such as funded amounts, repayment totals, interest rates, and debt-to-income ratios, the project provides insights into financial health and risk exposure.

## 📋 Overview
This analysis focuses on:
- **Loan Application Trends**: Total and Month-to-Date (MTD) applications.
- **Funded Amounts**: Total and MTD disbursements.
- **Repayment Performance**: Total and MTD amounts received.
- **Interest & DTI Metrics**: Average interest rates and borrower debt-to-income ratios.
- **Loan Quality Breakdown**:
  - **Good Loans**: Fully paid loans with repayment success.
  - **Bad Loans**: Charged-off loans indicating default risk.

## 📌 Key Findings
- **13.8%** of loans are classified as bad (Charged Off).
- **83.3%** are good loans (Fully Paid).
- **Average Interest Rate**: ~12.05%
- **Average DTI**: ~13.33%
- **Top 10% of loans** contribute significantly to total repayments.

## 🧠 Skills & Tools Used
### Data Analysis
- Data Cleaning and Preprocessing
- Descriptive Statistics

### Data Visualization
- Matplotlib
- Seaborn

### Statistical Analysis
- Correlation Analysis

### Programming Language
- Python

### Libraries
- Pandas
- Numpy
- Matplotlib
- Seaborn

## 📁 Files
- `loan_kpi_analysis.py`: Main script for KPI computation
- `financial_loan.xlsx`: Input dataset
- `README.md`: Project documentation

## 🚀 Usage
Place `financial_loan.xlsx` in the same directory and run:
```bash
python loan_kpi_analysis.py
```

## 📎 Notes
Ensure the Excel file has the correct format with columns like `issue_date`, `loan_status`, `loan_amount`, `total_payment`, `int_rate`, and `dti`.
