import folium
import streamlit as st
from streamlit_folium import st_folium
import pandas as pd

def generar_mapa():
    attr = (
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
        'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
    )

    tiles = 'https://wms.ign.gob.ar/geoserver/gwc/service/tms/1.0.0/capabaseargenmap@EPSG%3A3857@png/{z}/{x}/{-y}.png'
    m = folium.Map(
        location=(-33.457606, -65.346857),
        control_scale=True,
        zoom_start=5,
        name='es',
        tiles=tiles,
        attr=attr
    )
    return m


felinos = pd.read_csv('felinos_filtrado.csv')
st.title("Mapa de avistamientos de puma")
mapa = generar_mapa()

puma = felinos[felinos['species'] == 'Puma concolor']

def agregar_marca_puma(row):
    folium.CircleMarker(
        location=[row['lat'], row['lng']],
        radius=6,
        color='red',
        fill=True,
        fill_color='red',
        popup=row['species']
    ).add_to(mapa)

puma.apply(agregar_marca_puma, axis=1)
st_folium(mapa, key='pumas')