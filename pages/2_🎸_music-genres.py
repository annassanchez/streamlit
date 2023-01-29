import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import src.soporteClean as sc
import src.soporteImagenes as si

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

tracks = sc.importDatasets()