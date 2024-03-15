import pandas as pd
import matplotlib.pyplot as plt
import sys
import subprocess

def create_visualization(df):

    # Task 1: visualization Total Gross vs. Inflation Adjusted Gross using scatter plot:
    plt.figure(figsize=(8, 6))
    plt.scatter(df['total_gross'], df['inflation_adjusted_gross'], alpha=0.5)
    plt.title('Total Gross vs. Inflation Adjusted Gross')
    plt.xlabel('Total Gross')
    plt.ylabel('Inflation Adjusted Gross')
    plt.savefig('service-result/vis1.png')

    # Task 2: visualization Release Date vs. Total Gross using scatter plot:
    plt.figure(figsize=(8, 6))
    plt.scatter(df['release_date'], df['total_gross'], alpha=0.5)
    plt.title('Release Date vs. Total Gross')
    plt.xlabel('Release Year')
    plt.ylabel('Total Gross')
    plt.savefig('service-result/vis2.png')


    # Task 3: visualization Release Date vs. Total Gross using Plot bar chart:
    # Aggregate total gross by release date
    total_gross_by_date = df.groupby('release_date')['total_gross'].sum()
    # Plot bar chart
    plt.figure(figsize=(10, 6))
    total_gross_by_date.plot(kind='bar' , color='skyblue')
    plt.title('Release Date vs. Total Gross')
    plt.xlabel('Release Year')
    plt.ylabel('Total Gross')
    plt.xticks(rotation=45) 
    plt.tight_layout()  
    plt.savefig('service-result/vis3.png')




def main():
    # Load DataFrame passed from eda.py
    df = pd.read_csv('service-result/res_dpre.csv')
    
    # Create visualization
    create_visualization(df)
    print("Data have been visualized, and you can see your visualized data now ")
    
    # Invoke model.py
    subprocess.run(['python3', 'model.py'])

if __name__ == "__main__":
    main()
