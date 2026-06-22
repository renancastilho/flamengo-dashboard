import { useState } from 'react'
import { useQuery } from 'react-query'
import { SportCategory } from '../types'
import { TABS } from '../constants/sports'
import { dashboardApiFacade } from '../services/dashboardApiFacade' 
import { MetricsGrid } from './dashboard/MetricsGrid'
import { NewsList } from './dashboard/NewsList'
import { MatchResults } from './dashboard/MatchResults'
import { AIChatSection } from './dashboard/AIChatSection'
import { SportChart } from './dashboard/SportChart'

export default function Dashboard() {
  const [tab, setTab] = useState('geral')
  const [sportFilter, setSportFilter] = useState<SportCategory | undefined>()

  const { data: news = [] } = useQuery(
    ['news', sportFilter],
    () => dashboardApiFacade.getNews({ sport: sportFilter, limit: 20 }),
    { refetchInterval: 60_000 }
  )

  const { data: matches = [] } = useQuery(
    ['matches'],
    () => dashboardApiFacade.getMatches({ completed: true }),
    { refetchInterval: 120_000 }
  )

  const { data: upcoming = [] } = useQuery(
    ['upcoming'],
    () => dashboardApiFacade.getUpcomingMatches(),
    { refetchInterval: 60_000 }
  )

  return (
    <div className="min-h-screen bg-gray-50 font-sans">
      <header className="bg-red-700 text-white px-6 py-4 flex items-center justify-between shadow">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-full bg-black flex items-center justify-center text-red-600 font-semibold text-sm border-2 border-white">
            CRF
          </div>
          <div>
            <h1 className="text-lg font-medium">Flamengo Nação</h1>
            <p className="text-xs text-red-200">Dashboard Esportivo — Todos os esportes</p>
          </div>
        </div>
        <span className="text-xs bg-white text-red-700 px-3 py-1 rounded-full flex items-center gap-1.5 font-medium">
          <span className="w-2 h-2 rounded-full bg-red-600 animate-pulse" />
          Ao vivo
        </span>
      </header>

      <nav className="bg-white border-b border-gray-200 px-6 py-2 flex gap-2 overflow-x-auto">
        {TABS.map((t) => (
          <button
            key={t.key}
            onClick={() => { 
              setTab(t.key); 
              setSportFilter(t.key === 'geral' ? undefined : t.key as SportCategory) 
            }}
            className={`px-4 py-1.5 rounded-full text-sm transition-all ${
              tab === t.key
                ? 'bg-red-700 text-white'
                : 'text-gray-500 hover:bg-gray-100 border border-gray-200'
            }`}
          >
            {t.label}
          </button>
        ))}
      </nav>

      <main className="max-w-7xl mx-auto px-6 py-6 flex flex-col gap-6">
        <MetricsGrid news={news} matches={matches} upcoming={upcoming} />

        <div className="grid md:grid-cols-2 gap-6">
          <NewsList news={news} />
          <MatchResults matches={matches} />
        </div>

        <SportChart news={news} />
        
        <AIChatSection />
      </main>
    </div>
  )
}
