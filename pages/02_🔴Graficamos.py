# librerias
import streamlit as st
import pandas as pd
import plotly.express as px

#dataset
felinos = pd.read_csv('felinos_filtrado.csv')

#titulo y parrafo
st.title("📊 Gráficos")
st.write("Teniendo en cuenta los datos anteriores, se pueden hacer mas cosas que solo saber el nombre de las provincias; donde si hay avistajes; la cantidad; o incluso de las filas y columnas. Podemos hacer graficos para ver de forma visual la magnitud del manejo de datos.")
st.image("./images/tabla-grafico.png", caption= None, width='stretch')
# se usa 'plotly express' (diferente al plotly de pandalyze/jupyter)
# variable = px.tipo_de_grafico(dataframe, x=dataframe.index, y=dataframe.values, title)

#corrigiendo dataset | porque tiene error de tipeado en Neuquén y Santa Cruz
felinos["stateProvince"] = felinos["stateProvince"].replace({
    "Neuquen":"Neuquén",
    "Santa cruz":"Santa Cruz"
})

#filtros
felinos_species = felinos['species'].value_counts()
felinos_provincias = felinos["stateProvince"].value_counts()

#1. figura de barra pero de especie
fig_1 = px.bar(
    felinos_species, 
    x=felinos_species.index,
    y=felinos_species.values,
    title="Cantidad de felinos por especie"
)
#imprime la fig (figura) st es el alias/apodo de streamlit 
with st.expander("De barra por especie"):
    st.plotly_chart(fig_1)

#2. figura de torta
fig_2 = px.pie(
    felinos_species,
    names=felinos_species.index,
    values=felinos_species.values,
    title="Porcentaje de cada especie de avistajes"
)
with st.expander("De torta por especie"):
    st.plotly_chart(fig_2)

#3. figura de barra pero de provincias
fig_3 = px.bar(
    felinos_provincias,
    x=felinos_provincias.index,
    y=felinos_provincias.values,
    title="Felinos por provincia"
)
with st.expander("De barra de felinos por provincia"):
    st.plotly_chart(fig_3)

































#fig,ax = plt.subplots()
# Crear el gráfico de barras
#conteo_tipos = felinos['Ubicación'].value_counts()
#conteo_tipos.plot(kind='bar', ax=ax, color='skyblue')
# Agregar etiquetas y título
#ax.set_xlabel('Provincia')
#ax.set_ylabel('Cantidad')
#ax.set_title('Cantidad de Lagos por provincia')

# Mostrar el gráfico
#st.pyplot(fig)
