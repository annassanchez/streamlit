import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import src.soporteClean as sc
import src.soporteImagenes as si

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

tracks = sc.importDatasets()

st.markdown(f'# Hi there')
st.image('https://64.media.tumblr.com/da7235613f6fe6292360d74d410ece3b/01bebaf99b141ae6-a4/s500x750/1070b19f89a4cc2c1b3420495fb027fcfb1acc9f.gif')
st.markdown("""
This is an investigation based on the `top 200` and `viral 50` spotify playlists on the USA region between 2017 and 2021 to see if there's a significant change on the musics upliftness.
This are the variables taken into account. 
- `Valence` is considered as how positive the music is percieved, being 1 the most positive and 0 the most negative
- `Energy` is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.
- `Danceability` describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
- The `key` the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on.  
- `Mode` indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived.
""")
