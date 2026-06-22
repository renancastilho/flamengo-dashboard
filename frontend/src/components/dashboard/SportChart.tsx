import React from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid } from 'recharts';
import { NewsArticle } from '../../types';
import { SPORT_LABELS, SPORT_COLORS } from '../../constants/sports';

interface SportChartProps {
  news: NewsArticle[];
}

export const SportChart: React.FC<SportChartProps> = ({ news }) => {
  const sportCounts = news.reduce<Record<string, number>>((acc, n) => {
    acc[n.sport] = (acc[n.sport] || 0) + 1;
    return acc;
  }, {});

  const chartData = Object.entries(sportCounts).map(([sport, count]) => ({
    sport: SPORT_LABELS[sport] || sport,
    notícias: count,
    fill: SPORT_COLORS[sport] || '#888',
  }));

  if (chartData.length === 0) return null;

  return (
    <div className="bg-white rounded-xl border border-gray-100 p-5">
      <h2 className="text-sm font-medium text-gray-500 mb-4">Volume de Notícias por Modalidade</h2>
      <div className="h-[250px] w-full">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={chartData}>
            <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#f0f0f0" />
            <XAxis dataKey="sport" fontSize={11} tickLine={false} axisLine={false} />
            <YAxis fontSize={11} tickLine={false} axisLine={false} />
            <Tooltip
              cursor={{ fill: '#f9f9f9' }}
              contentStyle={{ borderRadius: '8px', border: 'none', boxShadow: '0 4px 12px rgba(0,0,0,0.1)' }}
            />
            <Bar dataKey="notícias" radius={[4, 4, 0, 0]} barSize={40} />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};
