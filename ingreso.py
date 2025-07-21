import streamlit as st
from db import get_connection

def mostrar_formulario():
    st.subheader("📋 Ingreso de parámetros de extrusión")

    # Materiales
    mat1 = st.number_input("MAT 1 (%)", value=60.0)
    vel_motor_a = st.number_input("Velocidad Motor A (Hz)", value=65.0)

    # Temperaturas Extrusora A
    z1 = st.number_input("Temperatura Z-1 (°C)", value=0.0)
    z2 = st.number_input("Temperatura Z-2 (°C)", value=0.0)
    z3 = st.number_input("Temperatura Z-3 (°C)", value=0.0)
    z4 = st.number_input("Temperatura Z-4 (°C)", value=0.0)
    z5 = st.number_input("Temperatura Z-5 (°C)", value=0.0)
    z6 = st.number_input("Temperatura Z-6 (°C)", value=0.0)
    z7 = st.number_input("Temperatura Z-7 (°C)", value=0.0)
    z8 = st.number_input("Temperatura Z-8 (°C)", value=0.0)
    z9 = st.number_input("Temperatura Z-9 (°C)", value=0.0)
    z10 = st.number_input("Temperatura Z-10 (°C)", value=0.0)
    z11 = st.number_input("Temperatura Z-11 (°C)", value=0.0)
    z12 = st.number_input("Temperatura Z-12 (°C)", value=0.0)
    z13 = st.number_input("Temperatura Z-13 (°C)", value=0.0)
    z14 = st.number_input("Temperatura Z-14 (°C)", value=0.0)

    # Temperaturas Extrusora B
    otc_01 = st.number_input("OTC-01 (°C)", value=0.0)
    otc_02 = st.number_input("OTC-02 (°C)", value=0.0)
    otc_03 = st.number_input("OTC-03 (°C)", value=0.0)
    otc_04 = st.number_input("OTC-04 (°C)", value=0.0)
    otc_05 = st.number_input("OTC-05 (°C)", value=0.0)
    otc_06 = st.number_input("OTC-06 (°C)", value=0.0)
    otc_07 = st.number_input("OTC-07 (°C)", value=0.0)
    otc_08 = st.number_input("OTC-08 (°C)", value=0.0)
    otc_09 = st.number_input("OTC-09 (°C)", value=0.0)
    
    # Solo Lectura
    aceptada = st.selectbox("¿Placa OK?", ["SI", "NO"]) == "SI"

    if st.button("Guardar datos"):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO extrusion_corridas (mat1, 
                       velocidad_motor_a, 
                       z1, z2, z3, z4, z5, z6, z7,
                       z8, z9, z10, z11, z12, z13, z14, 
                       otc_01, otc_02, otc_03, otc_04, otc_05, otc_06, otc_07, otc_08, otc_09,
                       aceptada)
            VALUES (%s, 
                    %s, 
                    %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s,%s, %s, 
                    %s)
        """, (mat1, 
              vel_motor_a, 
              z1, z2, z3, z4, z5, z6, z7,
              z8, z9, z10, z11, z12, z13, z14,
              otc_01, otc_02, otc_03, otc_04, otc_05, otc_06, otc_07, otc_08, otc_09, 
              aceptada))
        conn.commit()
        conn.close()
        st.success("✅ Corrida guardada correctamente.")