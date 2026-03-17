from src.data.data_load import load_city
from src.data.poi_fetch import fetch_pois
from src.features.dead_zone import detect_dead_zones
from src.utils.geo_utils import perform_spatial_join
from src.features.density import calculate_density
from src.visual.map_visual import plot_density, plot_dead_zones

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

    # Dead Zone Detection
    city = detect_dead_zones(city)
    print("Dead Zones Identified")

    print(city[["Name", "POI Count", "POI Density", "Dead Zone"]].head())
    
    dead_zones = city[city["Dead Zone"]==True]
    dead_zones_sorted = dead_zones.sort_values(by="POI Density")
    print(dead_zones_sorted[["Name","POI Density"]].head(10))
    # Visualization
    plot_density(city)
    plot_dead_zones(city)


if __name__ == "__main__":
    main()