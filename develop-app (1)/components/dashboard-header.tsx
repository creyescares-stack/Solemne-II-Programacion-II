import { Briefcase, Download } from "lucide-react"
import { Button } from "@/components/ui/button"

export default function DashboardHeader() {
  return (
    <header className="border-b border-border bg-card">
      <div className="container mx-auto px-4 py-6">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-primary">
              <Briefcase className="h-6 w-6 text-primary-foreground" />
            </div>
            <div>
              <h1 className="text-2xl font-bold text-balance">Dashboard de Empleabilidad en Chile</h1>
              <p className="text-sm text-muted-foreground">Análisis del Mercado Laboral y Estadísticas de Empleo</p>
            </div>
          </div>

          <Button variant="outline" size="sm" className="gap-2 bg-transparent">
            <Download className="h-4 w-4" />
            Exportar Datos
          </Button>
        </div>
      </div>
    </header>
  )
}
