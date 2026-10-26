import pandas as pd
import streamlit as st
# dataset
felinos =  pd.read_csv('felinos_filtrado.csv')

#titulo y header (cabecera)
st.title("📖 Conociendo nuestros datos")
st.write("Antes de empezar, hay que saber con qué datos estamos trabajando. En esta parte vemos cómo está armado la base de datos de los avistamientos de felinos: cuántas filas y columnas tiene, en cuántas provincias hubo avistamientos y cuáles son.")
st.image("./images/puma.jpg", caption=None, width='stretch')
st.header("📌 Información útil:")

#le asigna a las variables filas y columnas las mismas del metodo shape
filas, columnas = felinos.shape

#corrigiendo dataset | porque tiene error de tipeado en Neuquén y Santa Cruz
felinos["stateProvince"] = felinos["stateProvince"].replace({
    "Neuquen":"Neuquén",
    "Santa cruz":"Santa Cruz"
})

# dropna saca los valores vacios de una columna, unique saca los valores unicos de estos     
nombres_ubic = felinos['stateProvince'].dropna().unique()

# nunique es como el unique pero devuelve directamente el valor y no un array/lista
cant_ubic = felinos['stateProvince'].nunique()

# 1. expander de filas y columnas
with st.expander("¿Cuántas filas y columnas tiene el dataset?"):
    filas, columnas = felinos.shape
    st.write("**¿Qué es una fila? ¿Qué es una columna?**")
    st.write("La forma en la que está hecho este trabajo es mediante una especie de base de datos que está compuesta de filas y columnas. Como una tabla, estilo Excel.")
    columna_1, columna_2 = st.columns(2)
    with columna_1:
        st.image("./images/df.png", caption="Ejemplo de la base de datos usada.", width='stretch')
    with columna_2:
        st.image("./images/excel-filas-y-columnas.png", caption="Ejemplo de una tabla de Excel.", width='stretch')
    st.write(f'La base de datos de los avistamientos tiene **{ filas} filas** y **{columnas} columnas**')

#2. expander de cantidad de provincias que tienen avistajes
with st.expander("¿Cuántas provincias tienen avistamientos?"):
    st.write("¿Qué es un avistamiento?")
    st.write("Por avistamiento entendemos que es la accion de avistar, o sea descurbrir. En este caso es de felinos. Se descubre y se anota/queda registrado sobre este.")
    columna_1, columna_2 = st.columns(2)
    with columna_1:
        st.image("./images/provincias.avif", caption="provincias de Argentina.", width='stretch')
    with columna_2:
        st.image("./images/avistamiento.jpg", caption="avistamiento", width='stretch')
    st.write("La cantidad de provincias que tienen avistaje es: ", cant_ubic)

#3. expander de las provincias que tienen avistajes
with st.expander("¿Cuáles son las provincias que tienen avistamientos?"):
    st.image("./images/provincias.avif", caption="provincias", width='stretch')
    st.write(nombres_ubic)

#4. expander momentaneamente removido porque no le vi sentido usar para las preguntas del desafio (seccion 4)
# with st.expander("¿Cuáles son los nombres de las columnas ?"):
#    st.write(felinos.columns)