import sys
import pandas as pd
import subprocess

def data_cleaning(df):
    # Data Cleaning tasks...

    # Task 1: Remove duplicate rows
    df = df.drop_duplicates()
    # Task 2: Drop rows with missing values
    df = df.dropna()

    return df

def data_transformation(df):
    # Data Transformation tasks...

    # Task 1: Convert categorical variables to numerical using one-hot encoding
    df = pd.get_dummies(df, columns=['genre'])
    # Task 2: Convert date-time strings to datetime objects
    df['release_date'] = pd.to_datetime(df['release_date'])
   
    return df

def data_reduction(df):
    # Data Reduction tasks...

    # Task 1: Extracting year from datetime and assigning it back to the column
    df['release_date'] = df['release_date'].dt.year
    
    return df

def data_discretization(df):
    # Data Discretization tasks...

    # Discretize total_gross and inflation_adjusted_gross into quartiles
    df['total_gross_category'] = pd.qcut(df["total_gross"], q=3, labels=['Low', 'Medium', 'High'])
    df['inflation_adjusted_gross_category'] = pd.qcut(df["inflation_adjusted_gross"], q=3, labels=['Low', 'Medium', 'High'])
    return df

def main():
    # Load DataFrame passed from load.py
    dataset_path = sys.argv[1]
    df = pd.read_csv(dataset_path)
    
    # Data Preprocessing steps
    df = data_cleaning(df)
    df = data_transformation(df)
    df = data_discretization(df)
    df = data_reduction(df)
   
    # Save the resulting DataFrame to a new CSV file
    df.to_csv('service-result/res_dpre.csv', index=False)
    print("Preprocessed data saved to res_dpre.csv")
    
    # Invoke eda.py and pass DataFrame path
    subprocess.run(['python3', 'eda.py', 'service-result/res_dpre.csv'])

if __name__ == "__main__":
    main()
