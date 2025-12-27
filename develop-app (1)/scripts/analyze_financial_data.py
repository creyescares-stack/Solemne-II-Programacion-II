"""
Script de Análisis de Datos Financieros
Autor: Sistema de Análisis Financiero
Fecha: 2024-01-15

Este script realiza análisis estadístico sobre los datos financieros.
Calcula KPIs, tendencias y genera insights de negocio.
"""

import json
import statistics
from collections import defaultdict

def cargar_datos():
    """Carga los datos generados"""
    try:
        with open('scripts/transacciones.json', 'r', encoding='utf-8') as f:
            transacciones = json.load(f)
        
        with open('scripts/metricas_mensuales.json', 'r', encoding='utf-8') as f:
            metricas = json.load(f)
        
        with open('scripts/productos.json', 'r', encoding='utf-8') as f:
            productos = json.load(f)
        
        return transacciones, metricas, productos
    except FileNotFoundError:
        print("⚠️  Archivos de datos no encontrados. Ejecuta primero generate_financial_data.py")
        return [], [], []

def analizar_ventas_por_categoria(transacciones):
    """Analiza ventas agrupadas por categoría"""
    ventas_por_categoria = defaultdict(lambda: {"monto": 0, "cantidad": 0})
    
    for t in transacciones:
        if t["estado"] == "Completado":
            cat = t["categoria"]
            ventas_por_categoria[cat]["monto"] += t["monto_total"]
            ventas_por_categoria[cat]["cantidad"] += t["cantidad"]
    
    # Ordenar por monto
    resultado = sorted(
        [{"categoria": k, **v} for k, v in ventas_por_categoria.items()],
        key=lambda x: x["monto"],
        reverse=True
    )
    
    return resultado

def calcular_kpis(transacciones, metricas):
    """Calcula indicadores clave de rendimiento"""
    # Filtrar transacciones completadas
    completadas = [t for t in transacciones if t["estado"] == "Completado"]
    
    # KPIs básicos
    total_ventas = sum(t["monto_total"] for t in completadas)
    num_transacciones = len(completadas)
    ticket_promedio = total_ventas / num_transacciones if num_transacciones > 0 else 0
    
    # Análisis de descuentos
    descuentos_aplicados = [t["descuento"] for t in completadas if t["descuento"] > 0]
    descuento_promedio = statistics.mean(descuentos_aplicados) if descuentos_aplicados else 0
    
    # Clientes únicos
    clientes_unicos = len(set(t["cliente"] for t in completadas))
    
    # Valor promedio por cliente
    valor_por_cliente = total_ventas / clientes_unicos if clientes_unicos > 0 else 0
    
    # Tendencia de crecimiento (últimos meses)
    if len(metricas) >= 2:
        ingreso_inicial = metricas[0]["ingresos"]
        ingreso_final = metricas[-1]["ingresos"]
        crecimiento = ((ingreso_final - ingreso_inicial) / ingreso_inicial) * 100
    else:
        crecimiento = 0
    
    return {
        "total_ventas": round(total_ventas, 2),
        "num_transacciones": num_transacciones,
        "ticket_promedio": round(ticket_promedio, 2),
        "descuento_promedio": round(descuento_promedio * 100, 2),
        "clientes_unicos": clientes_unicos,
        "valor_por_cliente": round(valor_por_cliente, 2),
        "tasa_crecimiento": round(crecimiento, 2)
    }

def analizar_productos_top(transacciones, top_n=5):
    """Identifica los productos más vendidos"""
    ventas_por_producto = defaultdict(lambda: {"ventas": 0, "cantidad": 0, "nombre": ""})
    
    for t in transacciones:
        if t["estado"] == "Completado":
            pid = t["producto_id"]
            ventas_por_producto[pid]["ventas"] += t["monto_total"]
            ventas_por_producto[pid]["cantidad"] += t["cantidad"]
            ventas_por_producto[pid]["nombre"] = t["producto_nombre"]
    
    # Ordenar y tomar top N
    productos_ordenados = sorted(
        ventas_por_producto.items(),
        key=lambda x: x[1]["ventas"],
        reverse=True
    )[:top_n]
    
    return [
        {
            "producto_id": pid,
            "nombre": datos["nombre"],
            "ventas_totales": round(datos["ventas"], 2),
            "unidades_vendidas": datos["cantidad"]
        }
        for pid, datos in productos_ordenados
    ]

def analizar_tendencias_temporales(transacciones):
    """Analiza patrones temporales en las ventas"""
    from datetime import datetime
    
    ventas_por_dia = defaultdict(float)
    
    for t in transacciones:
        if t["estado"] == "Completado":
            fecha = datetime.strptime(t["fecha"], "%Y-%m-%d")
            dia_semana = fecha.strftime("%A")
            ventas_por_dia[dia_semana] += t["monto_total"]
    
    return dict(ventas_por_dia)

def main():
    print("📊 Iniciando análisis de datos financieros...\n")
    
    # Cargar datos
    transacciones, metricas, productos = cargar_datos()
    
    if not transacciones:
        return
    
    # Análisis 1: KPIs principales
    print("=" * 60)
    print("📈 INDICADORES CLAVE DE RENDIMIENTO (KPIs)")
    print("=" * 60)
    kpis = calcular_kpis(transacciones, metricas)
    for key, value in kpis.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    # Análisis 2: Ventas por categoría
    print("\n" + "=" * 60)
    print("🏷️  VENTAS POR CATEGORÍA")
    print("=" * 60)
    ventas_categoria = analizar_ventas_por_categoria(transacciones)
    for item in ventas_categoria:
        print(f"{item['categoria']}: ${item['monto']:,.2f} ({item['cantidad']} unidades)")
    
    # Análisis 3: Productos top
    print("\n" + "=" * 60)
    print("⭐ TOP 5 PRODUCTOS MÁS VENDIDOS")
    print("=" * 60)
    productos_top = analizar_productos_top(transacciones)
    for i, prod in enumerate(productos_top, 1):
        print(f"{i}. {prod['nombre']}: ${prod['ventas_totales']:,.2f} ({prod['unidades_vendidas']} unidades)")
    
    # Análisis 4: Tendencias temporales
    print("\n" + "=" * 60)
    print("📅 VENTAS POR DÍA DE LA SEMANA")
    print("=" * 60)
    tendencias = analizar_tendencias_temporales(transacciones)
    for dia, monto in sorted(tendencias.items(), key=lambda x: x[1], reverse=True):
        print(f"{dia}: ${monto:,.2f}")
    
    # Guardar resultados del análisis
    resultados = {
        "kpis": kpis,
        "ventas_por_categoria": ventas_categoria,
        "productos_top": productos_top,
        "tendencias_temporales": tendencias
    }
    
    with open('scripts/analisis_resultados.json', 'w', encoding='utf-8') as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)
    
    print("\n✅ Análisis completado. Resultados guardados en analisis_resultados.json")

if __name__ == "__main__":
    main()
