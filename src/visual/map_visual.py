import matplotlib.pyplot as plt

def plot_density(city):
    """
    Plot POI density map
    """
    fig, ax = plt.subplots() 
    city.plot(
        column="POI Density",
        cmap="Reds",
        legend=True,
        figsize=(10, 10),
        ax=ax
    )
    ax.set_title("POI Density Map")
plt.show()


def plot_dead_zones(city):
    """
    Plot dead zones map
    """
    fig, ax = plt.subplots() 
    city.plot(
        column="Zone Type",
        cmap="coolwarm",
        legend=True,
        figsize=(10, 10),
        ax=ax
    )
    ax.set_title("Dead Zones")
    

def plot_zone_types(city):
    fig, ax = plt.subplots() 
    city.plot(
        column="Zone Type",
        legend = True,
        cmap="RdYlGn",
        edgecolor="black",
        ax=ax
    )
    ax.set_title("Zone Types")
    