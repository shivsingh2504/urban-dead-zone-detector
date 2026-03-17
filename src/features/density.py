import geopandas as gpd
def calculate_density(city, joined):
    # Count POIs per neighborhood
    poi_counts = joined.groupby("Name").size().reset_index(name="POI Count")

    # Merge with city data
    city = city.merge(poi_counts, on="Name", how="left")
    city["POI Count"] = city["POI Count"].fillna(0)

    # Convert to metric CRS for area calculation
    city = city.to_crs(epsg=3857)

    # Calculate area
    city["Area"] = city.geometry.area

    # Density = count / area
    city["POI Density"] = city["POI Count"] / city["Area"]

    return city