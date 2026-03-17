def detect_dead_zones(city):
    """
    Identify dead zones based on POI density threshold
    """
    threshold = city["POI Density"].quantile(0.25)

    city["Dead Zone"] = city["POI Density"] < threshold

    return city