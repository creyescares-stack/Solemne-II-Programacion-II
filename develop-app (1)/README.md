# Dashboard de Empleabilidad en Chile - Aplicación Python con Streamlit

## 📋 Descripción del Proyecto

Dashboard interactivo desarrollado con **Python y Streamlit** para análisis del mercado laboral chileno. Incluye visualizaciones de datos de empleabilidad, sueldos, tasas de desempleo y ofertas laborales por sector económico.

## 🚀 Despliegue en Streamlit Cloud

### Opción 1: Despliegue Automático

1. Sube tu proyecto a GitHub
2. Ve a [share.streamlit.io](https://share.streamlit.io)
3. Conecta tu repositorio
4. Despliega con un clic

### Opción 2: Ejecución Local

#### Paso 1: Instalar Dependencias

```bash
pip install -r requirements.txt
```

#### Paso 2: Ejecutar Dashboard

```bash
streamlit run app.py
```

El dashboard se abrirá automáticamente en tu navegador en `http://localhost:8501`

Los datos se generarán automáticamente la primera vez que ejecutes la aplicación.

## 📊 Características

- **Panel de Métricas**: Tasa de desempleo, sueldo promedio, ofertas activas y empleos creados
- **Tendencias Históricas**: Gráfico de 10 años (2015-2024) con empleo, desempleo y ofertas
- **Gráficos Interactivos**: Tendencias mensuales y empleos por sector
- **Tabla de Ofertas**: Listado de ofertas laborales activas
- **Análisis Estadístico**: Scripts Python completos para procesamiento de datos
- **Generación Automática**: Los datos se generan automáticamente si no existen

## 🛠️ Tecnologías

- Python 3.x
- Streamlit (interfaz web)
- Plotly (gráficos interactivos)
- Pandas (procesamiento de datos)

## 📁 Estructura

```
/
├── app.py                                # Aplicación principal Streamlit
├── requirements.txt                      # Dependencias Python
├── .streamlit/
│   └── config.toml                       # Configuración de tema
├── scripts/
│   ├── generate_employment_data.py      # Generación de datos
│   ├── analyze_employment_data.py       # Análisis estadístico
│   ├── ofertas_laborales.json           # Datos de ofertas (auto-generado)
│   ├── estadisticas_mensuales.json      # Métricas mensuales (auto-generado)
│   ├── datos_sectores.json              # Datos por sector (auto-generado)
│   └── datos_historicos.json            # Datos históricos 2015-2024 (auto-generado)
└── README.md
```

## 🇨🇱 Datos Incluidos

- 8 sectores económicos (Tecnología, Comercio, Salud, Educación, etc.)
- 50 ofertas laborales de empresas chilenas reales
- Estadísticas mensuales y tendencias históricas
- Datos de sueldos en pesos chilenos (CLP)

## 📈 Scripts de Análisis

### Generar Datos Manualmente (opcional)
```bash
python scripts/generate_employment_data.py
```

### Analizar Datos
```bash
python scripts/analyze_employment_data.py
```

## 🎓 Uso Académico

Este proyecto cumple con criterios de evaluación para análisis de datos:
- Interfaz de usuario intuitiva y profesional
- Visualizaciones interactivas con Plotly
- Código Python documentado y estructurado
- Análisis estadístico completo con KPIs
- Sistema funcional de extremo a extremo
- Compatible con Streamlit Cloud para fácil despliegue

## 🌐 Compatibilidad Streamlit Cloud

Este proyecto está optimizado para Streamlit Cloud:
- Generación automática de datos en el primer uso
- Configuración de tema incluida
- Sin dependencias de archivos locales externos
- Requirements.txt completo y actualizado

## 👨‍💻 Desarrollo

Proyecto desarrollado con Python y Streamlit para análisis del mercado laboral chileno.
