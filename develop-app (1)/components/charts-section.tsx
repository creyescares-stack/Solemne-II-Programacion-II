"use client"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import {
  Line,
  Bar,
  BarChart,
  LineChart,
  XAxis,
  YAxis,
  CartesianGrid,
  Legend,
  ResponsiveContainer,
  Tooltip,
} from "recharts"

const employmentData = [
  { month: "Ene", desempleo: 9.2, empleosCreados: 32000, sueldoPromedio: 680 },
  { month: "Feb", desempleo: 9.0, empleosCreados: 35000, sueldoPromedio: 685 },
  { month: "Mar", desempleo: 8.9, empleosCreados: 38000, sueldoPromedio: 690 },
  { month: "Abr", desempleo: 8.8, empleosCreados: 41000, sueldoPromedio: 695 },
  { month: "May", desempleo: 8.7, empleosCreados: 43000, sueldoPromedio: 705 },
  { month: "Jun", desempleo: 8.5, empleosCreados: 45000, sueldoPromedio: 710 },
  { month: "Jul", desempleo: 8.6, empleosCreados: 44000, sueldoPromedio: 715 },
  { month: "Ago", desempleo: 8.7, empleosCreados: 45230, sueldoPromedio: 720 },
]

const sectorData = [
  { sector: "Tecnología", empleos: 145000 },
  { sector: "Comercio", empleos: 320000 },
  { sector: "Salud", empleos: 187000 },
  { sector: "Educación", empleos: 210000 },
  { sector: "Construcción", empleos: 154000 },
  { sector: "Minería", empleos: 98000 },
]

export default function ChartsSection() {
  return (
    <div className="grid gap-6 lg:grid-cols-2">
      <Card>
        <CardHeader>
          <CardTitle>Tendencias del Mercado Laboral</CardTitle>
          <CardDescription>Evolución mensual de tasa de desempleo y empleos creados</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="h-80">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={employmentData} margin={{ top: 5, right: 20, bottom: 5, left: 0 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--border))" opacity={0.3} />
                <XAxis dataKey="month" stroke="hsl(var(--muted-foreground))" fontSize={12} />
                <YAxis
                  yAxisId="left"
                  stroke="hsl(var(--muted-foreground))"
                  fontSize={12}
                  tickFormatter={(value) => `${value}%`}
                />
                <YAxis
                  yAxisId="right"
                  orientation="right"
                  stroke="hsl(var(--muted-foreground))"
                  fontSize={12}
                  tickFormatter={(value) => `${(value / 1000).toFixed(0)}k`}
                />
                <Tooltip
                  contentStyle={{
                    backgroundColor: "hsl(var(--card))",
                    border: "1px solid hsl(var(--border))",
                    borderRadius: "8px",
                    color: "hsl(var(--foreground))",
                  }}
                  formatter={(value: number, name: string) => {
                    if (name === "Tasa Desempleo") return `${value}%`
                    if (name === "Empleos Creados") return value.toLocaleString()
                    return value
                  }}
                />
                <Legend />
                <Line
                  yAxisId="left"
                  type="monotone"
                  dataKey="desempleo"
                  stroke="hsl(var(--chart-3))"
                  strokeWidth={2}
                  name="Tasa Desempleo"
                  dot={{ fill: "hsl(var(--chart-3))", r: 4 }}
                  activeDot={{ r: 6 }}
                />
                <Line
                  yAxisId="right"
                  type="monotone"
                  dataKey="empleosCreados"
                  stroke="hsl(var(--chart-1))"
                  strokeWidth={2}
                  name="Empleos Creados"
                  dot={{ fill: "hsl(var(--chart-1))", r: 4 }}
                  activeDot={{ r: 6 }}
                />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle>Empleos por Sector Económico</CardTitle>
          <CardDescription>Distribución de empleados por sector en Chile</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="h-80">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={sectorData} margin={{ top: 5, right: 20, bottom: 5, left: 0 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--border))" opacity={0.3} />
                <XAxis
                  dataKey="sector"
                  stroke="hsl(var(--muted-foreground))"
                  fontSize={12}
                  angle={-45}
                  textAnchor="end"
                  height={80}
                />
                <YAxis
                  stroke="hsl(var(--muted-foreground))"
                  fontSize={12}
                  tickFormatter={(value) => `${(value / 1000).toFixed(0)}k`}
                />
                <Tooltip
                  contentStyle={{
                    backgroundColor: "hsl(var(--card))",
                    border: "1px solid hsl(var(--border))",
                    borderRadius: "8px",
                    color: "hsl(var(--foreground))",
                  }}
                  formatter={(value: number) => value.toLocaleString()}
                  cursor={{ fill: "hsl(var(--accent))" }}
                />
                <Bar dataKey="empleos" fill="hsl(var(--chart-1))" radius={[8, 8, 0, 0]} name="Empleos" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}
