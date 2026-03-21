import matplotlib.pyplot as plt

def plot_density(city):
    fig, ax = plt.subplots(figsize=(10, 10))

    city.plot(
        column="POI Density",
        cmap="Reds",
        legend=True,
        ax=ax
    )

    ax.set_title("POI Density Map")
    


def plot_dead_zones(city):
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches

    fig, ax = plt.subplots(figsize=(10, 8))

    # Base map
    city.plot(ax=ax, color="lightgrey", edgecolor="black")

    # Dead zones
    dead = city[city["Zone Type"] == "Dead Zone"]
    dead.plot(ax=ax, color="red")

    # ✅ Legend
    legend_patches = [
        mpatches.Patch(color="red", label="Dead Zone"),
        mpatches.Patch(color="lightgrey", label="Other Areas")
    ]

    ax.legend(handles=legend_patches)

    ax.set_title("Dead Zones Highlighted")
    plt.show()
    
    

def plot_zone_types(city):
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches

    fig, ax = plt.subplots(figsize=(10, 8))

    colors = {
        "Dead Zone": "red",
        "Developing Zone": "yellow",
        "Active Zone": "green"
    }

    # Plot zones
    for zone, color in colors.items():
        subset = city[city["Zone Type"] == zone]
        subset.plot(
            ax=ax,
            color=color,
            edgecolor="black"
        )

    # ✅ Custom legend
    legend_patches = [
        mpatches.Patch(color=color, label=zone)
        for zone, color in colors.items()
    ]

    ax.legend(handles=legend_patches, title="Zone Type")

    ax.set_title("Urban Zone Classification")
    plt.show()
