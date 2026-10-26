#librerias
import folium
import streamlit as st
from streamlit_folium import st_folium
import pandas as pd

#dataset
felinos = pd.read_csv('felinos_filtrado.csv')

#titulo
st.title("🗺️ Mapa de avistamientos de puma")
st.write("Como ya vimos, tenemos nuestros datos y una forma de manipularlos para entender que y cuantos son. En esta seccion tenemos otra forma más de manipularlos. Podemos hacer un mapa interactivo, donde podemos ver los avistajes del gene Puma por cada provincia.")
st.image("./images/puma-2.jpg", caption=None, width='stretch')

#corrigiendo dataset | porque tiene error de tipeado en Neuquén y Santa Cruz
felinos["stateProvince"] = felinos["stateProvince"].replace({
    "Neuquen":"Neuquén",
    "Santa cruz":"Santa Cruz"
})

#filtros
puma = felinos[felinos['genus'] == 'Puma']
provincias = sorted(puma['stateProvince'].dropna().unique())


# mapa base
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


def agregar_marca_puma(row):
    folium.CircleMarker(
        location=[row['lat'], row['lng']],
        radius=6,
        color='red',
        fill=True,
        fill_color='red',
        popup=row['species']
    ).add_to(mapa)


ac1, ac2 = st.columns([0.3, 0.7])
provincia = ac1.selectbox("Provincia", provincias)
puma_prov = puma[puma['stateProvince'] == provincia]

mapa = generar_mapa()

puma_prov.apply(agregar_marca_puma, axis=1)

with ac2:
    st_folium(mapa, key='mapa_pumas')