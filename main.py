from src.data.data_load import load_city
from src.data.poi_fetch import fetch_pois
from src.utils.geo_utils import perform_spatial_join
from src.features.density import calculate_density
from src.analysis.detect_zones import classify_zones
from src.visual.map_visual import plot_density, plot_dead_zones,plot_zone_types
from src.analysis.clustering import apply_dbscan, label_clusters
import matplotlib.pyplot as plt
def main():
    # Load data
    city = load_city("data/raw/ZillowNeighborhoods-NY.shp")
    city = city[city["City"] == "New York"]

    pois = fetch_pois("New York, USA")

    print("Data Loaded")

    # Spatial Join
    joined = perform_spatial_join(pois, city)
    print("Spatial Join Done")

    # Density Calculation
    city = calculate_density(city, joined)
    print("Density Calculated")

    # Zone Classification (NEW LOGIC)
    city = classify_zones(city)
    print("Zones Classified")

    # Preview
    print(city[["Name", "POI Density", "Zone Type"]].head())

    # Get worst dead zones
    dead_zones = city[city["Zone Type"] == "Dead Zone"]
    dead_zones_sorted = dead_zones.sort_values(by="POI Density")

    print("\nTop 10 Worst Dead Zones:")
    print(dead_zones_sorted[["Name", "POI Density"]].head(10))

    print(city["Zone Type"].value_counts())
    # Visualization
    plot_density(city)
    plot_dead_zones(city)
    plot_zone_types(city)
    
    plt.show()



if __name__ == "__main__":
    main()