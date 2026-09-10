import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuración inicial de la página
st.set_page_config(page_title="Dashboard: La Ruta del Gerente de Marca", layout="wide")

# Estilos CSS personalizados para mantener la estética corporativa
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1, h2, h3 { color: #003366; }
    </style>
    """, unsafe_allow_html=True)

st.title("🗺️ La Ruta del Gerente de Marca")

# Navegación en la barra lateral
st.sidebar.title("Navegación")
dimension = st.sidebar.radio("Selecciona una Dimensión:", 
                             ["1. Perfil del Puesto", 
                              "2. Avance en La Ruta", 
                              "3. Evaluación de Potencial"])

# ==========================================
# DIMENSIÓN 1: PERFIL DEL PUESTO
# ==========================================
if dimension == "1. Perfil del Puesto":
    st.header("Dimensión 1: ADN del Gerente de Marca")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Misión y Alcance")
        st.write("**Ubicación:** Salta y Jujuy" + "[cite: 5]")
        st.write("**Responsabilidad económica:** P&L integral de la marca" + "[cite: 5]")
        st.info("Liderar integralmente el negocio, garantizando resultados económicos, maximizando rentabilidad y desarrollando equipos ágiles." + "[cite: 5]")
        
        st.subheader("Competencias Clave")
        # Listado de competencias extraídas del perfil
        competencias = ["Visión integral de negocio", "Orientación a resultados y rentabilidad", 
                        "Capacidad analítica", "Liderazgo de líderes", "Toma de decisiones", "Gestión transversal"]
        for comp in competencias:
            st.markdown(f"- {comp}" + "[cite: 5]")
            
    with col2:
        st.subheader("Principales Responsabilidades")
        with st.expander("Gestión Integral y P&L"):
            st.write("Responsable del P&L, gestionar drivers de ingresos/costos y gestionar gastos controlables." + "[cite: 5]")
        with st.expander("Gestión Comercial y Posventa"):
            st.write("Cumplimiento de market share, definición de listas de precios y objetivos de rentabilidad en Posventa." + "[cite: 5]")
        with st.expander("Personas y Liderazgo"):
            st.write("Desarrollar al equipo gerencial e identificar posiciones críticas y sucesores." + "[cite: 5]")
            
        st.subheader("Indicadores de Gestión (KPIs)")
        st.write("- **Rentabilidad:** Resultado económico y cumplimiento de presupuesto." + "[cite: 5]")
        st.write("- **Comercial:** Market share y rotación de stock." + "[cite: 5]")

# ==========================================
# DIMENSIÓN 2: LA RUTA (PLAN DE CARRERA)
# ==========================================
elif dimension == "2. Avance en La Ruta":
    st.header("Dimensión 2: Progreso de Participantes")
    st.markdown("Visualización de los 4 Tramos y 14 Paradas hacia la Gerencia de Marca." + "[cite: 5]")
    
    # Datos simulados de los colaboradores en la ruta
    data_ruta = {
        "Colaborador": ["Alejandro", "Melisa", "Carmelo", "Gonzalo"],
        "Tramo Actual": ["Tramo 2", "Tramo 3", "Tramo 1", "Tramo 4"],
        "Parada Actual": [5, 9, 2, 12],
        "Avance General (%)": [35, 65, 15, 85]
    }
    df_ruta = pd.DataFrame(data_ruta)
    
    # TIP DE PROCESAMIENTO: Al calcular el avance promedio de un grupo, es vital limpiar los datos.
    # Usamos dropna() para asegurar que si un participante aún no tiene métricas (celda vacía), 
    # no se cuente como un cero, evitando distorsionar los promedios del tablero.
    df_ruta_clean = df_ruta.dropna(subset=['Avance General (%)'])
    
    # Gráfico de Gantt / Timeline de progreso
    st.subheader("Mapa de Posicionamiento Actual")
    fig_bar = px.bar(df_ruta_clean, x="Avance General (%)", y="Colaborador", 
                     color="Tramo Actual", orientation='h', 
                     title="Porcentaje de avance por colaborador",
                     range_x=[0,100])
    st.plotly_chart(fig_bar, use_container_width=True)

    # Detalle de Tramos
    st.subheader("Estructura de la Ruta")
    t1, t2, t3, t4 = st.tabs(["Tramo 1: Fundamentos", "Tramo 2: Comercial", "Tramo 3: Sinergia", "Tramo 4: Estrategia"])
    with t1:
        st.write("**Parada 1 a 3:** Capacidad analítica financiera, Gestión por indicadores, Mejora continua." + "[cite: 5]")
    with t2:
        st.write("**Parada 4 a 7:** Orientación comercial, Negociación, Comunicación, Relaciones Institucionales." + "[cite: 5]")
    with t3:
        st.write("**Parada 8 a 10:** Liderazgo de líderes, Desarrollo de equipos, Gestión transversal." + "[cite: 5]")
    with t4:
        st.write("**Parada 11 a 14:** Visión de negocio, Planificación, Orientación a resultados, Toma de decisiones." + "[cite: 5]")

# ==========================================
# DIMENSIÓN 3: EVALUACIÓN DE POTENCIAL
# ==========================================
elif dimension == "3. Evaluación de Potencial":
    st.header("Dimensión 3: Matriz de Talento (9-Box)")
    st.markdown("Clasificación de candidatos pre-ingreso a La Ruta según su desempeño histórico y potencial de liderazgo.")
    
    # Datos simulados para el 9-Box
    data_9box = {
        "Colaborador": ["Alejandro", "Melisa", "Carmelo", "Gonzalo", "Nuevo Candidato"],
        "Desempeño": [3, 4, 2, 5, 3.5], # Escala 1 a 5
        "Potencial": [4, 5, 3, 4, 2]    # Escala 1 a 5
    }
    df_9box = pd.DataFrame(data_9box)
    
    # Construcción gráfica de la matriz 9-Box con Plotly
    fig_9box = px.scatter(df_9box, x="Desempeño", y="Potencial", text="Colaborador",
                          title="Matriz de Evaluación de Reemplazos",
                          range_x=[1, 5], range_y=[1, 5])
    
    # Agregando las divisiones visuales de la matriz (líneas en 2.5 y 3.5 para crear las 9 cajas)
    fig_9box.add_hline(y=2.5, line_width=1, line_dash="dash", line_color="gray")
    fig_9box.add_hline(y=3.5, line_width=1, line_dash="dash", line_color="gray")
    fig_9box.add_vline(x=2.5, line_width=1, line_dash="dash", line_color="gray")
    fig_9box.add_vline(x=3.5, line_width=1, line_dash="dash", line_color="gray")
    
    fig_9box.update_traces(textposition='top center', marker=dict(size=15, color='#17a2b8'))
    
    st.plotly_chart(fig_9box, use_container_width=True)
    
    st.info("💡 **Guía de acción:** Los candidatos ubicados en el cuadrante superior derecho (Alto Desempeño / Alto Potencial) deberían iniciar su recorrido directamente en el Tramo 3 o 4. Quienes posean alto potencial pero desempeño medio, ingresan al Tramo 1 para fortalecer bases operativas.")
