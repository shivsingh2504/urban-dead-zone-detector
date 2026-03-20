from sklearn.cluster import KMeans

def apply_kmeans(city_with_counts):
  features = city_with_counts[["POI Density"]]