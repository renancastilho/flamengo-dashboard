import { useState } from 'react'
import { useQuery } from 'react-query'
import { newsService, matchService, aiService, SportCategory } from '../services/api'
import { format } from 'date-fns'
import { ptBR } from 'date-fns/locale'
import {
  BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid
} from 'recharts'

const SPORT_LABELS: Record<string, string> = {
  futebol: 'Futebol', basquete: 'Basquete', natacao: 'Natação',
  volei: 'Vôlei', remo: 'Remo', esports: 'eSports', futsal: 'Futsal', outros: 'Outros',
}

const SPORT_COLORS: Record<string, string> = {
  futebol: '#CC0000', basquete: '#185FA5', natacao: '#0F6E56',
  volei: '#854F0B', esports: '#534AB7', remo: '#993556',
}

const SPORT_BG: Record<string, string> = {
  futebol: '#FCEBEB', basquete: '#E6F1FB', natacao: '#E1F5EE',
  volei: '#FAEEDA', esports: '#EEEDFE', remo: '#FBEAF0',
}

const TABS: Array<{ key: string; label: string }> = [
  { key: 'geral', label: 'Geral' },
  { key: 'futebol', label: 'Futebol' },
  { key: 'basquete', label: 'Basquete' },
  { key: 'natacao', label: 'Natação' },
  { key: 'esports', label: 'eSports' },
]

export default function Dashboard() {
  const [tab, setTab] = useState('geral')
  const [sportFilter, setSportFilter] = useState<SportCategory | undefined>()
  const [aiQuestion, setAiQuestion] = useState('')
  const [aiAnswer, setAiAnswer] = useState('')
  const [aiLoading, setAiLoading] = useState(false)

  const { data: news = [] } = useQuery(
    ['news', sportFilter],
    () => newsService.list({ sport: sportFilter, limit: 20 }),
    { refetchInterval: 60_000 }
  )

  const { data: matches = [] } = useQuery(
    ['matches'],
    () => matchService.list({ completed: true }),
    { refetchInterval: 120_000 }
  )

  const { data: upcoming = [] } = useQuery(
    ['upcoming'],
    () => matchService.upcoming(),
    { refetchInterval: 60_000 }
  )

  const handleAsk = async () => {
    if (!aiQuestion.trim()) return
    setAiLoading(true)
    setAiAnswer('')
    try {
      const res = await aiService.chat(aiQuestion)
      setAiAnswer(res.answer)
    } catch {
      setAiAnswer('Erro ao consultar a IA. Verifique a configuração da API.')
    } finally {
      setAiLoading(false)
    }
  }

  const sportCounts = news.reduce<Record<string, number>>((acc, n) => {
    acc[n.sport] = (acc[n.sport] || 0) + 1
    return acc
  }, {})

  const chartData = Object.entries(sportCounts).map(([sport, count]) => ({
    sport: SPORT_LABELS[sport] || sport,
    notícias: count,
    fill: SPORT_COLORS[sport] || '#888',
  }))

  return (
    <div className="min-h-screen bg-gray-50 font-sans">
      {/* Header */}
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

      {/* Nav tabs */}
      <nav className="bg-white border-b border-gray-200 px-6 py-2 flex gap-2 overflow-x-auto">
        {TABS.map((t) => (
          <button
            key={t.key}
            onClick={() => { setTab(t.key); setSportFilter(t.key === 'geral' ? undefined : t.key as SportCategory) }}
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
        {/* Métricas */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {[
            { val: '43°', label: 'Títulos nacionais', sub: '+1 em 2024', color: 'text-red-700' },
            { val: news.length, label: 'Notícias hoje', sub: 'todas modalidades', color: '' },
            { val: matches.filter(m => m.result === 'V').length, label: 'Vitórias recentes', sub: 'últimas partidas', color: 'text-green-700' },
            { val: upcoming.length, label: 'Próximos jogos', sub: 'agendados', color: '' },
          ].map((m, i) => (
            <div key={i} className="bg-white rounded-xl border border-gray-100 p-4 text-center">
              <div className={`text-3xl font-medium ${m.color}`}>{m.val}</div>
              <div className="text-xs text-gray-500 mt-1">{m.label}</div>
              <div className="text-xs text-gray-400 mt-0.5">{m.sub}</div>
            </div>
          ))}
        </div>

        <div className="grid md:grid-cols-2 gap-6">
          {/* Notícias */}
          <div className="bg-white rounded-xl border border-gray-100 p-5">
            <h2 className="text-sm font-medium text-gray-500 mb-4">Últimas notícias</h2>
            <div className="flex flex-col divide-y divide-gray-50">
              {news.slice(0, 6).map((n) => (
                <div key={n.id} className="py-3 first:pt-0 last:pb-0">
                  <span
                    className="text-xs font-medium px-2 py-0.5 rounded-full mb-1 inline-block"
                    style={{ background: SPORT_BG[n.sport], color: SPORT_COLORS[n.sport] }}
                  >
                    {SPORT_LABELS[n.sport]}
                  </span>
                  <p className="text-sm font-medium text-gray-800 leading-snug">{n.title}</p>
                  {n.published_at && (
                    <p className="text-xs text-gray-400 mt-1">
                      {format(new Date(n.published_at), "dd 'de' MMM, HH:mm", { locale: ptBR })}
                      {n.source && ` · ${n.source}`}
                    </p>
                  )}
                </div>
              ))}
              {news.length === 0 && (
                <p className="text-sm text-gray-400 py-4 text-center">
                  Nenhuma notícia cadastrada ainda.
                </p>
              )}
            </div>
          </div>

          {/* Resultados */}
          <div className="bg-white rounded-xl border border-gray-100 p-5">
            <h2 className="text-sm font-medium text-gray-500 mb-4">Resultados recentes</h2>
            <div className="flex flex-col divide-y divide-gray-50">
              {matches.slice(0, 5).map((m) => (
                <div key={m.id} className="py-3 first:pt-0 last:pb-0 flex items-center justify-between">
                  <div>
                    <span
                      className="text-xs font-medium px-2 py-0.5 rounded-full mb-1 inline-block"
                      style={{ background: SPORT_BG[m.sport], color: SPORT_COLORS[m.sport] }}
                    >
                      {SPORT_LABELS[m.sport]}
                    </span>
                    <p className="text-sm font-medium text-gray-800">
                      Flamengo {m.flamengo_score} × {m.opponent_score} {m.opponent}
                    </p>
                    <p className="text-xs text-gray-400">{m.competition}</p>
                  </div>
                  <span className={`text-sm font-medium px-2 py-1 rounded ${
                    m.result === 'V' ? 'text-green-700 bg-green-50' :
                    m.result === 'D' ? 'text-red-700 bg-red-50' : 'text-gray-600 bg-gray-50'
                  }`}>{m.result || '—'}</span>
                </div>
              ))}
              {matches.length === 0 && (
                <p className="text-sm text-gray-400 py-4 text-center">
                  Nenhum resultado cadastrado ainda.
                </p>
              )}
            </div>
          </div>
        </div>

        {/* Gráfico de notícias por esporte */}
        {chartData.length > 0 && (
          <div className="bg-white rounded-xl border border-gray-100 p-5">
            <h2 className="text-sm font-medium text-gray-500 mb-4">Notícias por modalidade</h2>
            <ResponsiveContainer width="100%" height={200}>
              <BarChart data={chartData} barCategoryGap="40%">
                <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
                <XAxis dataKey="sport" tick={{ fontSize: 12 }} />
                <YAxis tick={{ fontSize: 12 }} allowDecimals={false} />
                <Tooltip />
                <Bar dataKey="notícias" radius={[4, 4, 0, 0]} fill="#CC0000" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        )}

        {/* IA Chat */}
        <div className="bg-white rounded-xl border border-gray-100 p-5">
          <h2 className="text-sm font-medium text-gray-500 mb-3">Pergunte sobre o Flamengo (IA)</h2>
          <div className="flex gap-2">
            <input
              className="flex-1 border border-gray-200 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-1 focus:ring-red-500"
              placeholder="Ex: Qual o histórico do Fla na Libertadores?"
              value={aiQuestion}
              onChange={(e) => setAiQuestion(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && handleAsk()}
            />
            <button
              onClick={handleAsk}
              disabled={aiLoading}
              className="bg-red-700 text-white px-4 py-2 rounded-lg text-sm font-medium hover:bg-red-800 disabled:opacity-50 transition"
            >
              {aiLoading ? 'Pensando...' : 'Perguntar'}
            </button>
          </div>
          <div className="flex flex-wrap gap-2 mt-2">
            {['Títulos do Flamengo', 'Esportes do CRF', 'Fla na Libertadores'].map((q) => (
              <button
                key={q}
                onClick={() => setAiQuestion(q)}
                className="text-xs border border-gray-200 rounded-full px-3 py-1 text-gray-500 hover:bg-gray-50"
              >
                {q}
              </button>
            ))}
          </div>
          {aiAnswer && (
            <div className="mt-3 p-3 bg-gray-50 rounded-lg text-sm text-gray-700 leading-relaxed">
              {aiAnswer}
            </div>
          )}
        </div>
      </main>
    </div>
  )
}
