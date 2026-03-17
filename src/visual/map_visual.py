import matplotlib.pyplot as plt

def plot_density(city):
    """
    Plot POI density map
    """
    city.plot(
        column="POI Density",
        cmap="Reds",
        legend=True,
        figsize=(10, 10)
    )
    plt.title("POI Density Map")
    plt.show()


def plot_dead_zones(city):
    """
    Plot dead zones map
    """
    city.plot(
        column="Dead Zone",
        cmap="coolwarm",
        legend=True,
        figsize=(10, 10)
    )
    plt.title("Dead Zones (Low POI Density)")
    plt.show()