# librerias
import streamlit as st

# banner
st.image("./images/banner_felinos.png", caption=None, width='stretch')

# texto introduccion
st.header("¿De qué trata esta app?")
st.write(
    "En Argentina viven felinos silvestres, como el puma o el yaguareté. "
    "Cuando alguien ve a uno en la naturaleza, o una cámara lo registra, se anota qué animal era, "
    "dónde y cuándo. A cada una de esas anotaciones la llamamos **avistamiento**."
)
st.write(
    "Esta app reúne esos avistamientos y los muestra de forma sencilla, "
    "para descubrir qué felinos viven en el país y en qué lugares se los ha visto."
)

st.header("¿Cómo se recorre?")
st.write(
    "La app tiene tres secciones que conviene ver en orden. Primero conocemos la información "
    "con la que vamos a trabajar, después la vemos en gráficos y, por último, la ubicamos en un mapa. "
    "Todas están en el menú de la izquierda."
)

st.header("El desafío")
st.write(
    "Al terminar el recorrido te espera un juego de preguntas sobre lo que viste en cada sección. "
    "Sirve para comprobar cuánto aprendiste, y no pasa nada si te equivocás: "
    "cada respuesta te dice si estuvo bien y, si no, cuál era la correcta. La idea es que te vayas con más conocimiento de cuando viniste."
)