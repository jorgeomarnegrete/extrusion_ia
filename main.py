import streamlit as st
from ingreso import mostrar_formulario
from sugerencias import mostrar_sugerencias

st.set_page_config(page_title="Sistema de Extrusión IA", layout="wide")
st.title("🧠 Sistema de Extrusión Inteligente")

opcion = st.sidebar.radio("Seleccionar sección", ["📋 Ingreso de datos", "🔍 Sugerencias", "📈 Historial"])

if opcion == "📋 Ingreso de datos":
    mostrar_formulario()
elif opcion == "🔍 Sugerencias":
    mostrar_sugerencias()
elif opcion == "📈 Historial":
    st.info("Esta sección estará disponible próximamente.")