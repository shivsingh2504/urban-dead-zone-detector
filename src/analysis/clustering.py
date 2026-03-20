from sklearn.cluster import DBSCAN
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors
import numpy as np
import matplotlib.pyplot as plt


def plot_k_distance(scaled_data):
    neigh = NearestNeighbors(n_neighbors=5)
    nbrs = neigh.fit(scaled_data)
    distances, _ = nbrs.kneighbors(scaled_data)

    distances = np.sort(distances[:, 4])

    plt.figure()
    plt.plot(distances)
    plt.title("K-Distance Graph (Find eps here)")
    plt.xlabel("Points sorted")
    plt.ylabel("Distance")
    plt.show()


def apply_dbscan(city_with_counts):
    city = city_with_counts.copy()

    # Feature engineering
    city["POI per Area"] = city["POI Count"] / (city["Area"] + 1)
    city["Log Density"] = np.log1p(city["POI per Area"])

    # Scaling
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(city[["Log Density"]])

    # ✅ 🔥 SHOW GRAPH HERE
    plot_k_distance(scaled)

    # DBSCAN
    dbscan = DBSCAN(eps=0.06, min_samples=5)
    city["Cluster"] = dbscan.fit_predict(scaled)

    print("Cluster counts:\n", city["Cluster"].value_counts())

    return city

def label_clusters(city_with_counts):
    city = city_with_counts.copy()

    # Default: everything is Dead Zone
    city["Cluster Zone"] = "Dead Zone"

    # Only consider non-noise clusters
    valid = city[city["Cluster"] != -1]

    # If no clusters found
    if valid.empty:
        return city

    # Rank clusters by density
    cluster_means = valid.groupby("Cluster")["POI per Area"].mean()
    sorted_clusters = cluster_means.sort_values().index

    # If only one cluster → treat as Active
    if len(sorted_clusters) == 1:
        city.loc[city["Cluster"] != -1, "Cluster Zone"] = "Active Zone"
        return city

    # Assign labels
    for i, cluster in enumerate(sorted_clusters):
        if i == 0:
            label = "Developing Zone"
        else:
            label = "Active Zone"

        city.loc[city["Cluster"] == cluster, "Cluster Zone"] = label

    return city