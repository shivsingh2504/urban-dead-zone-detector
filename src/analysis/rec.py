import numpy as np
from sklearn.neighbors import NearestNeighbors
def recommend_zones(city):
  city["Centroid"] = city.geometry.centroid
  city["X"] = city.centroid.x
  city["Y"] = city.centroid.y

  coords = city[["X","Y"]].values
  NN = NearestNeighbors(n_neighbors=5)
  NN.fit(coords)

  distances, indices = NN.kneighbors(coords)

  demand = []
  for n in indices:
    demand.append(city.iloc[n]["POI per Area"].mean())
  city["Demand Score"] = demand

  min_val = city["POI per Area"].min()
  max_val = city["POI per Area"].max()

  city["Normalized Density"] = (city['POI per Area']-min_val)/(max_val-min_val + 1e-9)

  city["Opportunity Score"] = (0.6*(1 - city["POI per Area"]) + 0.4* (city["Normalized Density"]))
  return city

def get_opp(city,n):
  return city.sort_values(by = "Opportunity Score" , ascending = False)[["Name", "Opportunity Score", "POI Density"]].head(n)