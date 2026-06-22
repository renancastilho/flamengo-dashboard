import React from 'react';
import { Match } from '../../types';
import { SPORT_LABELS, SPORT_COLORS, SPORT_BG } from '../../constants/sports';

interface MatchResultsProps {
  matches: Match[];
}

export const MatchResults: React.FC<MatchResultsProps> = ({ matches }) => {
  return (
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
  );
};
