"use client"

import { useState } from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { ArrowUpDown } from "lucide-react"

const jobPostings = [
  {
    id: "EMP001",
    date: "2024-01-15",
    company: "Falabella",
    position: "Desarrollador Full Stack",
    salary: 1800000,
    sector: "Tecnología",
    status: "Activa",
  },
  {
    id: "EMP002",
    date: "2024-01-15",
    company: "Banco de Chile",
    position: "Analista de Datos",
    salary: 1500000,
    sector: "Finanzas",
    status: "Activa",
  },
  {
    id: "EMP003",
    date: "2024-01-14",
    company: "Codelco",
    position: "Ingeniero de Minas",
    salary: 2200000,
    sector: "Minería",
    status: "Cerrada",
  },
  {
    id: "EMP004",
    date: "2024-01-14",
    company: "Ripley",
    position: "Gerente de Ventas",
    salary: 1600000,
    sector: "Comercio",
    status: "Activa",
  },
  {
    id: "EMP005",
    date: "2024-01-13",
    company: "Hospital Clínico UC",
    position: "Enfermero/a Especializado",
    salary: 950000,
    sector: "Salud",
    status: "Activa",
  },
  {
    id: "EMP006",
    date: "2024-01-13",
    company: "Universidad de Chile",
    position: "Profesor de Ingeniería",
    salary: 1400000,
    sector: "Educación",
    status: "En Revisión",
  },
  {
    id: "EMP007",
    date: "2024-01-12",
    company: "Movistar Chile",
    position: "Ingeniero de Telecomunicaciones",
    salary: 1750000,
    sector: "Tecnología",
    status: "Activa",
  },
  {
    id: "EMP008",
    date: "2024-01-12",
    company: "Constructora Salfa",
    position: "Arquitecto de Proyectos",
    salary: 1650000,
    sector: "Construcción",
    status: "Activa",
  },
]

export default function DataTable() {
  const [sortField, setSortField] = useState<string | null>(null)
  const [sortDirection, setSortDirection] = useState<"asc" | "desc">("desc")

  const handleSort = (field: string) => {
    if (sortField === field) {
      setSortDirection(sortDirection === "asc" ? "desc" : "asc")
    } else {
      setSortField(field)
      setSortDirection("desc")
    }
  }

  const sortedPostings = [...jobPostings].sort((a, b) => {
    if (!sortField) return 0

    const aValue = a[sortField as keyof typeof a]
    const bValue = b[sortField as keyof typeof b]

    if (aValue < bValue) return sortDirection === "asc" ? -1 : 1
    if (aValue > bValue) return sortDirection === "asc" ? 1 : -1
    return 0
  })

  return (
    <Card>
      <CardHeader>
        <CardTitle>Ofertas Laborales Recientes</CardTitle>
        <CardDescription>Últimas ofertas de empleo publicadas en el mercado chileno</CardDescription>
      </CardHeader>
      <CardContent>
        <div className="rounded-md border border-border">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>ID</TableHead>
                <TableHead>
                  <Button
                    variant="ghost"
                    size="sm"
                    onClick={() => handleSort("date")}
                    className="flex items-center gap-1 hover:bg-secondary"
                  >
                    Fecha
                    <ArrowUpDown className="h-4 w-4" />
                  </Button>
                </TableHead>
                <TableHead>Empresa</TableHead>
                <TableHead>Cargo</TableHead>
                <TableHead className="text-right">
                  <Button
                    variant="ghost"
                    size="sm"
                    onClick={() => handleSort("salary")}
                    className="flex items-center gap-1 hover:bg-secondary ml-auto"
                  >
                    Sueldo
                    <ArrowUpDown className="h-4 w-4" />
                  </Button>
                </TableHead>
                <TableHead>Sector</TableHead>
                <TableHead>Estado</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {sortedPostings.map((posting) => (
                <TableRow key={posting.id}>
                  <TableCell className="font-mono text-sm">{posting.id}</TableCell>
                  <TableCell>{posting.date}</TableCell>
                  <TableCell className="font-medium">{posting.company}</TableCell>
                  <TableCell>{posting.position}</TableCell>
                  <TableCell className="text-right font-semibold">${posting.salary.toLocaleString("es-CL")}</TableCell>
                  <TableCell>{posting.sector}</TableCell>
                  <TableCell>
                    <Badge
                      variant={
                        posting.status === "Activa"
                          ? "default"
                          : posting.status === "En Revisión"
                            ? "secondary"
                            : "destructive"
                      }
                    >
                      {posting.status}
                    </Badge>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </div>
      </CardContent>
    </Card>
  )
}
