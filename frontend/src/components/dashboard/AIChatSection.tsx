import React, { useState } from 'react';
import { dashboardApiFacade } from '../../services/dashboardApiFacade';

export const AIChatSection: React.FC = () => {
  const [aiQuestion, setAiQuestion] = useState('');
  const [aiAnswer, setAiAnswer] = useState('');
  const [aiLoading, setAiLoading] = useState(false);

  const handleAsk = async () => {
    if (!aiQuestion.trim()) return; 
    setAiLoading(true);
    setAiAnswer('');
    
    try {
      const res = await dashboardApiFacade.askAI(aiQuestion);
      setAiAnswer(res.answer);
    } catch {
      setAiAnswer('Erro ao consultar a IA. Verifique a configuração da API.');
    } finally {
      setAiLoading(false);
    }
  };

  return (
    <div className="bg-white rounded-xl border border-gray-100 p-5">
      <h2 className="text-sm font-medium text-gray-500 mb-4">Pergunte ao Especialista (IA)</h2>
      
      <div className="flex gap-2">
        <input
          type="text"
          value={aiQuestion}
          onChange={(e) => setAiQuestion(e.target.value)}
          placeholder="Ex: Quem é o maior artilheiro do basquete?"
          className="flex-1 text-sm border border-gray-200 rounded-lg px-3 py-2 focus:outline-none focus:ring-1 focus:ring-red-500"
          onKeyDown={(e) => e.key === 'Enter' && handleAsk()} 
        />
        <button
          onClick={handleAsk}
          disabled={aiLoading}
          className="bg-black text-white px-4 py-2 rounded-lg text-sm font-medium hover:bg-gray-800 disabled:bg-gray-400 transition-colors"
        >
          {aiLoading ? '...' : 'Perguntar'}
        </button>
      </div>

      {aiAnswer && (
        <div className="mt-4 p-3 bg-gray-50 rounded-lg border border-gray-100">
          <p className="text-xs font-bold text-red-700 mb-1 uppercase tracking-wider">Resposta:</p>
          <p className="text-sm text-gray-700 leading-relaxed whitespace-pre-wrap">{aiAnswer}</p>
        </div>
      )}
    </div>
  );
};
