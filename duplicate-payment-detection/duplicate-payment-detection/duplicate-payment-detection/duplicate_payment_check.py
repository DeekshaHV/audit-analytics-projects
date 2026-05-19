import pandas as pd

# Load dataset
df = pd.read_csv("payments.csv")

# Detect duplicate payments
duplicates = df[df.duplicated(
    subset=['invoice_no', 'vendor', 'amount'],
    keep=False
)]

print("=== Duplicate Payments Detected ===")
print(duplicates)

# Count duplicates
print("\nTotal duplicate records found:", len(duplicates))
