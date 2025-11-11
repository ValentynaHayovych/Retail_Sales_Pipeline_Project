import pandas as pd

df = pd.read_csv(r'C:\Users\mante\OneDrive\Documents\Retail_Sales_Pipeline\data\retail_sales_cleaned.csv',
                 encoding='latin1')
print(df.head()) # first 5 rows
print(df.info()) # summary of the dataframe
print(df.isnull().sum()) # check for missing values
print(df.dtypes)
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce', infer_datetime_format=True)
print(df['ORDERDATE'].head())
df['PHONE'] = df['PHONE'].str.replace(r'\D', '', regex=True)

df = df.dropna(subset=['ORDERNUMBER', 'ORDERDATE', 'QUANTITYORDERED', 'PRICEEACH'])
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
df['total_sales'] = df['QUANTITYORDERED'] * df['PRICEEACH']
print(df[['QUANTITYORDERED', 'PRICEEACH', 'total_sales']].head())
print(df.describe())
print(df.dtypes)

print(df.head(10)[['ORDERNUMBER', 'QUANTITYORDERED', 'PRICEEACH', 'SALES', 'total_sales']])
df['difference'] = df['SALES'] - df['total_sales']
print(df[['ORDERNUMBER', 'SALES', 'total_sales', 'difference']].head())

# ========================
# Additional tests start here
#=========================

total_revenue = df['total_sales'].sum()
print(f'Total Revenue: ${total_revenue:,.2f}')

# Verified: Total Revenue is $8,290,886.79
# Matches BigQuery SUM(total_sales) result of 2025-10-30
# Data validation passed

#rename columns
df.rename(columns={'YEAR_ID': 'YEAR', 'MONTH_ID': 'MONTH'}, inplace = True)

#date month data type change
df['MONTH'] = pd.to_datetime(df['MONTH'], format='%B', errors = 'coerce').dt.month_name()
df['YEAR-MONTH'] = pd.to_datetime(df['YEAR'].astype(str) + '-' + df['MONTH'] + '-01')


print(df['MONTH'].unique())
print(df.columns)
print(df['MONTH'].unique()[:12])
