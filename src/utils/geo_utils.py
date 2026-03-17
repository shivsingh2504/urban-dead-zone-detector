import geopandas as gpd

def perform_spatial_join(pois, city):
    pois = pois.to_crs(city.crs)
    joined = gpd.sjoin(pois, city, predicate="within")
    return joined