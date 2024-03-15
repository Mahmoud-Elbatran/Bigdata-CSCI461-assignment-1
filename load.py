import sys
import pandas as pd
import subprocess

def main():
    # Get dataset path from command-line argument
    dataset_path = sys.argv[1]
    
    # Read dataset into DataFrame
    df = pd.read_csv(dataset_path)

    # For demonstration purposes, let's print the first few rows of the dataframe
    print(df.head())
    
    # Invoke dpre.py and pass DataFrame path
    subprocess.run(['python3', 'dpre.py', dataset_path])

if __name__ == "__main__":
    main()
