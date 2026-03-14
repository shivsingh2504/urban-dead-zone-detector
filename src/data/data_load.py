import geopandas as gpd

def load_city(path):
  print("Loading shapefile...")
  gdf = gpd.read_file(path)
  print("File loaded!")
  return gdf