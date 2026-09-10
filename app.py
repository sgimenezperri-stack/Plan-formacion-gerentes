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
        st.write("**Ubicación:** Salta y Jujuy[cite: 5]")
        st.write("**Responsabilidad económica:** P&L integral de la marca[cite: 5]")
        st.info("Liderar integralmente el negocio, garantizando resultados económicos, maximizando rentabilidad y desarrollando equipos ágiles.[cite: 5]")
        
        st.subheader("Competencias Clave")
        competencias = [
            "Visión integral de negocio[cite: 5]", 
            "Orientación a resultados y rentabilidad[cite: 5]", 
            "Capacidad analítica y comprensión financiera[cite: 5]", 
            "Liderazgo de líderes[cite: 5]", 
            "Toma de decisiones[cite: 5]", 
            "Gestión transversal[cite: 5]"
        ]
        for comp in competencias:
            st.markdown(f"- {comp}")
            
    with col2:
        st.subheader("Principales Responsabilidades")
        with st.expander("Gestión Integral y P&L"):
            st.write("Responsable del P&L, gestionar drivers de ingresos/costos y gestionar gastos controlables.[cite: 5]")
        with st.expander("Gestión Comercial y Posventa"):
            st.write("Cumplimiento de market share, definición de listas de precios y objetivos de rentabilidad en Posventa.[cite: 5]")
        with st.expander("Personas y Liderazgo"):
            st.write("Desarrollar al equipo gerencial e identificar posiciones críticas y sucesores.[cite: 5]")
            
        st.subheader("Indicadores de Gestión (KPIs)")
        st.write("- **Rentabilidad:** Resultado económico y cumplimiento de presupuesto.[cite: 5]")
        st.write("- **Comercial:** Market share y rotación de stock.[cite: 5]")

# ==========================================
# DIMENSIÓN 2: LA RUTA (PLAN DE CARRERA)
# ==========================================
elif dimension == "2. Avance en La Ruta":
    st.header("🗺️ Dimensión 2: Progreso y Estructura de La Ruta")
    st.markdown("Visualización gráfica del recorrido de los colaboradores a través de los 4 Tramos hacia la Gerencia de Marca.[cite: 5]")
    
    # 1. CONSTRUCCIÓN DEL MAPA VISUAL DE LA RUTA
    st.subheader("Mapa de Posicionamiento de Talentos")
    
    # Coordenadas para simular un camino serpenteante
    ruta_x = list(range(1, 15)) # Paradas 1 a 14
    ruta_y = [2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3] # Efecto zigzag del camino
    paradas_nombres = [f"Parada {i}" for i in range(1, 15)]
    
    # Datos simulados de los colaboradores en su parada actual 
    colaboradores = [
        {"nombre": "Carmelo", "parada": 2, "color": "#ff9999"},
        {"nombre": "Alejandro", "parada": 5, "color": "#66b3ff"},
        {"nombre": "Melisa", "parada": 9, "color": "#99ff99"}
    ]
    
    fig_ruta = go.Figure()
    
    # Dibujar la línea del camino
    fig_ruta.add_trace(go.Scatter(
        x=ruta_x, y=ruta_y, mode='lines+markers+text',
        line=dict(color='lightgray', width=4, dash='dot'),
        marker=dict(size=20, color='white', line=dict(color='gray', width=2)),
        text=paradas_nombres, textposition="top center",
        name="Ruta de Formación", hoverinfo='text'
    ))
    
    # Posicionar a los colaboradores en el mapa
    for colab in colaboradores:
        idx = colab["parada"] - 1 # Índice en la lista (0 a 13)
        fig_ruta.add_trace(go.Scatter(
            x=[ruta_x[idx]], y=[ruta_y[idx]], mode='markers+text',
            marker=dict(size=25, color=colab["color"], symbol='star'),
            text=[colab["nombre"]], textposition="bottom center",
            name=colab["nombre"],
            hovertext=f"{colab['nombre']} está en la Parada {colab['parada']}"
        ))
        
    fig_ruta.update_layout(
        xaxis=dict(showgrid=False, zeroline=False, visible=False),
        yaxis=dict(showgrid=False, zeroline=False, visible=False),
        plot_bgcolor='white', height=400, showlegend=False,
        margin=dict(l=20, r=20, t=30, b=20)
    )
    
    st.plotly_chart(fig_ruta, use_container_width=True)

    # 2. DETALLE ESPECÍFICO DEL PROGRAMA DE FORMACIÓN
    st.subheader("Estructura Detallada del Programa")
    
    t1, t2, t3, t4 = st.tabs([
        "Tramo 1: Fundamentos", 
        "Tramo 2: Comercial", 
        "Tramo 3: Sinergia", 
        "Tramo 4: Estrategia"
    ])
    
    with t1:
        st.markdown("### TRAMO 1: Fundamentos Analíticos y Operativos[cite: 5]")
        with st.expander("Parada 1: Capacidad analítica y financiera (3 semanas)[cite: 5]"):
            st.write("- **Teoría:** Estructura de P&L, drivers. Capacitación en cuentas de resultados y estados financieros.[cite: 5]")
            st.write("- **Práctica:** Acompañar en el cierre mensual.[cite: 5]")
            st.write("- **Hito:** Identificar desvío real en P&L y presentar acción correctiva.[cite: 5]")
            st.write("- **Instructor:** Gonzalo Rodriguez[cite: 5]")
        with st.expander("Parada 2: Disciplina de gestión por indicadores (2 semanas)[cite: 5]"):
            st.write("- **Teoría:** Diseño de KPIs, control de gestión.[cite: 5]")
            st.write("- **Práctica:** Seguimiento de métricas (rotación, inventario).[cite: 5]")
            st.write("- **Hito:** Diseñar/automatizar tablero de control de resultados.[cite: 5]")
        with st.expander("Parada 3: Adaptabilidad y mejora continua (2 semanas)[cite: 5]"):
            st.write("- **Teoría:** Metodologías de mejora (ej. DMAIC).[cite: 5]")
            st.write("- **Práctica:** Recorrer operaciones (Salta/Jujuy) detectando oportunidades.[cite: 5]")
            st.write("- **Hito:** Plan estructurado para optimizar cuello de botella operativo.[cite: 5]")

    with t2:
        st.markdown("### TRAMO 2: Tracción Comercial y Mercado[cite: 5]")
        with st.expander("Parada 4: Orientación comercial y al cliente (2 semanas)[cite: 5]"):
            st.write("- **Teoría:** CX y programas de excelencias.[cite: 5]")
            st.write("- **Práctica:** Análisis de satisfacción y Planes de Ahorro.[cite: 5]")
            st.write("- **Hito:** Plan de acción ante desvío en indicadores de calidad.[cite: 5]")
        with st.expander("Parada 5: Capacidad de negociación (2 semanas)[cite: 5]"):
            st.write("- **Teoría:** Técnicas y políticas comerciales.[cite: 5]")
            st.write("- **Práctica:** Definición de descuentos por modelo.[cite: 5]")
            st.write("- **Hito:** Role-play de negociación complejo.[cite: 5]")
        with st.expander("Parada 6: Comunicación e influencia (1 semana)[cite: 5]"):
            st.write("- **Teoría:** Storytelling con datos.[cite: 5]")
            st.write("- **Práctica:** Observar fundamentación de decisiones operativas.[cite: 5]")
            st.write("- **Hito:** Presentar resultados logrando respaldo de la Dirección.[cite: 5]")
        with st.expander("Parada 7: Relaciones institucionales (2 semanas)[cite: 5]"):
            st.write("- **Teoría:** Eventos y reuniones con las marcas.[cite: 5]")
            st.write("- **Práctica:** Asistencia a reuniones con la marca.[cite: 5]")
            st.write("- **Hito:** Liderar actividad de benchmarking con la red.[cite: 5]")

    with t3:
        st.markdown("### TRAMO 3: Sinergia Organizacional y Liderazgo[cite: 5]")
        with st.expander("Parada 8: Liderazgo de líderes (2 semanas)[cite: 5]"):
            st.write("- **Teoría:** Gestión del desempeño.[cite: 5]")
            st.write("- **Práctica:** Presenciar fijación de objetivos (tableros).[cite: 5]")
            st.write("- **Hito:** Revisar tableros y realizar propuestas de mejoras.[cite: 5]")
        with st.expander("Parada 9: Desarrollo de equipos (2 semanas)[cite: 5]"):
            st.write("- **Teoría:** Mapeo de talento y headcount.[cite: 5]")
            st.write("- **Práctica:** Identificar posiciones críticas.[cite: 5]")
            st.write("- **Hito:** Plan de sucesión para dos posiciones clave.[cite: 5]")
        with st.expander("Parada 10: Gestión transversal (3 semanas)[cite: 5]"):
            st.write("- **Teoría:** Resolución de conflictos.[cite: 5]")
            st.write("- **Práctica:** Alinear acciones entre 3+ gerencias.[cite: 5]")
            st.write("- **Hito:** Liderar proyecto corto de mejora interárea.[cite: 5]")

    with t4:
        st.markdown("### TRAMO 4: Recta Final - Visión Estratégica[cite: 5]")
        with st.expander("Parada 11: Visión integral de negocio (2 semanas)[cite: 5]"):
            st.write("- **Teoría:** Dinámica del sector.[cite: 5]")
            st.write("- **Práctica:** Análisis integral frente a competencia.[cite: 5]")
            st.write("- **Hito:** Diagnóstico estratégico (Comercial, Posventa, Planes).[cite: 5]")
        with st.expander("Parada 12: Planificación y ejecución (3 semanas)[cite: 5]"):
            st.write("- **Teoría:** Gestión de proyectos.[cite: 5]")
            st.write("- **Práctica:** Planificación de compras 0km.[cite: 5]")
            st.write("- **Hito:** Fundamentar Plan de Negocios anual.[cite: 5]")
        with st.expander("Parada 13: Orientación a resultados (2 semanas)[cite: 5]"):
            st.write("- **Teoría:** Evaluación de proyectos (ROI).[cite: 5]")
            st.write("- **Práctica:** Identificar necesidades de inversión.[cite: 5]")
            st.write("- **Hito:** Propuesta de CAPEX justificando impacto.[cite: 5]")
        with st.expander("Parada 14: Toma de decisiones (1 semana)[cite: 5]"):
            st.write("- **Teoría:** Decisiones bajo presión.[cite: 5]")
            st.write("- **Práctica:** Asignación de gastos y listas de precios.[cite: 5]")
            st.write("- **Hito:** Caso integrador: acciones sobre P&L y mercado.[cite: 5]")

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
    
    # NOTA: Al integrar datos reales (ej. ventas comerciales) a esta matriz o cualquier cálculo de promedio, 
    # asegúrate de filtrar con df.dropna() para ignorar las celdas vacías y no tratarlas como ceros.
    
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
