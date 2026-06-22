import React from 'react';
import { NewsArticle, Match } from '../../types';

interface MetricsGridProps {
  news: NewsArticle[];
  matches: Match[];
  upcoming: Match[];
}

export const MetricsGrid: React.FC<MetricsGridProps> = ({ news, matches, upcoming }) => {
  const metrics = [
    { val: '43°', label: 'Títulos nacionais', sub: '+1 em 2024', color: 'text-red-700' },
    { val: news.length, label: 'Notícias hoje', sub: 'todas modalidades', color: '' },
    { val: matches.filter(m => m.result === 'V').length, label: 'Vitórias recentes', sub: 'últimas partidas', color: 'text-green-700' },
    { val: upcoming.length, label: 'Próximos jogos', sub: 'agendados', color: '' },
  ];

  return (
    <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
      {metrics.map((m, i) => (
        <div key={i} className="bg-white rounded-xl border border-gray-100 p-4 text-center">
          <div className={`text-3xl font-medium ${m.color}`}>{m.val}</div>
          <div className="text-xs text-gray-500 mt-1">{m.label}</div>
          <div className="text-xs text-gray-400 mt-0.5">{m.sub}</div>
        </div>
      ))}
    </div>
  );
};
