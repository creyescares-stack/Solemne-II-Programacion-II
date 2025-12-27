"""
Script de Generación de Datos Financieros
Autor: Sistema de Análisis Financiero
Fecha: 2024-01-15

Este script genera datos financieros sintéticos para análisis.
Incluye datos de ventas, clientes, productos y transacciones.
"""

import json
import random
from datetime import datetime, timedelta

# Configuración de semilla para reproducibilidad
random.seed(42)

# Datos de ejemplo
productos = [
    {"id": 1, "nombre": "Laptop Pro", "categoria": "Electrónica", "precio": 1299},
    {"id": 2, "nombre": "Mouse Inalámbrico", "categoria": "Electrónica", "precio": 45},
    {"id": 3, "nombre": "Monitor 27\"", "categoria": "Electrónica", "precio": 399},
    {"id": 4, "nombre": "Teclado Mecánico", "categoria": "Electrónica", "precio": 129},
    {"id": 5, "nombre": "Webcam HD", "categoria": "Electrónica", "precio": 89},
    {"id": 6, "nombre": "Camisa Business", "categoria": "Ropa", "precio": 59},
    {"id": 7, "nombre": "Pantalón Formal", "categoria": "Ropa", "precio": 79},
    {"id": 8, "nombre": "Lámpara LED", "categoria": "Hogar", "precio": 45},
    {"id": 9, "nombre": "Cojines Decorativos", "categoria": "Hogar", "precio": 29},
    {"id": 10, "nombre": "Pelota de Fútbol", "categoria": "Deportes", "precio": 35},
]

clientes = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez",
    "Luis Rodríguez", "Sofia Torres", "Diego Ramírez", "Carmen Silva",
    "Roberto Fernández", "Laura González"
]

def generar_transacciones(num_transacciones=100):
    """Genera transacciones sintéticas de ventas"""
    transacciones = []
    fecha_inicio = datetime.now() - timedelta(days=90)
    
    for i in range(num_transacciones):
        producto = random.choice(productos)
        cliente = random.choice(clientes)
        fecha = fecha_inicio + timedelta(days=random.randint(0, 90))
        cantidad = random.randint(1, 5)
        descuento = random.choice([0, 0.05, 0.10, 0.15])
        
        monto_base = producto["precio"] * cantidad
        monto_final = monto_base * (1 - descuento)
        
        transaccion = {
            "id": f"TXN{str(i+1).zfill(4)}",
            "fecha": fecha.strftime("%Y-%m-%d"),
            "hora": fecha.strftime("%H:%M:%S"),
            "cliente": cliente,
            "producto_id": producto["id"],
            "producto_nombre": producto["nombre"],
            "categoria": producto["categoria"],
            "cantidad": cantidad,
            "precio_unitario": producto["precio"],
            "descuento": descuento,
            "monto_total": round(monto_final, 2),
            "estado": random.choices(
                ["Completado", "Pendiente", "Cancelado"],
                weights=[0.85, 0.10, 0.05]
            )[0]
        }
        transacciones.append(transaccion)
    
    return transacciones

def generar_metricas_mensuales():
    """Genera métricas agregadas por mes"""
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    metricas = []
    base_revenue = 45000
    
    for i, mes in enumerate(meses[:8]):  # Últimos 8 meses
        # Tendencia de crecimiento con variación
        factor_crecimiento = 1 + (i * 0.05) + random.uniform(-0.1, 0.15)
        revenue = base_revenue * factor_crecimiento
        
        expenses = revenue * random.uniform(0.65, 0.75)
        profit = revenue - expenses
        
        metrica = {
            "mes": mes,
            "mes_num": i + 1,
            "ingresos": round(revenue, 2),
            "gastos": round(expenses, 2),
            "ganancias": round(profit, 2),
            "margen_ganancia": round((profit / revenue) * 100, 2)
        }
        metricas.append(metrica)
    
    return metricas

def main():
    print("🚀 Generando datos financieros...")
    
    # Generar datos
    transacciones = generar_transacciones(100)
    metricas = generar_metricas_mensuales()
    
    # Guardar a archivos JSON
    with open('scripts/transacciones.json', 'w', encoding='utf-8') as f:
        json.dump(transacciones, f, ensure_ascii=False, indent=2)
    
    with open('scripts/metricas_mensuales.json', 'w', encoding='utf-8') as f:
        json.dump(metricas, f, ensure_ascii=False, indent=2)
    
    with open('scripts/productos.json', 'w', encoding='utf-8') as f:
        json.dump(productos, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Generadas {len(transacciones)} transacciones")
    print(f"✅ Generadas {len(metricas)} métricas mensuales")
    print(f"✅ Catálogo de {len(productos)} productos")
    
    # Estadísticas básicas
    total_ventas = sum(t["monto_total"] for t in transacciones if t["estado"] == "Completado")
    print(f"\n📊 Total de ventas completadas: ${total_ventas:,.2f}")
    
    return {
        "transacciones": len(transacciones),
        "metricas": len(metricas),
        "productos": len(productos),
        "total_ventas": total_ventas
    }

if __name__ == "__main__":
    resultado = main()
