"use client"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Line, LineChart, XAxis, YAxis, CartesianGrid, Legend, ResponsiveContainer, Tooltip } from "recharts"

const historicalData = [
  { year: 2015, desempleo: 6.4, empleo: 7850000, ofertas: 45000 },
  { year: 2016, desempleo: 6.7, empleo: 7920000, ofertas: 47000 },
  { year: 2017, desempleo: 7.1, empleo: 8050000, ofertas: 51000 },
  { year: 2018, desempleo: 7.3, empleo: 8180000, ofertas: 55000 },
  { year: 2019, desempleo: 7.2, empleo: 8320000, ofertas: 58000 },
  { year: 2020, desempleo: 10.8, empleo: 7950000, ofertas: 32000 },
  { year: 2021, desempleo: 9.4, empleo: 8150000, ofertas: 42000 },
  { year: 2022, desempleo: 8.6, empleo: 8480000, ofertas: 65000 },
  { year: 2023, desempleo: 8.2, empleo: 8720000, ofertas: 72000 },
  { year: 2024, desempleo: 8.7, empleo: 8850000, ofertas: 78000 },
]

export default function HistoricalTrends() {
  return (
    <Card className="lg:col-span-2">
      <CardHeader>
        <CardTitle>Evolución Histórica del Mercado Laboral (2015-2024)</CardTitle>
        <CardDescription>
          Análisis de 10 años de datos: Tasa de desempleo, niveles de empleo total y ofertas laborales publicadas
        </CardDescription>
      </CardHeader>
      <CardContent>
        <div className="h-96">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={historicalData} margin={{ top: 5, right: 30, bottom: 5, left: 0 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--border))" opacity={0.3} />
              <XAxis
                dataKey="year"
                stroke="hsl(var(--muted-foreground))"
                fontSize={12}
                label={{ value: "Año", position: "insideBottom", offset: -5 }}
              />
              <YAxis
                yAxisId="left"
                stroke="hsl(var(--muted-foreground))"
                fontSize={12}
                tickFormatter={(value) => `${value}%`}
                label={{ value: "Desempleo %", angle: -90, position: "insideLeft" }}
              />
              <YAxis
                yAxisId="right"
                orientation="right"
                stroke="hsl(var(--muted-foreground))"
                fontSize={12}
                tickFormatter={(value) => `${(value / 1000000).toFixed(1)}M`}
                label={{ value: "Empleos (Millones)", angle: 90, position: "insideRight" }}
              />
              <Tooltip
                contentStyle={{
                  backgroundColor: "hsl(var(--card))",
                  border: "1px solid hsl(var(--border))",
                  borderRadius: "8px",
                  color: "hsl(var(--foreground))",
                }}
                formatter={(value: number, name: string) => {
                  if (name === "Tasa de Desempleo") return [`${value}%`, name]
                  if (name === "Empleo Total") return [value.toLocaleString(), name]
                  if (name === "Ofertas Publicadas") return [value.toLocaleString(), name]
                  return [value, name]
                }}
              />
              <Legend />
              <Line
                yAxisId="left"
                type="monotone"
                dataKey="desempleo"
                stroke="hsl(var(--chart-3))"
                strokeWidth={3}
                name="Tasa de Desempleo"
                dot={{ fill: "hsl(var(--chart-3))", r: 5 }}
                activeDot={{ r: 7 }}
              />
              <Line
                yAxisId="right"
                type="monotone"
                dataKey="empleo"
                stroke="hsl(var(--chart-1))"
                strokeWidth={3}
                name="Empleo Total"
                dot={{ fill: "hsl(var(--chart-1))", r: 5 }}
                activeDot={{ r: 7 }}
              />
              <Line
                yAxisId="right"
                type="monotone"
                dataKey="ofertas"
                stroke="hsl(var(--chart-2))"
                strokeWidth={3}
                name="Ofertas Publicadas"
                dot={{ fill: "hsl(var(--chart-2))", r: 5 }}
                activeDot={{ r: 7 }}
              />
            </LineChart>
          </ResponsiveContainer>
        </div>

        <div className="mt-6 grid gap-4 sm:grid-cols-3">
          <div className="rounded-lg border bg-card p-4">
            <div className="text-sm text-muted-foreground">Desempleo Promedio</div>
            <div className="text-2xl font-bold">8.1%</div>
            <div className="text-xs text-muted-foreground mt-1">Últimos 10 años</div>
          </div>
          <div className="rounded-lg border bg-card p-4">
            <div className="text-sm text-muted-foreground">Crecimiento Empleo</div>
            <div className="text-2xl font-bold text-green-600">+12.7%</div>
            <div className="text-xs text-muted-foreground mt-1">Desde 2015</div>
          </div>
          <div className="rounded-lg border bg-card p-4">
            <div className="text-sm text-muted-foreground">Ofertas Totales</div>
            <div className="text-2xl font-bold">545K</div>
            <div className="text-xs text-muted-foreground mt-1">Acumuladas 2015-2024</div>
          </div>
        </div>
      </CardContent>
    </Card>
  )
}
