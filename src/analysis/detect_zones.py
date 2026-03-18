from sklearn.preprocessing import MinMaxScaler
def classify_zones(city_with_counts):
  scaler = MinMaxScaler()
  city_with_counts["Density Score"] = scaler.fit_transform(city_with_counts[["POI Density"]])
  low = city_with_counts["Density Score"].quantile(0.33)
  high = city_with_counts["Density Score"].quantile(0.66) 
  def classify_zone(score):
    if score < low:
      return "Dead Zone"
    elif score < high:
      return "Developing Zone"
    else:
      return "Active Zone"
  city_with_counts["Zone Type"] = city_with_counts["Density Score"].apply(classify_zone)
  return city_with_counts
