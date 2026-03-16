from src.data.data_load import load_city
from src.data.poi_fetch import fetch_pois
import geopandas as gpd
import matplotlib.pyplot as plt
city = load_city("data/raw/ZillowNeighborhoods-NY.shp")
city = city[city["City"] == "New York"]
print(city.head())
print(city.columns)
pois = fetch_pois("New York, USA")
print("POIs fetched!")
print(pois.head())

pois = pois.to_crs(city.crs)
print("CRS aligned")
joined = gpd.sjoin(pois,city,predicate="within")
print("Spatial join complete!!")
print(joined.head())

poi_counts = joined.groupby("Name").size().reset_index(name="POI Count")
print(poi_counts.head())

city_with_counts = city.merge(poi_counts, on="Name", how="left")
city_with_counts["POI Count"] = city_with_counts["POI Count"].fillna(0)
print(city_with_counts[["Name","POI Count"]].head())
city_with_counts["Area"] = city_with_counts.geometry.area
city_with_counts["POI Density"]=(city_with_counts["POI Count"]/city_with_counts["Area"])
print(city_with_counts[["Name","POI Count","POI Density"]].head())
city_with_counts["Dead Zone"] = city_with_counts["POI Count"]<10
print(city_with_counts[["Name","POI Count","Dead Zone"]].head())

city_with_counts.plot(
  column="POI Density",
  cmap="Reds",
  legend=True,
  edgecolor="black",
  linewidth=0.3,
  figsize=(12,10)
)
plt.show()