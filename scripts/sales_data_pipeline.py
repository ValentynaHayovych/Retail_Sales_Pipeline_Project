#Python automation
import pandas as pd
from pandas_gbq import to_gbq

def load_clean_data(path, project_id, dataset_table):
    #1 Load CSV
    df = pd.read_csv(path)

    #2 Clean Data
    df = df.dropna(subset=['ORDERNUMBER', 'ORDERDATE', 'QUANTITYORDERED', 'PRICEEACH'])

    #3 Rename columns
    df.rename(columns={'YEAR_ID': 'YEAR', 'MONTH_ID': 'MONTH'}, inplace = True)

    #4 Convert date
    df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
    df['YEAR'] = df['ORDERDATE'].dt.year
    df['MONTH'] = df['ORDERDATE'].dt.month
    df['MONTH_ID'] = df['ORDERDATE'].dt.month_name()
    df['YEAR-MONTH'] = pd.to_datetime(df['ORDERDATE'].dt.to_period('M').dt.to_timestamp())

    #5 Calculated total sales and difference
    df['total_sales'] = df['QUANTITYORDERED'] * df['PRICEEACH']
    df['difference'] = df['SALES'] - df['total_sales']

    #6 Load to BigQuery
    to_gbq(df, dataset_table, project_id, if_exists='replace')

    #Check for negative differences
    negative_diff = df[df['difference'] < 0]
    total_rows = len(df)
    if not negative_diff.empty:
        print(f"Total rows in dataset: {total_rows}")
        print(f"Total rows with negative difference: {negative_diff}")
        print(negative_diff.head(5))

if __name__ == "__main__":
    load_clean_data(
        "data/retail_sales_cleaned.csv", 
        "retail-sales-pipeline-476503",
        "retail_sales_cleaned.retail_sales_cleaned"
        )