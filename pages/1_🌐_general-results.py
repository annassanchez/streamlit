import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import src.soporteClean as sc
import src.soporteImagenes as si

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

tracks = sc.importDatasets()

st.markdown(f'# Hi there')
st.markdown("""this is an investigation based on the top 200 and viral 50 spotify playlist on the USA region between 2017 and 2021 to see if theres a significant change on the musics upliftness
""")
chart = tracks['chart'].unique().tolist()
chart_input = st.selectbox(f'## Choose which playlist you want to analyze', chart)

st.markdown(f"""This is the evolution of valence throught the given period. 
- Valence is considered as how positive the music is percieved, being 1 the most positive and 0 the most negative
- Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.
- Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
""")
si.valence_general(tracks, chart_input)
st.image('imagenes/valence_general.png')

chart_type = st.selectbox('Choose the visualization type', ['boxplot', 'violinplot'])
column = st.selectbox('Choose the variable to see the evolution', ['energy', 'danceability', 'valence'])
si.general_chart(tracks, chart_input, column, chart_type)
st.image(f'imagenes/general_{chart_type}_{column}.png')

st.markdown(f"""Some other variables that need to be taken into account are: 
- The key the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on.  
- Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived""")

si.general_kde(tracks, chart_input, 'key_mapped')
st.image(f'imagenes/general_kde_key_mapped.png')
si.general_kde(tracks, chart_input, 'mode_mapped')
st.image(f'imagenes/general_kde_mode_mapped.png')