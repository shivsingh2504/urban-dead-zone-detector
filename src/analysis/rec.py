import numpy as np
from sklearn.neighbors import NearestNeighbors

def recommend_zones(city):

    # --- 1. Centroids ---
    city["centroid"] = city.geometry.centroid
    city["X"] = city["centroid"].x
    city["Y"] = city["centroid"].y

    # --- 2. Nearest Neighbors ---
    coords = city[["X", "Y"]].values
    nn = NearestNeighbors(n_neighbors=5)
    nn.fit(coords)
    _, indices = nn.kneighbors(coords)

    # --- 3. Demand Score (spatial) ---
    demand = []
    for n in indices:
        demand.append(city.iloc[n]["POI per Area"].mean())
    city["Demand Score"] = demand

    # --- 4. Normalize Density ---
    min_val = city["POI per Area"].min()
    max_val = city["POI per Area"].max()
    city["Normalized Density"] = (
        (city["POI per Area"] - min_val) / (max_val - min_val + 1e-9)
    )

    # --- 5. Normalize Demand ---
    min_d = city["Demand Score"].min()
    max_d = city["Demand Score"].max()
    city["Demand Score"] = (
        (city["Demand Score"] - min_d) / (max_d - min_d + 1e-9)
    )

    # --- 6. Opportunity (Sweet Spot Model) ---
    ideal_density = 0.10
    city["Density Score"] = np.exp(
        -((city["Normalized Density"] - ideal_density) ** 2) / 0.02
    )

    city["Opportunity Score"] = (
        0.4 * city["Density Score"] +
        0.6 * city["Demand Score"]
    )

    # --- 7. Dead Zone Score ---
    city["Dead Zone Score"] = (
        (1 - city["Normalized Density"]) *
        (1 - city["Demand Score"])
    )

    # --- 8. Clean duplicates ---
    city = city.drop_duplicates(subset="Name")

    # --- 9. Filters for Opportunity Zones ---
    city["Is Opportunity Zone"] = (
        (city["Normalized Density"] > 0.05) &
        (city["Normalized Density"] < 0.6) &
        (city["Demand Score"] > 0.25)
    )

    # --- 10. Filters for Dead Zones ---
    city["Is Dead Zone"] = (
        (city["Normalized Density"] < 0.1) &
        (city["Demand Score"] < 0.2)
    )

    return city


def get_opp(city, n):
    return city[city["Is Opportunity Zone"]].sort_values(
        by="Opportunity Score",
        ascending=False
    )[["Name", "Opportunity Score", "POI Density"]].head(n)


def get_dead_zones(city, n):
    return city[city["Is Dead Zone"]].sort_values(
        by="Dead Zone Score",
        ascending=False
    )[["Name", "Dead Zone Score", "POI Density"]].head(n)