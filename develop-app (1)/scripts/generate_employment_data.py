"""
Script de Generación de Datos de Empleabilidad en Chile
Autor: Sistema de Análisis de Mercado Laboral
Fecha: 2024-01-15

Este script genera datos sintéticos sobre el mercado laboral chileno.
Incluye datos de empleo por sector, sueldos, tasas de desempleo y ofertas laborales.
"""

import json
import random
from datetime import datetime, timedelta
import os

# Configuración de semilla para reproducibilidad
random.seed(42)

# Datos de sectores económicos en Chile
sectores = [
    {"nombre": "Tecnología", "empleos_base": 145000, "sueldo_promedio": 1650000},
    {"nombre": "Comercio", "empleos_base": 320000, "sueldo_promedio": 650000},
    {"nombre": "Salud", "empleos_base": 187000, "sueldo_promedio": 1100000},
    {"nombre": "Educación", "empleos_base": 210000, "sueldo_promedio": 950000},
    {"nombre": "Construcción", "empleos_base": 154000, "sueldo_promedio": 780000},
    {"nombre": "Minería", "empleos_base": 98000, "sueldo_promedio": 2100000},
    {"nombre": "Finanzas", "empleos_base": 125000, "sueldo_promedio": 1450000},
    {"nombre": "Transporte", "empleos_base": 176000, "sueldo_promedio": 720000},
]

# Empresas chilenas representativas
empresas = [
    "Falabella", "Banco de Chile", "Codelco", "Ripley", "Hospital Clínico UC",
    "Universidad de Chile", "Movistar Chile", "Constructora Salfa", "CMPC",
    "Entel", "Cencosud", "BCI", "Latam Airlines", "Arauco", "AES Gener"
]

# Cargos típicos por sector
cargos_por_sector = {
    "Tecnología": ["Desarrollador Full Stack", "Data Scientist", "DevOps Engineer", "UX Designer"],
    "Comercio": ["Gerente de Ventas", "Supervisor de Tienda", "Vendedor Especializado"],
    "Salud": ["Enfermero/a Especializado", "Médico General", "Técnico Paramédico"],
    "Educación": ["Profesor de Ingeniería", "Coordinador Académico", "Docente de Matemáticas"],
    "Construcción": ["Arquitecto de Proyectos", "Ingeniero Civil", "Jefe de Obra"],
    "Minería": ["Ingeniero de Minas", "Geólogo", "Supervisor de Operaciones"],
    "Finanzas": ["Analista de Datos", "Contador Auditor", "Asesor Financiero"],
    "Transporte": ["Coordinador Logístico", "Operador de Flota", "Supervisor de Rutas"],
}

def generar_ofertas_laborales(num_ofertas=50):
    """Genera ofertas laborales sintéticas del mercado chileno"""
    ofertas = []
    fecha_inicio = datetime.now() - timedelta(days=30)
    
    for i in range(num_ofertas):
        sector = random.choice(sectores)
        empresa = random.choice(empresas)
        cargo = random.choice(cargos_por_sector.get(sector["nombre"], ["Profesional"]))
        fecha = fecha_inicio + timedelta(days=random.randint(0, 30))
        
        # Sueldo con variación
        sueldo_base = sector["sueldo_promedio"]
        variacion = random.uniform(0.7, 1.4)
        sueldo = int(sueldo_base * variacion)
        
        oferta = {
            "id": f"EMP{str(i+1).zfill(4)}",
            "fecha": fecha.strftime("%Y-%m-%d"),
            "empresa": empresa,
            "cargo": cargo,
            "sector": sector["nombre"],
            "sueldo": sueldo,
            "region": random.choice(["Metropolitana", "Valparaíso", "Biobío", "Antofagasta"]),
            "tipo_contrato": random.choice(["Indefinido", "Plazo Fijo", "Por Proyecto"]),
            "jornada": random.choice(["Completa", "Part-Time", "Flexible"]),
            "estado": random.choices(
                ["Activa", "En Revisión", "Cerrada"],
                weights=[0.70, 0.20, 0.10]
            )[0]
        }
        ofertas.append(oferta)
    
    return ofertas

def generar_estadisticas_mensuales():
    """Genera estadísticas del mercado laboral por mes"""
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    estadisticas = []
    tasa_desempleo_base = 9.2
    
    for i, mes in enumerate(meses[:8]):  # Últimos 8 meses
        # Tendencia decreciente del desempleo con pequeñas variaciones
        tasa_desempleo = max(8.0, tasa_desempleo_base - (i * 0.08) + random.uniform(-0.2, 0.2))
        
        # Empleos creados con tendencia creciente
        empleos_creados = int(32000 + (i * 1600) + random.randint(-2000, 3000))
        
        # Sueldo promedio con tendencia creciente
        sueldo_promedio = int(680000 + (i * 5000) + random.randint(-5000, 10000))
        
        # Tasa de participación laboral
        tasa_participacion = round(60.5 + random.uniform(-0.5, 1.0), 2)
        
        estadistica = {
            "mes": mes,
            "mes_num": i + 1,
            "tasa_desempleo": round(tasa_desempleo, 1),
            "empleos_creados": empleos_creados,
            "sueldo_promedio": sueldo_promedio,
            "tasa_participacion": tasa_participacion,
            "trabajadores_activos": int(9200000 + (i * 15000))
        }
        estadisticas.append(estadistica)
    
    return estadisticas

def generar_datos_por_sector():
    """Genera datos detallados por sector económico"""
    datos_sectores = []
    
    for sector in sectores:
        # Variación en el empleo
        variacion_empleo = random.uniform(0.95, 1.08)
        empleos_actuales = int(sector["empleos_base"] * variacion_empleo)
        
        # Crecimiento anual
        crecimiento = round(random.uniform(-2.0, 15.0), 1)
        
        dato = {
            "sector": sector["nombre"],
            "empleos_totales": empleos_actuales,
            "sueldo_promedio": sector["sueldo_promedio"],
            "crecimiento_anual": crecimiento,
            "ofertas_activas": random.randint(150, 800),
            "tasa_rotacion": round(random.uniform(8.0, 25.0), 1)
        }
        datos_sectores.append(dato)
    
    return datos_sectores

def generar_datos_historicos():
    """Genera datos históricos del mercado laboral chileno (2015-2024)"""
    datos_historicos = []
    
    # Datos base año 2015
    empleo_base = 7850000
    desempleo_base = 6.4
    ofertas_base = 45000
    
    for year in range(2015, 2025):
        # Simular impacto COVID en 2020
        if year == 2020:
            factor_crisis = 0.92
            desempleo_year = 10.8
            ofertas_year = 32000
        else:
            factor_crisis = 1.0
            # Tendencia general con variaciones
            crecimiento = (year - 2015) * 0.015 * factor_crisis
            empleo_year = int(empleo_base * (1 + crecimiento + random.uniform(-0.01, 0.02)))
            
            # Desempleo con tendencia y variación
            if year < 2020:
                desempleo_year = round(desempleo_base + (year - 2015) * 0.15 + random.uniform(-0.2, 0.3), 1)
            else:
                # Recuperación post-pandemia
                desempleo_year = round(10.8 - (year - 2020) * 0.35 + random.uniform(-0.2, 0.2), 1)
            
            # Ofertas laborales con crecimiento
            ofertas_year = int(ofertas_base * (1 + (year - 2015) * 0.08 + random.uniform(-0.05, 0.1)))
        
        dato = {
            "year": year,
            "empleo_total": empleo_year if year != 2020 else int(empleo_base * factor_crisis),
            "tasa_desempleo": desempleo_year,
            "ofertas_publicadas": ofertas_year,
            "pib_variacion": round(random.uniform(-1.0, 4.5) if year != 2020 else -5.8, 1),
            "salario_real_variacion": round(random.uniform(-0.5, 2.5), 1)
        }
        datos_historicos.append(dato)
    
    return datos_historicos

def main():
    print("🇨🇱 Generando datos de empleabilidad en Chile...")
    
    os.makedirs('scripts', exist_ok=True)
    
    # Generar datos
    ofertas = generar_ofertas_laborales(50)
    estadisticas = generar_estadisticas_mensuales()
    datos_sectores = generar_datos_por_sector()
    datos_historicos = generar_datos_historicos()
    
    # Guardar a archivos JSON
    with open('scripts/ofertas_laborales.json', 'w', encoding='utf-8') as f:
        json.dump(ofertas, f, ensure_ascii=False, indent=2)
    
    with open('scripts/estadisticas_mensuales.json', 'w', encoding='utf-8') as f:
        json.dump(estadisticas, f, ensure_ascii=False, indent=2)
    
    with open('scripts/datos_sectores.json', 'w', encoding='utf-8') as f:
        json.dump(datos_sectores, f, ensure_ascii=False, indent=2)
    
    with open('scripts/datos_historicos.json', 'w', encoding='utf-8') as f:
        json.dump(datos_historicos, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Generadas {len(ofertas)} ofertas laborales")
    print(f"✅ Generadas {len(estadisticas)} estadísticas mensuales")
    print(f"✅ Datos de {len(datos_sectores)} sectores económicos")
    print(f"✅ Datos históricos de {len(datos_historicos)} años (2015-2024)")
    
    # Estadísticas básicas
    ofertas_activas = sum(1 for o in ofertas if o["estado"] == "Activa")
    sueldo_promedio_global = sum(s["sueldo_promedio"] for s in datos_sectores) / len(datos_sectores)
    
    print(f"\n📊 Ofertas activas: {ofertas_activas}")
    print(f"💰 Sueldo promedio nacional: ${sueldo_promedio_global:,.0f}")
    print(f"📈 Tasa de desempleo actual: {estadisticas[-1]['tasa_desempleo']}%")
    
    return {
        "ofertas": len(ofertas),
        "estadisticas": len(estadisticas),
        "sectores": len(datos_sectores),
        "ofertas_activas": ofertas_activas
    }

if __name__ == "__main__":
    resultado = main()
