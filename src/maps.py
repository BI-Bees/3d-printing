import pygal
import pandas as pd

# Creating a map graph that displays how many 3-printers a country produces
def create_data_map(df, df_country):
    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'Antal 3D-Printere producenter per land'

    df_map = df.Country.unique()
    for countries in df_map:
        worldmap_chart.add(countries + ' ' + str(df.Country.value_counts()[countries]), {
            countries.lower(): df.Country.value_counts()[countries]
        })

    return worldmap_chart
