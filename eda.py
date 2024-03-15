import sys
import pandas as pd
import subprocess

def exploratory_data_analysis(df):

    # Example insights
    insight_1 = "The average total gross of Disney movies is ${:,.2f}".format(df['total_gross'].mean())
    insight_2 = "The maximum total gross of Disney movies is ${:,.2f}".format(df['total_gross'].max())
    insight_3 = "The average inflation-adjusted gross of Disney movies is ${:,.2f}".format(df['inflation_adjusted_gross'].mean())

    # Save insights as text files
    with open("service-result/eda-in-1.txt", "w") as f:
        f.write(insight_1)
    with open("service-result/eda-in-2.txt", "w") as f:
        f.write(insight_2)
    with open("service-result/eda-in-3.txt", "w") as f:
        f.write(insight_3)


def main():
    # Load DataFrame passed from dpre.py
    dataset_path = sys.argv[1]
    df = pd.read_csv(dataset_path)
    
    # Conduct exploratory data analysis
    exploratory_data_analysis(df)
    print("Insights data files have been saved ")
    
    # Invoke vis.py
    subprocess.run(['python3', 'vis.py'])

if __name__ == "__main__":
    main()
