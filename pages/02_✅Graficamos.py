# librerias
import streamlit as st
import pandas as pd

import plotly.express as px
# codigo

felinos = pd.read_csv('felinos_filtrado.csv')
st.title("Gráfico")
felinos_species = felinos['species'].value_counts()

# esto es plotly express (diferente al plotly de pandalyze/jupyter)
# variable = px.tipo_de_grafico(dataframe, x=dataframe.index, y=dataframe.values, title)


#1
fig_1 = px.bar(
    felinos_species, 
    x=felinos_species.index,
    y=felinos_species.values,
    title="Cantidad de felinos por especie"
)
#imprime la fig (figura) st es el alias/apodo de streamlit 
st.plotly_chart(fig_1)

#2
fig_2 = px.pie(
    felinos_species,
    names=felinos_species.index,
    values=felinos_species.values,
    title="Porcentaje de cada especie de avistajes"
)
st.plotly_chart(fig_2)

#3
felinos_provincias = felinos["stateProvince"].value_counts()
fig_3 = px.bar(
    felinos_provincias,
    x=felinos_provincias.index,
    y=felinos_provincias.values,
    title="Felinos por provincia"
)
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
