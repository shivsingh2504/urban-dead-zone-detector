import osmnx as ox
def fetch_pois(place):
  tags={
    'amenity': ["Restaurant","Cafe","Bar","Fast Food"],
    "shop": True
  }
  pois = ox.features_from_place(place,tags)
  return pois
