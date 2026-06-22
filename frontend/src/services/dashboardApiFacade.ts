import { SportCategory, NewsArticle, AIChatResponse } from "../types";
import { newsService, matchService, aiService, sportsService } from "./api";

export const dashboardApiFacade = {
  getNews: (params?: { sport?: SportCategory; featured?: boolean; limit?: number }) => {
    return newsService.list(params);
  },

  getSingleNews: (id: number) => {
    return newsService.get(id);
  },

  createNews: (data: Partial<NewsArticle>) => {
    return newsService.create(data);
  },

  getMatches: (params?: { sport?: SportCategory; completed?: boolean; limit?: number }) => {
    return matchService.list(params);
  },

  getUpcomingMatches: (limit?: number) => {
    return matchService.upcoming(limit);
  },

  askAI: (question: string, context?: string): Promise<AIChatResponse> => {
    return aiService.chat(question, context);
  },

  getSportAISummary: (sport: string) => {
    return aiService.sportSummary(sport);
  },

  getSports: () => {
    return sportsService.list();
  },

  getSport: (sportCategory: string) => {
    return sportsService.get(sportCategory);
  },
};
