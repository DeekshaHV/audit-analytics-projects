import pandas as pd

# Load payment dataset
df = pd.read_csv("payments.csv")

# Detect duplicate payments
duplicates = df[df.duplicated(
    subset=['invoice_no', 'vendor', 'amount'],
    keep=False
)]

print("=== DUPLICATE PAYMENTS DETECTED ===")
print(duplicates)

# Summary statistics
print("\n=== AUDIT SUMMARY ===")
print("Total transactions:", len(df))
print("Duplicate records found:", len(duplicates))
print("Affected vendors:", duplicates['vendor'].nunique())

# Risk classification
duplicates['risk_level'] = 'High'

print("\n=== RISK CLASSIFICATION ===")
print(duplicates[['invoice_no', 'vendor', 'risk_level']])
