import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { TrendingUp, TrendingDown, Briefcase, Users, DollarSign, Building2 } from "lucide-react"

const metrics = [
  {
    title: "Tasa de Desempleo",
    value: "8.7%",
    change: "-0.3%",
    trend: "up",
    icon: Users,
  },
  {
    title: "Sueldo Promedio",
    value: "$720.450",
    change: "+4.2%",
    trend: "up",
    icon: DollarSign,
  },
  {
    title: "Nuevos Empleos",
    value: "45.230",
    change: "+12.5%",
    trend: "up",
    icon: Briefcase,
  },
  {
    title: "Empresas Contratando",
    value: "3.847",
    change: "+8.3%",
    trend: "up",
    icon: Building2,
  },
]

export default function MetricsGrid() {
  return (
    <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
      {metrics.map((metric) => {
        const Icon = metric.icon
        const TrendIcon = metric.trend === "up" ? TrendingUp : TrendingDown
        const trendColor = metric.trend === "up" ? "text-accent" : "text-destructive"

        return (
          <Card key={metric.title}>
            <CardHeader className="flex flex-row items-center justify-between pb-2">
              <CardTitle className="text-sm font-medium text-muted-foreground">{metric.title}</CardTitle>
              <Icon className="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold text-balance">{metric.value}</div>
              <div className={`flex items-center gap-1 text-sm ${trendColor}`}>
                <TrendIcon className="h-4 w-4" />
                <span>{metric.change}</span>
                <span className="text-muted-foreground">vs trimestre anterior</span>
              </div>
            </CardContent>
          </Card>
        )
      })}
    </div>
  )
}
