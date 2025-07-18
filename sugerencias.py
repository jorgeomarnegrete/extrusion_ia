import streamlit as st
from db import get_connection

def mostrar_sugerencias():
    st.subheader("🔍 Sugerencias del sistema")

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM extrusion_corridas ORDER BY fecha DESC LIMIT 1")
    ultima = cursor.fetchone()
    conn.close()

    if ultima:
        st.write("📄 Última corrida registrada:")
        st.json(ultima)

        # Simulación de sugerencia
        if ultima["z1"] < 190:
            st.warning("⚠️ Temperatura Z-1 baja. Posible mala fusión.")
        elif ultima["otc_01"] > 150:
            st.error("❌ OTC-01 demasiado alta. Riesgo de degradación.")
        else:
            st.success("✅ Parámetros dentro de rango. Proceder con extrusión.")
    else:
        st.info("No hay corridas registradas aún.")