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

puma = felinos[felinos['genus'] == 'Puma']
provincias = sorted(puma['stateProvince'].dropna().unique())

ac1, ac2 = st.columns([0.3, 0.7])
provincia = ac1.selectbox("Provincia", provincias)
puma_prov = puma[puma['stateProvince'] == provincia]

mapa = generar_mapa()

def agregar_marca_puma(row):
    folium.CircleMarker(
        location=[row['lat'], row['lng']],
        radius=6,
        color='red',
        fill=True,
        fill_color='red',
        popup=row['species']
    ).add_to(mapa)

puma_prov.apply(agregar_marca_puma, axis=1)

with ac2:
    st_folium(mapa, key='mapa_pumas')