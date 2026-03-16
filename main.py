from src.data.data_load import load_city
from src.data.poi_fetch import fetch_pois
import geopandas as gpd
city = load_city("data/raw/ZillowNeighborhoods-NY.shp")
print(city.head())
print(city.columns)
pois = fetch_pois("Manhattan, New York, USA")
print("POIs fetched!")
print(pois.head())

pois = pois.to_crs(city.crs)
print("CRS aligned")
joined = gpd.sjoin(pois,city,predicate="within")
print("Spatial join complete!!")
print(joined.head())

poi_counts = joined.groupby("Name").size().reset_index(name="poi_count")
print(poi_counts.head())