# librerias
import streamlit as st
import pandas as pd

import plotly.express as px
# codigo

felinos = pd.read_csv('felinos_filtrado.csv')
st.title("Gráfico")
felinos_species = felinos['species'].value_counts()
fig = px.bar(
    felinos, 
    x='species', 
    title="Cantidad de felinos por especie"
)
st.plotly_chart(fig)



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
