"""
Script de Análisis de Datos de Empleabilidad
Autor: Sistema de Análisis de Mercado Laboral
Fecha: 2024-01-15

Este script analiza los datos generados del mercado laboral chileno.
Calcula KPIs, tendencias y proporciona insights estadísticos.
"""

import json
import statistics

def cargar_datos():
    """Carga los datos generados previamente"""
    try:
        with open('scripts/ofertas_laborales.json', 'r', encoding='utf-8') as f:
            ofertas = json.load(f)
        
        with open('scripts/estadisticas_mensuales.json', 'r', encoding='utf-8') as f:
            estadisticas = json.load(f)
        
        with open('scripts/datos_sectores.json', 'r', encoding='utf-8') as f:
            sectores = json.load(f)
        
        return ofertas, estadisticas, sectores
    except FileNotFoundError:
        print("❌ Error: Primero ejecuta generate_employment_data.py")
        return None, None, None

def analizar_ofertas(ofertas):
    """Analiza las ofertas laborales"""
    print("\n" + "="*60)
    print("📋 ANÁLISIS DE OFERTAS LABORALES")
    print("="*60)
    
    total_ofertas = len(ofertas)
    ofertas_activas = [o for o in ofertas if o["estado"] == "Activa"]
    
    # Estadísticas de sueldos
    sueldos = [o["sueldo"] for o in ofertas]
    sueldo_promedio = statistics.mean(sueldos)
    sueldo_mediano = statistics.median(sueldos)
    sueldo_min = min(sueldos)
    sueldo_max = max(sueldos)
    
    print(f"\n📊 Resumen General:")
    print(f"   • Total de ofertas: {total_ofertas}")
    print(f"   • Ofertas activas: {len(ofertas_activas)} ({len(ofertas_activas)/total_ofertas*100:.1f}%)")
    
    print(f"\n💰 Análisis Salarial:")
    print(f"   • Sueldo promedio: ${sueldo_promedio:,.0f}")
    print(f"   • Sueldo mediano: ${sueldo_mediano:,.0f}")
    print(f"   • Rango salarial: ${sueldo_min:,.0f} - ${sueldo_max:,.0f}")
    
    # Ofertas por sector
    ofertas_por_sector = {}
    for oferta in ofertas:
        sector = oferta["sector"]
        ofertas_por_sector[sector] = ofertas_por_sector.get(sector, 0) + 1
    
    print(f"\n🏢 Ofertas por Sector:")
    for sector, count in sorted(ofertas_por_sector.items(), key=lambda x: x[1], reverse=True):
        print(f"   • {sector}: {count} ofertas")
    
    return {
        "total": total_ofertas,
        "activas": len(ofertas_activas),
        "sueldo_promedio": sueldo_promedio,
        "ofertas_por_sector": ofertas_por_sector
    }

def analizar_tendencias(estadisticas):
    """Analiza tendencias del mercado laboral"""
    print("\n" + "="*60)
    print("📈 ANÁLISIS DE TENDENCIAS DEL MERCADO LABORAL")
    print("="*60)
    
    # Tendencia de desempleo
    tasas_desempleo = [e["tasa_desempleo"] for e in estadisticas]
    cambio_desempleo = tasas_desempleo[-1] - tasas_desempleo[0]
    
    # Tendencia de empleos creados
    empleos_totales = sum(e["empleos_creados"] for e in estadisticas)
    promedio_empleos = empleos_totales / len(estadisticas)
    
    # Tendencia salarial
    sueldos = [e["sueldo_promedio"] for e in estadisticas]
    crecimiento_salarial = ((sueldos[-1] - sueldos[0]) / sueldos[0]) * 100
    
    print(f"\n📉 Tasa de Desempleo:")
    print(f"   • Inicial: {tasas_desempleo[0]}%")
    print(f"   • Actual: {tasas_desempleo[-1]}%")
    print(f"   • Cambio: {cambio_desempleo:+.1f}% ({'+' if cambio_desempleo < 0 else '-'} es mejor)")
    
    print(f"\n💼 Creación de Empleos:")
    print(f"   • Total empleos creados: {empleos_totales:,}")
    print(f"   • Promedio mensual: {promedio_empleos:,.0f}")
    print(f"   • Mejor mes: {max(estadisticas, key=lambda x: x['empleos_creados'])['mes']}")
    
    print(f"\n💵 Evolución Salarial:")
    print(f"   • Sueldo inicial: ${sueldos[0]:,}")
    print(f"   • Sueldo actual: ${sueldos[-1]:,}")
    print(f"   • Crecimiento: {crecimiento_salarial:+.1f}%")
    
    return {
        "cambio_desempleo": cambio_desempleo,
        "empleos_totales": empleos_totales,
        "crecimiento_salarial": crecimiento_salarial
    }

def analizar_sectores(sectores):
    """Analiza datos por sector económico"""
    print("\n" + "="*60)
    print("🏭 ANÁLISIS POR SECTOR ECONÓMICO")
    print("="*60)
    
    # Sector con más empleos
    sector_mayor_empleo = max(sectores, key=lambda x: x["empleos_totales"])
    
    # Sector con mejor sueldo
    sector_mejor_sueldo = max(sectores, key=lambda x: x["sueldo_promedio"])
    
    # Sector con mayor crecimiento
    sector_mayor_crecimiento = max(sectores, key=lambda x: x["crecimiento_anual"])
    
    print(f"\n🥇 Destacados:")
    print(f"   • Mayor empleador: {sector_mayor_empleo['sector']} ({sector_mayor_empleo['empleos_totales']:,} empleos)")
    print(f"   • Mejores sueldos: {sector_mejor_sueldo['sector']} (${sector_mejor_sueldo['sueldo_promedio']:,})")
    print(f"   • Mayor crecimiento: {sector_mayor_crecimiento['sector']} ({sector_mayor_crecimiento['crecimiento_anual']:+.1f}%)")
    
    print(f"\n📊 Resumen por Sector:")
    for sector in sorted(sectores, key=lambda x: x["empleos_totales"], reverse=True):
        print(f"\n   {sector['sector']}:")
        print(f"      • Empleos: {sector['empleos_totales']:,}")
        print(f"      • Sueldo promedio: ${sector['sueldo_promedio']:,}")
        print(f"      • Crecimiento anual: {sector['crecimiento_anual']:+.1f}%")
        print(f"      • Ofertas activas: {sector['ofertas_activas']}")
    
    return {
        "sector_mayor_empleo": sector_mayor_empleo["sector"],
        "sector_mejor_sueldo": sector_mejor_sueldo["sector"],
        "sector_mayor_crecimiento": sector_mayor_crecimiento["sector"]
    }

def generar_reporte_ejecutivo(ofertas_analisis, tendencias, sectores_analisis):
    """Genera un reporte ejecutivo consolidado"""
    print("\n" + "="*60)
    print("📄 REPORTE EJECUTIVO - MERCADO LABORAL CHILENO")
    print("="*60)
    
    print(f"\n🎯 KPIs Principales:")
    print(f"   • Ofertas laborales totales: {ofertas_analisis['total']}")
    print(f"   • Tasa de activación: {ofertas_analisis['activas']/ofertas_analisis['total']*100:.1f}%")
    print(f"   • Sueldo promedio ofertado: ${ofertas_analisis['sueldo_promedio']:,.0f}")
    print(f"   • Empleos creados (período): {tendencias['empleos_totales']:,}")
    print(f"   • Variación desempleo: {tendencias['cambio_desempleo']:+.1f}%")
    print(f"   • Crecimiento salarial: {tendencias['crecimiento_salarial']:+.1f}%")
    
    print(f"\n✨ Insights Clave:")
    print(f"   1. El sector {sectores_analisis['sector_mayor_empleo']} lidera en número de empleos")
    print(f"   2. {sectores_analisis['sector_mejor_sueldo']} ofrece los mejores sueldos promedio")
    print(f"   3. {sectores_analisis['sector_mayor_crecimiento']} muestra el mayor dinamismo")
    
    if tendencias['cambio_desempleo'] < 0:
        print(f"   4. ✅ La tasa de desempleo ha disminuido (señal positiva)")
    else:
        print(f"   4. ⚠️ La tasa de desempleo ha aumentado (requiere atención)")
    
    if tendencias['crecimiento_salarial'] > 0:
        print(f"   5. ✅ Los sueldos han crecido en el período analizado")
    else:
        print(f"   5. ⚠️ Los sueldos han decrecido o se mantienen estancados")

def main():
    print("🔍 Iniciando análisis del mercado laboral chileno...")
    
    # Cargar datos
    ofertas, estadisticas, sectores = cargar_datos()
    
    if ofertas is None:
        return
    
    # Realizar análisis
    ofertas_analisis = analizar_ofertas(ofertas)
    tendencias = analizar_tendencias(estadisticas)
    sectores_analisis = analizar_sectores(sectores)
    
    # Generar reporte ejecutivo
    generar_reporte_ejecutivo(ofertas_analisis, tendencias, sectores_analisis)
    
    print("\n" + "="*60)
    print("✅ Análisis completado exitosamente")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
