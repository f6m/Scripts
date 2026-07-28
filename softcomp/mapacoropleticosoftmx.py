#Previamente se debe tener en el directorio
#los archivos esoft.csv y mxestados.geojson
#cargar librerias pip -U pyfonts
# pip -U pypalettes
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
from pyfonts import load_google_font
from pypalettes import load_cmap


path = "/content/esoft.csv"
df_esoft = pd.read_csv(path,encoding='Latin-1')

path = "/content/mxestados.geojson"
gdf = gpd.read_file(path).merge(df_esoft, on="NOMGEO")
##print(gdf.geometry.head())

##gdf.head()

#Agregamos centroide
#gdf_projected = gdf.to_crs(epsg=3035)
#gdf_projected["centroid"] = gdf_projected.geometry.centroid
#gdf["centroid"] = gdf_projected["centroid"].to_crs(gdf.crs)
#gdf.head()

#Choroplet map
cmap = load_cmap("Sunset2", cmap_type="continuous", reverse=False)

fig, ax = plt.subplots(figsize=(8, 8), dpi=400)

ax.set_xlim(-120, -80)
ax.set_ylim(12, 35)
ax.axis("off")

gdf.plot(ax=ax, column="esoft", cmap=cmap, edgecolor="white", linewidth=1)

bar_ax = ax.inset_axes(bounds=[0.05, -0.05, 0.5, 0.4], zorder=-1)
n, bins, _ = bar_ax.hist(gdf["esoft"], bins=15, alpha=0)
colors = [cmap((val - min(bins)) / (max(bins) - min(bins))) for val in bins]
bar_ax.bar(bins[:-1], n, color=colors, width=2, edgecolor="white", linewidth=1
)

bar_ax.spines[["top", "left", "right"]].set_visible(False)
bar_ax.set_yticks([])
x_ticks = list(range(0, 135, 10))
x_tick_labels = [f"{val}" for val in x_ticks]
bar_ax.set_xticks(x_ticks, labels=x_tick_labels, size=8)
bar_ax.tick_params(axis="x", length=0, pad=5)

fig.tight_layout()
