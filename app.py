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
    .stTabs [data-baseweb="tab-list"] { gap: 20px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: #e9ecef; border-radius: 5px 5px 0 0; padding: 10px 20px; }
    .stTabs [aria-selected="true"] { background-color: #003366; color: white; }
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
    st.markdown("Detalle integral de responsabilidades, estructura y competencias requeridas para liderar el negocio.")
    
    # Uso de pestañas para organizar la información de forma dinámica
    tab_adn, tab_resp, tab_aut, tab_kpi, tab_comp = st.tabs([
        "Misión y Estructura", 
        "Responsabilidades", 
        "Nivel de Autoridad", 
        "KPIs de Gestión", 
        "Competencias Clave"
    ])
    
    with tab_adn:
        st.subheader("Misión y Alcance")
        st.write("**Ubicación:** Salta y Jujuy | **Reporta a:** Gerente General | **Alcance:** Gestión integral del negocio")
        st.write("**Responsabilidad económica:** P&L integral de la marca")
        st.info("""
        - Liderar integralmente el negocio, garantizando resultados económicos y financieros.
        - Maximizar la rentabilidad y eficiencia desarrollando equipos de alto desempeño.
        - Anticiparse a los cambios del mercado, impulsando acciones de competitividad.
        """)
        
        st.subheader("Ubicación en la Estructura")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Reportes Directos:**")
            st.markdown("- Gerente Comercial\n- Gerente de Posventa\n- Jefe/a de Administración\n- Jefa de Planes de Ahorro\n- Responsable de Calidad")
        with col2:
            st.markdown("**Relaciones Funcionales:**")
            st.markdown("- Director de Administración y Finanzas\n- Directora de Recursos Humanos\n- Director Controller\n- Áreas corporativas del Grupo")
            
        st.success("**Definición de Éxito:** Lograr que la marca alcance de manera sostenible sus objetivos de rentabilidad, market share, volumen comercial, Posventa, Planes de Ahorro y calidad, desarrollando una estructura sólida.")

    with tab_resp:
        st.subheader("Principales Responsabilidades")
        col_r1, col_r2 = st.columns(2)
        
        with col_r1:
            with st.expander("Gestión Integral y P&L"):
                st.write("- Ser responsable integral del P&L, comprendiendo drivers de ingresos, márgenes y costos.")
                st.write("- Analizar rentabilidad y detectar desvíos.")
                st.write("- Gestionar los gastos controlables de la marca.")
            with st.expander("Plan de Negocios"):
                st.write("- Liderar elaboración del Plan de Negocios y presentarlo ante la Dirección y la marca.")
                st.write("- Transformar objetivos anuales en planes concretos para cada gerencia.")
            with st.expander("Gestión Comercial"):
                st.write("- Cumplimiento de volumen y market share.")
                st.write("- Definir estrategia, mix, listas de precios, descuentos y acciones comerciales por modelo.")
            with st.expander("Stock y Compra 0 km"):
                st.write("- Planificación de compras coordinada con Finanzas (capital de trabajo).")
                st.write("- Equilibrar disponibilidad comercial, rotación y costo financiero.")
            with st.expander("Posventa"):
                st.write("- Responsable de objetivos económicos y operativos (facturación, rentabilidad, productividad, absorción).")
                
        with col_r2:
            with st.expander("Planes de Ahorro"):
                st.write("- Desempeño integral, calidad de cartera, adjudicaciones, entregas y rentabilidad.")
                st.write("- Coordinar entre Planes, Comercial y Administración.")
            with st.expander("Calidad y Experiencia del Cliente"):
                st.write("- Responsable final de los indicadores de calidad de la marca.")
                st.write("- Liderar planes de acción ante desvíos y promover cultura orientada al cliente.")
            with st.expander("Personas y Liderazgo"):
                st.write("- Liderar, evaluar y desarrollar al equipo gerencial.")
                st.write("- Identificar posiciones críticas, sucesores y trabajar planes de desarrollo con RRHH.")
            with st.expander("Relación con Marcas y Benchmarking"):
                st.write("- Principal interlocutor frente a la marca. Representación en convenciones.")
                st.write("- Benchmarking con otros concesionarios e identificación de mejores prácticas.")
            with st.expander("Inversiones y CAPEX"):
                st.write("- Identificar necesidades de inversión.")
                st.write("- Desarrollar propuestas de CAPEX justificando retorno, sujeto a aprobación financiera.")

    with tab_aut:
        st.subheader("Niveles de Autoridad y Autonomía")
        col_a1, col_a2 = st.columns(2)
        with col_a1:
            st.markdown("✅ **Puede decidir directamente:**")
            st.markdown("""
            - Asignación de gastos controlables (dentro de objetivo).
            - Estrategia comercial y acciones por modelo.
            - Descuentos comerciales y listas de precios (respetando lineamientos).
            - Distribución de objetivos en sus equipos.
            - Acciones correctivas sobre las unidades de negocio.
            """)
        with col_a2:
            st.markdown("⚠️ **Propone y requiere aprobación:**")
            st.markdown("""
            - **CAPEX e inversiones:** Director de Administración y Finanzas.
            - **Altas, bajas y cambios de estructura:** Dirección de RRHH.
            - **Planes de sucesión y desarrollo:** En conjunto con Dirección de RRHH.
            - **Plan de Negocios:** Instancias internas y de la marca.
            """)

    with tab_kpi:
        st.subheader("Indicadores Clave de Gestión (KPIs)")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.info("**Rentabilidad**\n- Resultado económico\n- Rentabilidad s/ facturación\n- Cumplimiento presupuesto\n- Gastos vs. objetivo")
            st.info("**Comercial**\n- Market share\n- Volumen de ventas\n- Rotación y días de stock")
        with c2:
            st.info("**Posventa**\n- Facturación y rentabilidad\n- Absorción de costos fijos\n- Cumplimiento objetivos")
            st.info("**Planes de Ahorro**\n- Volumen de ventas\n- Calidad de cartera")
        with c3:
            st.info("**Calidad**\n- Satisfacción del cliente\n- Cumplimiento de estándares")
            st.info("**Personas**\n- Evaluación de equipos\n- Cobertura posiciones críticas\n- Desarrollo sucesores")

    with tab_comp:
        st.subheader("Competencias Clave Requeridas")
        competencias = [
            "Visión integral de negocio", "Orientación a resultados y rentabilidad",
            "Capacidad analítica y comprensión financiera", "Liderazgo de líderes",
            "Desarrollo de equipos y sucesores", "Capacidad de planificación y ejecución",
            "Orientación comercial y al cliente", "Capacidad de negociación",
            "Toma de decisiones", "Gestión transversal", "Comunicación e influencia",
            "Capacidad para construir relaciones institucionales", "Disciplina de seguimiento y gestión (KPIs)",
            "Adaptabilidad y mejora continua"
        ]
        # Mostrar en dos columnas para mayor legibilidad
        col_c1, col_c2 = st.columns(2)
        for i, comp in enumerate(competencias):
            if i % 2 == 0:
                col_c1.markdown(f"- {comp}")
            else:
                col_c2.markdown(f"- {comp}")

# ==========================================
# DIMENSIÓN 2: LA RUTA (PLAN DE CARRERA)
# ==========================================
elif dimension == "2. Avance en La Ruta":
    st.header("🗺️ Dimensión 2: Progreso y Estructura de La Ruta")
    st.markdown("Visualización gráfica del recorrido de los colaboradores a través de los 4 Tramos hacia la Gerencia de Marca.")
    
    st.subheader("Mapa de Posicionamiento de Talentos")
    ruta_x = list(range(1, 15))
    ruta_y = [2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]
    paradas_nombres = [f"Parada {i}" for i in range(1, 15)]
    
    colaboradores = [
        {"nombre": "Carmelo", "parada": 2, "color": "#ff9999"},
        {"nombre": "Alejandro", "parada": 5, "color": "#66b3ff"},
        {"nombre": "Melisa", "parada": 9, "color": "#99ff99"},
        {"nombre": "Gonzalo", "parada": 12, "color": "#ffcc99"}
    ]
    
    fig_ruta = go.Figure()
    
    fig_ruta.add_trace(go.Scatter(
        x=ruta_x, y=ruta_y, mode='lines+markers+text',
        line=dict(color='lightgray', width=4, dash='dot'),
        marker=dict(size=20, color='white', line=dict(color='gray', width=2)),
        text=paradas_nombres, textposition="top center",
        name="Ruta de Formación", hoverinfo='text'
    ))
    
    for colab in colaboradores:
        idx = colab["parada"] - 1
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

    st.subheader("Estructura Detallada del Programa")
    
    t1, t2, t3, t4 = st.tabs([
        "Tramo 1: Fundamentos", 
        "Tramo 2: Comercial", 
        "Tramo 3: Sinergia", 
        "Tramo 4: Estrategia"
    ])
    
    with t1:
        st.markdown("### TRAMO 1: Fundamentos Analíticos y Operativos")
        with st.expander("Parada 1: Capacidad analítica y financiera (3 semanas)"):
            st.write("- **Teoría:** Estructura de P&L, drivers. Capacitación en cuentas de resultados y estados financieros.")
            st.write("- **Práctica:** Acompañar en el cierre mensual.")
            st.write("- **Hito:** Identificar desvío real en P&L y presentar acción correctiva.")
            st.write("- **Instructor:** Gonzalo Rodriguez")
        with st.expander("Parada 2: Disciplina de gestión por indicadores (2 semanas)"):
            st.write("- **Teoría:** Diseño de KPIs, control de gestión.")
            st.write("- **Práctica:** Seguimiento de métricas (rotación, inventario).")
            st.write("- **Hito:** Diseñar/automatizar tablero de control de resultados.")
        with st.expander("Parada 3: Adaptabilidad y mejora continua (2 semanas)"):
            st.write("- **Teoría:** Metodologías de mejora (ej. DMAIC).")
            st.write("- **Práctica:** Recorrer operaciones (Salta/Jujuy) detectando oportunidades.")
            st.write("- **Hito:** Plan estructurado para optimizar cuello de botella operativo.")

    with t2:
        st.markdown("### TRAMO 2: Tracción Comercial y Mercado")
        with st.expander("Parada 4: Orientación comercial y al cliente (2 semanas)"):
            st.write("- **Teoría:** CX y programas de excelencias.")
            st.write("- **Práctica:** Análisis de satisfacción y Planes de Ahorro.")
            st.write("- **Hito:** Plan de acción ante desvío en indicadores de calidad.")
        with st.expander("Parada 5: Capacidad de negociación (2 semanas)"):
            st.write("- **Teoría:** Técnicas y políticas comerciales.")
            st.write("- **Práctica:** Definición de descuentos por modelo.")
            st.write("- **Hito:** Role-play de negociación complejo.")
        with st.expander("Parada 6: Comunicación e influencia (1 semana)"):
            st.write("- **Teoría:** Storytelling con datos.")
            st.write("- **Práctica:** Observar fundamentación de decisiones operativas.")
            st.write("- **Hito:** Presentar resultados logrando respaldo de la Dirección.")
        with st.expander("Parada 7: Relaciones institucionales (2 semanas)"):
            st.write("- **Teoría:** Eventos y reuniones con las marcas.")
            st.write("- **Práctica:** Asistencia a reuniones con la marca.")
            st.write("- **Hito:** Liderar actividad de benchmarking con la red.")

    with t3:
        st.markdown("### TRAMO 3: Sinergia Organizacional y Liderazgo")
        with st.expander("Parada 8: Liderazgo de líderes (2 semanas)"):
            st.write("- **Teoría:** Gestión del desempeño.")
            st.write("- **Práctica:** Presenciar fijación de objetivos (tableros).")
            st.write("- **Hito:** Revisar tableros y realizar propuestas de mejoras.")
        with st.expander("Parada 9: Desarrollo de equipos (2 semanas)"):
            st.write("- **Teoría:** Mapeo de talento y headcount.")
            st.write("- **Práctica:** Identificar posiciones críticas.")
            st.write("- **Hito:** Plan de sucesión para dos posiciones clave.")
        with st.expander("Parada 10: Gestión transversal (3 semanas)"):
            st.write("- **Teoría:** Resolución de conflictos.")
            st.write("- **Práctica:** Alinear acciones entre 3+ gerencias.")
            st.write("- **Hito:** Liderar proyecto corto de mejora interárea.")

    with t4:
        st.markdown("### TRAMO 4: Recta Final - Visión Estratégica")
        with st.expander("Parada 11: Visión integral de negocio (2 semanas)"):
            st.write("- **Teoría:** Dinámica del sector.")
            st.write("- **Práctica:** Análisis integral frente a competencia.")
            st.write("- **Hito:** Diagnóstico estratégico (Comercial, Posventa, Planes).")
        with st.expander("Parada 12: Planificación y ejecución (3 semanas)"):
            st.write("- **Teoría:** Gestión de proyectos.")
            st.write("- **Práctica:** Planificación de compras 0km.")
            st.write("- **Hito:** Fundamentar Plan de Negocios anual.")
        with st.expander("Parada 13: Orientación a resultados (2 semanas)"):
            st.write("- **Teoría:** Evaluación de proyectos (ROI).")
            st.write("- **Práctica:** Identificar necesidades de inversión.")
            st.write("- **Hito:** Propuesta de CAPEX justificando impacto.")
        with st.expander("Parada 14: Toma de decisiones (1 semana)"):
            st.write("- **Teoría:** Decisiones bajo presión.")
            st.write("- **Práctica:** Asignación de gastos y listas de precios.")
            st.write("- **Hito:** Caso integrador: acciones sobre P&L y mercado.")

# ==========================================
# DIMENSIÓN 3: EVALUACIÓN DE POTENCIAL
# ==========================================
elif dimension == "3. Evaluación de Potencial":
    st.header("Dimensión 3: Matriz de Talento (9-Box)")
    st.markdown("Clasificación de candidatos pre-ingreso a La Ruta según su desempeño histórico y potencial de liderazgo.")
    
    data_9box = {
        "Colaborador": ["Alejandro", "Melisa", "Carmelo", "Gonzalo", "Nuevo Candidato"],
        "Desempeño": [3, 4, 2, 5, 3.5], 
        "Potencial": [4, 5, 3, 4, 2]    
    }
    df_9box = pd.DataFrame(data_9box)
    
    fig_9box = px.scatter(df_9box, x="Desempeño", y="Potencial", text="Colaborador",
                          title="Matriz de Evaluación de Reemplazos",
                          range_x=[1, 5], range_y=[1, 5])
    
    fig_9box.add_hline(y=2.5, line_width=1, line_dash="dash", line_color="gray")
    fig_9box.add_hline(y=3.5, line_width=1, line_dash="dash", line_color="gray")
    fig_9box.add_vline(x=2.5, line_width=1, line_dash="dash", line_color="gray")
    fig_9box.add_vline(x=3.5, line_width=1, line_dash="dash", line_color="gray")
    
    fig_9box.update_traces(textposition='top center', marker=dict(size=15, color='#17a2b8'))
    
    st.plotly_chart(fig_9box, use_container_width=True)
    
    st.info("💡 **Guía de acción:** Los candidatos ubicados en el cuadrante superior derecho (Alto Desempeño / Alto Potencial) deberían iniciar su recorrido directamente en el Tramo 3 o 4. Quienes posean alto potencial pero desempeño medio, ingresan al Tramo 1 para fortalecer bases operativas.")
