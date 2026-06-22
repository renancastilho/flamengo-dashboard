export type SportCategory =
  | 'futebol' | 'basquete' | 'natacao' | 'volei'
  | 'remo' | 'esports' | 'futsal' | 'outros'

export interface NewsArticle {
  id: number
  title: string
  summary?: string
  url?: string
  source?: string
  sport: SportCategory
  is_featured: boolean
  published_at?: string
  created_at: string
}

export interface Match {
  id: number
  sport: SportCategory
  competition: string
  round_name?: string
  opponent: string
  flamengo_score?: number
  opponent_score?: number
  is_home: boolean
  venue?: string
  match_date: string
  is_completed: boolean
  result?: 'V' | 'D' | 'E'
}

export interface AIChatResponse {
  answer: string
  tokens_used: number
}
