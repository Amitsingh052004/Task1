import pandas as pd

# Load the uploaded CSV file
file_path = "marketing_campaign.csv"
df = pd.read_csv(file_path, sep='\t')

# Step 1: View basic info
initial_info = df.info()
initial_head = df.head()

# Step 2: Handle missing values
missing_values_before = df.isnull().sum()
df = df.dropna()  # Alternatively, df.fillna(value) can be used

# Step 3: Remove duplicates
df = df.drop_duplicates()

# Step 4: Standardize text values
if 'Gender' in df.columns:
    df['Gender'] = df['Gender'].str.upper().str.strip()
    df['Gender'] = df['Gender'].replace({'F': 'Female', 'M': 'Male'})

# Step 5: Convert date formats
if 'Dt_Customer' in df.columns:
    df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y', errors='coerce')

# Step 6: Rename columns to be clean and uniform
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 7: Check and fix data types
if 'income' in df.columns:
    df['income'] = pd.to_numeric(df['income'], errors='coerce')

for col in ['kidhome', 'teenhome']:
    if col in df.columns:
        df[col] = df[col].astype('int')

if 'kidhome' in df.columns and 'teenhome' in df.columns:
    df['total_children'] = df['kidhome'] + df['teenhome']

# Convert a few more numerical columns safely
num_cols = ['income', 'recency', 'mntwines', 'mntfruits']
for col in num_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Final overview
cleaned_info = df.info()
cleaned_head = df.head()

df.to_csv("cleaned_marketing_campaign.csv", index=False)

missing_values_before, initial_head, cleaned_head