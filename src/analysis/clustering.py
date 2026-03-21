from sklearn.cluster import DBSCAN
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def apply_dbscan(city_with_counts):
    city = city_with_counts.copy()

    # Feature engineering
    city["POI per Area"] = city["POI Count"] / (city["Area"] + 1)
    city["Log Density"] = np.log1p(city["POI per Area"])

    # Scaling
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(city[["Log Density"]])


    # DBSCAN
    dbscan = DBSCAN(eps=0.02, min_samples=5)
    city["Cluster"] = dbscan.fit_predict(scaled)

    print("Cluster counts:\n", city["Cluster"].value_counts())

    return city



def label_clusters(city):
    city = city.copy()

    # Feature
    city["POI per Area"] = city["POI Count"] / (city["Area"] + 1)

    # ✅ Step 1: Quantile-based zoning (main logic)
    city["Zone Type"] = pd.qcut(
        city["POI per Area"],
        q=3,
        labels=["Dead Zone", "Developing Zone", "Active Zone"]
    )

    # ✅ Step 2: Override extreme dead zones using DBSCAN
    city.loc[city["Cluster"] == -1, "Zone Type"] = "Dead Zone"

    return city