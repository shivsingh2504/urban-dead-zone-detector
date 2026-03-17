import geopandas as gpd
def classify_zones(city,threshold=0.000002):
  city["Zone Type"] = "Normal"
  city.loc[city["POI Density"]==0,"Zone Type"]= "Special Zone"
  city.loc[
      (city["POI Density"] < threshold) & (city["POI Density"]>0),"Zone Type"] = "Dead Zone"
  return city