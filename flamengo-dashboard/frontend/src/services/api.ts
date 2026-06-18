import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export const api = axios.create({
  baseURL: `${API_URL}/api/v1`,
  headers: { 'Content-Type': 'application/json' },
})

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

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

export const newsService = {
  list: (params?: { sport?: SportCategory; featured?: boolean; limit?: number }) =>
    api.get<NewsArticle[]>('/news', { params }).then((r) => r.data),
  get: (id: number) => api.get<NewsArticle>(`/news/${id}`).then((r) => r.data),
  create: (data: Partial<NewsArticle>) =>
    api.post<NewsArticle>('/news', data).then((r) => r.data),
}

export const matchService = {
  list: (params?: { sport?: SportCategory; completed?: boolean }) =>
    api.get<Match[]>('/matches', { params }).then((r) => r.data),
  upcoming: (sport?: SportCategory) =>
    api.get<Match[]>('/matches/upcoming', { params: { sport } }).then((r) => r.data),
}

export const sportsService = {
  list: () => api.get('/sports').then((r) => r.data),
  get: (sport: SportCategory) => api.get(`/sports/${sport}`).then((r) => r.data),
}

export const aiService = {
  chat: (question: string, context?: string) =>
    api.post('/ai/chat', { question, context }).then((r) => r.data),
  sportSummary: (sport: string) =>
    api.get(`/ai/summary/${sport}`).then((r) => r.data),
}

export const authService = {
  login: (email: string, password: string) =>
    api
      .post('/auth/login', new URLSearchParams({ username: email, password }), {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      })
      .then((r) => {
        localStorage.setItem('token', r.data.access_token)
        return r.data
      }),
  register: (email: string, username: string, password: string) =>
    api.post('/auth/register', { email, username, password }).then((r) => r.data),
  logout: () => localStorage.removeItem('token'),
}
