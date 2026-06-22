import axios from 'axios'
import { SportCategory, NewsArticle, Match, AIChatResponse } from '../types'

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

export const newsService = {
  list: (params?: { sport?: SportCategory; featured?: boolean; limit?: number }) =>
    api.get<NewsArticle[]>('/news', { params }).then((r) => r.data),
  get: (id: number) => api.get<NewsArticle>(`/news/${id}`).then((r) => r.data),
  create: (data: Partial<NewsArticle>) =>
    api.post<NewsArticle>('/news', data).then((r) => r.data),
}

export const matchService = {
  list: (params?: { sport?: SportCategory; completed?: boolean; limit?: number }) =>
    api.get<Match[]>('/matches', { params }).then((r) => r.data),
  upcoming: (limit?: number) =>
    api.get<Match[]>('/matches/upcoming', { params: { limit } }).then((r) => r.data),
}

export const aiService = {
  chat: (question: string, context?: string) =>
    api.post<AIChatResponse>('/ai/chat', { question, context }).then((r) => r.data),
  sportSummary: (sport: string) =>
    api.get<{ sport: string; summary: string }>(`/ai/summary/${sport}`).then((r) => r.data),
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
