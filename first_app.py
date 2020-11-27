import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px

st.title('Hallo Tabs!')

text = 'Wie geht es dir?'
text


# Import City-Dataframe
#df_cities = pd.read_csv('/Users/msenske/Desktop/FC Bayern München/Innovationszentrum/Python/Data/Sonstiges/simplemaps_worldcities_basicv1/worldcities.csv')

#countries_europe = ['Germany','France','Finland','Italy','Spain','United Kingdom','Poland']
#df_largest_cities_europe = df_cities[df_cities['country'].isin(countries_europe)].sort_values('population', ascending=False)
#df_largest_cities_europe_sel = df_largest_cities_europe.copy()
#df_largest_cities_europe_sel['population'] = df_largest_cities_europe_sel['population'] * 2

#df_largest_cities_world = df_cities.sort_values('population', ascending=False)
#df_largest_cities_world_sel = df_largest_cities_world.copy()
#df_largest_cities_world_sel['population'] = df_largest_cities_world_sel['population'] / 5

#df_sel = pd.concat([df_largest_cities_world_sel.head(50), df_largest_cities_europe_sel.head(20)])

#fig = px.scatter_mapbox(df_sel, lat="lat", lon="lng", size='population', hover_name="city", hover_data=["country", "population"],
#                        color_discrete_sequence=["fuchsia"], zoom=1.75, height=700)
#fig.update_layout(mapbox_style="open-street-map")
#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#fig
