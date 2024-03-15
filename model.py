import pandas as pd
import sys
from sklearn.cluster import KMeans
import subprocess

def k_means_clustering(df):

    kmeans = KMeans(n_clusters=3)

    #task 1: K-means 'total_gross' VS. 'inflation_adjusted_gross' :
    df_for_kmeans1 = df[['total_gross', 'inflation_adjusted_gross']]
    df['cluster_total_gross'] = kmeans.fit_predict(df_for_kmeans1)
    cluster_counts1 = df['cluster_total_gross'].value_counts()
    # Save cluster counts
    with open("service-result/k1.txt", "w") as f:
        for cluster_total_gross, count in cluster_counts1.items():
            f.write(f"Cluster {cluster_total_gross}: {count} records\n")


    #task 2: K-means 'release_date' VS. 'total_gross' :
    df_for_kmeans2 = df[['release_date', 'total_gross']]
    df['cluster_release_date'] = kmeans.fit_predict(df_for_kmeans2)
    cluster_counts2 = df['cluster_release_date'].value_counts()
    # Save cluster counts
    with open("service-result/k2.txt", "w") as f:
        for cluster_release_date, count in cluster_counts2.items():
            f.write(f"Cluster {cluster_release_date}: {count} records\n")        


def main():
    # Load DataFrame passed from vis.py
    df = pd.read_csv('service-result/res_dpre.csv')
    
    # Implement K-means algorithm
    k_means_clustering(df)
    print("K means clustering txt files have been saved ")
   

    # Invoke final.sh
    subprocess.run(['./final.sh'])
if __name__ == "__main__":
    main()
