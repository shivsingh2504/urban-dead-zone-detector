from sklearn.cluster import KMeans

def apply_kmeans(city_with_counts):
  features = city_with_counts[["POI Density"]]

  kmeans = KMeans(n_clusters=3, random_state=42)
  city_with_counts["Cluster"] = kmeans.fit_predict(features)
  return city_with_counts

def label_clusters(city_with_counts):
  cluster_mean = city_with_counts.groupby("Cluster")["POI Density"].mean()
  sorted_clusters = cluster_mean.sort_values().index

  mapping = {
    sorted_clusters[0] : "Dead Zone",
    sorted_clusters[1] : "Developing Zone",
    sorted_clusters[2] : "Active Zone"
  }

  city_with_counts["Cluster Zone"] = city_with_counts["Cluster"].map(mapping)
  return city_with_counts