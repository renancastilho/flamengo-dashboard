import React from 'react';
import { format } from 'date-fns';
import { ptBR } from 'date-fns/locale';
import { NewsArticle } from '../../types';
import { SPORT_LABELS, SPORT_COLORS, SPORT_BG } from '../../constants/sports';

interface NewsListProps {
  news: NewsArticle[];
}

export const NewsList: React.FC<NewsListProps> = ({ news }) => {
  return (
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
  );
};
