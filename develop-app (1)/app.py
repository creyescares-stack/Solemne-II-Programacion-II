"""
Dashboard de Empleabilidad en Chile
Aplicación web interactiva con Streamlit
"""

import streamlit as st
import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os

# Configuración de la página
st.set_page_config(
    page_title="Dashboard Empleabilidad Chile",
    page_icon="🇨🇱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilos CSS personalizados
st.markdown("""
<style>
    .main {
        background-color: #0a0a0a;
    }
    .stMetric {
        background-color: #1a1a1a;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #2a2a2a;
    }
    .stMetric label {
        color: #a0a0a0;
        font-size: 14px;
    }
    .stMetric [data-testid="stMetricValue"] {
        font-size: 28px;
        color: #ffffff;
    }
    h1, h2, h3 {
        color: #ffffff;
    }
    .css-1d391kg {
        background-color: #1a1a1a;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def cargar_datos():
    """Carga todos los datos necesarios, generándolos si no existen"""
    import os
    
    # Verificar si los archivos existen, si no, generarlos
    archivos_necesarios = [
        'scripts/estadisticas_mensuales.json',
        'scripts/datos_sectores.json',
        'scripts/ofertas_laborales.json',
        'scripts/datos_historicos.json'
    ]
    
    archivos_faltantes = [f for f in archivos_necesarios if not os.path.exists(f)]
    
    if archivos_faltantes:
        st.info("⏳ Generando datos del mercado laboral...")
        # Importar y ejecutar el script de generación
        from scripts.generate_employment_data import main as generar_datos
        generar_datos()
        st.success("✅ Datos generados correctamente")
    
    try:
        with open('scripts/estadisticas_mensuales.json', 'r', encoding='utf-8') as f:
            estadisticas = json.load(f)
        
        with open('scripts/datos_sectores.json', 'r', encoding='utf-8') as f:
            sectores = json.load(f)
        
        with open('scripts/ofertas_laborales.json', 'r', encoding='utf-8') as f:
            ofertas = json.load(f)
        
        with open('scripts/datos_historicos.json', 'r', encoding='utf-8') as f:
            historicos = json.load(f)
        
        return estadisticas, sectores, ofertas, historicos
    except FileNotFoundError as e:
        st.error(f"⚠️ Error al cargar datos: {e}")
        st.info("Por favor, verifica que el directorio 'scripts' existe.")
        st.stop()

def mostrar_header():
    """Muestra el encabezado del dashboard"""
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.title("🇨🇱 Dashboard de Empleabilidad en Chile")
        st.markdown("*Análisis del mercado laboral y estadísticas de empleo*")
    
    with col2:
        st.markdown(f"**Última actualización:** {datetime.now().strftime('%d/%m/%Y')}")
        if st.button("📊 Exportar Datos", use_container_width=True):
            st.info("Función de exportación disponible próximamente")

def mostrar_metricas(estadisticas, sectores):
    """Muestra las métricas principales"""
    ultima_estadistica = estadisticas[-1]
    penultima_estadistica = estadisticas[-2] if len(estadisticas) > 1 else estadisticas[-1]
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        cambio_desempleo = ultima_estadistica["tasa_desempleo"] - penultima_estadistica["tasa_desempleo"]
        st.metric(
            label="Tasa de Desempleo",
            value=f"{ultima_estadistica['tasa_desempleo']}%",
            delta=f"{cambio_desempleo:.1f}%",
            delta_color="inverse"
        )
    
    with col2:
        cambio_sueldo = ultima_estadistica["sueldo_promedio"] - penultima_estadistica["sueldo_promedio"]
        st.metric(
            label="Sueldo Promedio",
            value=f"${ultima_estadistica['sueldo_promedio']:,}",
            delta=f"${cambio_sueldo:,}"
        )
    
    with col3:
        total_ofertas = sum(s["ofertas_activas"] for s in sectores)
        st.metric(
            label="Ofertas Activas",
            value=f"{total_ofertas:,}",
            delta="+12.5%"
        )
    
    with col4:
        st.metric(
            label="Empleos Creados (Mes)",
            value=f"{ultima_estadistica['empleos_creados']:,}",
            delta="+8.2%"
        )

def mostrar_tendencias_historicas(historicos):
    """Muestra gráfico de tendencias de 10 años"""
    st.subheader("📈 Tendencias Históricas del Mercado Laboral (2015-2024)")
    
    df = pd.DataFrame(historicos)
    
    # Crear gráfico con tres ejes
    fig = go.Figure()
    
    # Línea de desempleo
    fig.add_trace(go.Scatter(
        x=df['year'],
        y=df['tasa_desempleo'],
        name='Tasa de Desempleo (%)',
        line=dict(color='#ef4444', width=3),
        mode='lines+markers'
    ))
    
    # Línea de empleo total (escala secundaria)
    fig.add_trace(go.Scatter(
        x=df['year'],
        y=df['empleo_total'],
        name='Empleo Total',
        line=dict(color='#22c55e', width=3),
        mode='lines+markers',
        yaxis='y2'
    ))
    
    # Línea de ofertas publicadas (escala terciaria)
    fig.add_trace(go.Scatter(
        x=df['year'],
        y=df['ofertas_publicadas'],
        name='Ofertas Publicadas',
        line=dict(color='#3b82f6', width=3),
        mode='lines+markers',
        yaxis='y3'
    ))
    
    fig.update_layout(
        height=500,
        hovermode='x unified',
        plot_bgcolor='#1a1a1a',
        paper_bgcolor='#1a1a1a',
        font=dict(color='#ffffff'),
        xaxis=dict(
            title='Año',
            gridcolor='#2a2a2a',
            showgrid=True
        ),
        yaxis=dict(
            title='Tasa de Desempleo (%)',
            titlefont=dict(color='#ef4444'),
            tickfont=dict(color='#ef4444'),
            gridcolor='#2a2a2a'
        ),
        yaxis2=dict(
            title='Empleo Total',
            titlefont=dict(color='#22c55e'),
            tickfont=dict(color='#22c55e'),
            overlaying='y',
            side='right'
        ),
        yaxis3=dict(
            title='Ofertas Publicadas',
            titlefont=dict(color='#3b82f6'),
            tickfont=dict(color='#3b82f6'),
            overlaying='y',
            side='right',
            position=0.95
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Métricas resumidas
    col1, col2, col3 = st.columns(3)
    with col1:
        promedio_desempleo = sum(h['tasa_desempleo'] for h in historicos) / len(historicos)
        st.metric("Desempleo Promedio (10 años)", f"{promedio_desempleo:.1f}%")
    with col2:
        crecimiento_empleo = ((historicos[-1]['empleo_total'] - historicos[0]['empleo_total']) / historicos[0]['empleo_total']) * 100
        st.metric("Crecimiento del Empleo", f"{crecimiento_empleo:+.1f}%")
    with col3:
        total_ofertas = sum(h['ofertas_publicadas'] for h in historicos)
        st.metric("Ofertas Acumuladas", f"{total_ofertas:,}")

def mostrar_graficos(estadisticas, sectores):
    """Muestra los gráficos principales"""
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💼 Tendencias Mensuales")
        df_est = pd.DataFrame(estadisticas)
        
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(
            x=df_est['mes'], y=df_est['empleos_creados'],
            name='Empleos Creados',
            line=dict(color='#22c55e', width=3),
            fill='tonexty'
        ))
        fig1.add_trace(go.Scatter(
            x=df_est['mes'], y=df_est['tasa_desempleo'] * 3000,
            name='Tasa Desempleo (x3000)',
            line=dict(color='#ef4444', width=3)
        ))
        
        fig1.update_layout(
            height=400,
            plot_bgcolor='#1a1a1a',
            paper_bgcolor='#1a1a1a',
            font=dict(color='#ffffff'),
            xaxis=dict(gridcolor='#2a2a2a'),
            yaxis=dict(gridcolor='#2a2a2a'),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        st.subheader("🏢 Empleos por Sector")
        df_sec = pd.DataFrame(sectores).sort_values('empleos_totales', ascending=True)
        
        fig2 = go.Figure(go.Bar(
            x=df_sec['empleos_totales'],
            y=df_sec['sector'],
            orientation='h',
            marker=dict(
                color=df_sec['empleos_totales'],
                colorscale='Blues',
                showscale=False
            ),
            text=df_sec['empleos_totales'].apply(lambda x: f'{x:,}'),
            textposition='outside'
        ))
        
        fig2.update_layout(
            height=400,
            plot_bgcolor='#1a1a1a',
            paper_bgcolor='#1a1a1a',
            font=dict(color='#ffffff'),
            xaxis=dict(title='Número de Empleos', gridcolor='#2a2a2a'),
            yaxis=dict(title='', gridcolor='#2a2a2a')
        )
        
        st.plotly_chart(fig2, use_container_width=True)

def mostrar_tabla_ofertas(ofertas):
    """Muestra tabla de ofertas laborales"""
    st.subheader("💼 Ofertas Laborales Recientes")
    
    # Filtrar solo ofertas activas
    ofertas_activas = [o for o in ofertas if o["estado"] == "Activa"][:15]
    
    df = pd.DataFrame(ofertas_activas)
    df['sueldo'] = df['sueldo'].apply(lambda x: f"${x:,}")
    
    # Seleccionar y renombrar columnas
    df_display = df[['fecha', 'empresa', 'cargo', 'sector', 'sueldo', 'region']].copy()
    df_display.columns = ['Fecha', 'Empresa', 'Cargo', 'Sector', 'Sueldo', 'Región']
    
    st.dataframe(
        df_display,
        use_container_width=True,
        height=400,
        hide_index=True
    )

def main():
    """Función principal de la aplicación"""
    # Cargar datos
    estadisticas, sectores, ofertas, historicos = cargar_datos()
    
    # Mostrar componentes
    mostrar_header()
    st.divider()
    
    mostrar_metricas(estadisticas, sectores)
    st.divider()
    
    mostrar_tendencias_historicas(historicos)
    st.divider()
    
    mostrar_graficos(estadisticas, sectores)
    st.divider()
    
    mostrar_tabla_ofertas(ofertas)
    
    # Footer
    st.divider()
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 20px;'>
        <p>Dashboard de Empleabilidad en Chile | Datos generados con fines educativos</p>
        <p>Desarrollado con Python & Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
