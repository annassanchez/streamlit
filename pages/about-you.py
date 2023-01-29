import streamlit as st
import src.soporteClean as sc

st.markdown(f'# Hola amiga narcisita')

tracks = sc.importDatasets()
#st.dataframe(tracks, width=700, height=200)
artistas = tracks['artist'].unique().tolist()
artista_input = st.selectbox('Elige un artista', artistas)

if artista_input != '':
    st.markdown(f'### Has elegido {artista_input}, vamos a ver como de tristes han estado')
    artista_info = sc.info_artistas(artista_input, tracks)
    st.dataframe(artista_info, width=700, height=200)
else:
    st.markdown(f'# Elígeme algo amiga')