import streamlit as st

st.set_page_config(page_title="Juego de Preguntas", page_icon="🎮")
st.title("🎮 Juego de Preguntas")

# ============================================================
# Definimos las preguntas
# ============================================================
preguntas = [
    # ---------- Sección 1: Conociendo nuestros datos ----------
    {
        "pregunta": "¿Cuántos valores únicos tiene la columna stateProvince?",
        "opciones": ["17", "18"],
        "correcta": 0
    },
    {
        "pregunta": "¿Cuántas filas tiene el dataset?",
        "opciones": ["3500", "2019"],
        "correcta": 1
    },
    {
        "pregunta": "¿Cuántas columnas tiene el dataset?",
        "opciones": ["19", "22"],
        "correcta": 0
    },

    # ---------- Sección 2: Graficamos ----------
    {
        "pregunta": "¿Cuál es la especie con menor porcentaje de aparición?",
        "opciones": ["Leopardus pajonales", "Puma concolor"],
        "correcta": 0
    },
    {
        "pregunta": "¿Cuál es la especie con más avistamientos?",
        "opciones": ["Panthera onca", "Puma concolor"],
        "correcta": 1
    },
    {
        "pregunta": "¿Cuál es la tercera provincia con más avistamientos?",
        "opciones": ["Provincia de Corrientes", "Provincia de Buenos Aires"],
        "correcta": 0
    },

    # ---------- Sección 3: Mostramos en mapas ----------
    {
        "pregunta": "¿Cuántas provincias aparecen en el menú del mapa de pumas?",
        "opciones": ["15", "17"],
        "correcta": 1
    },
    {
        "pregunta": "Si elegís Tucumán en el menú, ¿cuántos puntos rojos se ven en el mapa?",
        "opciones": ["1", "5"],
        "correcta": 0
    },
    {
        "pregunta": "¿Qué provincia muestra más puntos rojos en el mapa?",
        "opciones": ["Chubut", "Misiones"],
        "correcta": 1
    },
]

# ============================================================
# Una pregunta por bloque, con su propio botón de verificar
# ============================================================
for i, p in enumerate(preguntas):
    st.subheader(f"Pregunta {i + 1}")
    st.write(p["pregunta"])

    # El radio guarda la elección del estudiante
    eleccion = st.radio(
        "Elegí una opción:",
        p["opciones"],
        key=f"pregunta_{i}",
        index=None,
    )

    # Cada pregunta tiene su propio botón
    if st.button("Verificar", key=f"btn_{i}"):
        if eleccion is None:
            st.warning("⚠️ Elegí una opción antes de verificar.")
        elif eleccion == p["opciones"][p["correcta"]]:
            st.success("✅ ¡Correcto!")
        else:
            correcta = p["opciones"][p["correcta"]]
            st.error(f"❌ Incorrecto. La respuesta correcta era: **{correcta}**")

    st.divider()