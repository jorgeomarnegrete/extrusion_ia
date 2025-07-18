import streamlit as st
from db import get_connection

def mostrar_formulario():
    st.subheader("📋 Ingreso de parámetros de extrusión")

    mat1 = st.number_input("MAT 1 (%)", value=60.0)
    vel_motor_a = st.number_input("Velocidad Motor A (Hz)", value=65.0)
    z1 = st.number_input("Temperatura Z-1 (°C)", value=195.0)
    otc_01 = st.number_input("OTC-01 (°C)", value=90.0)
    aceptada = st.selectbox("¿Placa OK?", ["SI", "NO"]) == "SI"

    if st.button("Guardar datos"):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO extrusion_corridas (mat1, velocidad_motor_a, z1, otc_01, aceptada)
            VALUES (%s, %s, %s, %s, %s)
        """, (mat1, vel_motor_a, z1, otc_01, aceptada))
        conn.commit()
        conn.close()
        st.success("✅ Corrida guardada correctamente.")