import { Suspense } from "react"
import DashboardHeader from "@/components/dashboard-header"
import MetricsGrid from "@/components/metrics-grid"
import ChartsSection from "@/components/charts-section"
import DataTable from "@/components/data-table"
import HistoricalTrends from "@/components/historical-trends"
import { Skeleton } from "@/components/ui/skeleton"

export default function DashboardPage() {
  return (
    <div className="min-h-screen bg-background">
      <DashboardHeader />

      <main className="container mx-auto px-4 py-8 space-y-8">
        <Suspense fallback={<MetricsSkeleton />}>
          <MetricsGrid />
        </Suspense>

        <Suspense fallback={<HistoricalSkeleton />}>
          <HistoricalTrends />
        </Suspense>

        <Suspense fallback={<ChartsSkeleton />}>
          <ChartsSection />
        </Suspense>

        <Suspense fallback={<TableSkeleton />}>
          <DataTable />
        </Suspense>
      </main>
    </div>
  )
}

function MetricsSkeleton() {
  return (
    <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
      {[...Array(4)].map((_, i) => (
        <Skeleton key={i} className="h-32 w-full" />
      ))}
    </div>
  )
}

function ChartsSkeleton() {
  return (
    <div className="grid gap-6 lg:grid-cols-2">
      <Skeleton className="h-96 w-full" />
      <Skeleton className="h-96 w-full" />
    </div>
  )
}

function TableSkeleton() {
  return <Skeleton className="h-96 w-full" />
}

function HistoricalSkeleton() {
  return <Skeleton className="h-[550px] w-full lg:col-span-2" />
}
