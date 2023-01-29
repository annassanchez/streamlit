import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import src.soporteClean as sc
import src.soporteImagenes as si

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

tracks = sc.importDatasets()

st.markdown(f'# These are the general results')

chart = tracks['chart'].unique().tolist()
chart_input = st.selectbox(f'## Choose which playlist you want to analyze', chart)

st.markdown(f"""This is the evolution of `valence`, `danceability` and `energy` throught the given period. 
""")
si.valence_general(tracks, chart_input)
st.image('imagenes/valence_general.png')

chart_type = st.selectbox('Choose the visualization type', ['boxplot', 'violinplot'])
column = st.selectbox('Choose the variable to see the evolution', ['energy', 'danceability', 'valence'])
si.general_chart(tracks, chart_input, column, chart_type)
st.image(f'imagenes/general_{chart_type}_{column}.png')

st.markdown(f"""Here are the `key` and the `mode` in the given period: 
""")

si.general_kde(tracks, chart_input, 'key_mapped')
st.image(f'imagenes/general_kde_key_mapped.png')
si.general_kde(tracks, chart_input, 'mode_mapped')
st.image(f'imagenes/general_kde_mode_mapped.png')