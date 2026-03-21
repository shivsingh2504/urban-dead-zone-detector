import pandas as pd
import numpy as np

def classify_zones(city):
    city = city.copy()

    # Feature engineering
    city["POI per Area"] = city["POI Count"] / (city["Area"] + 1)

    # Log transform (stabilizes distribution)
    city["Log Density"] = np.log1p(city["POI per Area"])

    # Quantile-based zoning (core logic)
    city["Zone Type"] = pd.qcut(
        city["Log Density"],
        q=3,
        labels=["Dead Zone", "Developing Zone", "Active Zone"],
        duplicates="drop"
    )

    return city
