import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import src.soporteClean as sc
import src.soporteImagenes as si

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

tracks = sc.importDatasets()

st.markdown(f"""# These are the results by top artists
These are the 10 top most streamed music genres:
""")

top_artists = sc.info_artists(tracks)
st.dataframe(top_artists)

chart = tracks['chart'].unique().tolist()
chart_input = st.selectbox(f'## Choose which playlist you want to analyze', chart)

st.markdown(f"""
Let's see the evolution of the `valence`, `danceability` and `energy` in the given period:
""")

column = st.selectbox('Choose the variable to see the evolution', ['energy', 'danceability', 'valence'])

si.artist_lineplot(tracks, chart_input, top_artists['artist'].tolist(), column)
st.image(f'imagenes/lineplot_artist_{column}.png')

chart_type = st.selectbox('Choose the visualization type', ['boxplot', 'violinplot'])
si.general_chart_artist(tracks, chart_input, top_artists['artist'].tolist(), column, chart_type)
st.image(f'imagenes/artist_{chart_type}_{column}.png')

st.markdown(f"""
Let's see the `key` and `mode` in the given period:
""")

si.artist_kde(tracks, chart_input, top_artists['artist'].tolist(), 'key_mapped')
st.image(f'imagenes/artists_kde_key_mapped.png')
si.artist_kde(tracks, chart_input, top_artists['artist'].tolist(), 'mode_mapped')
st.image(f'imagenes/artists_kde_mode_mapped.png')