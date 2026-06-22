export const SPORT_LABELS: Record<string, string> = {
  futebol: 'Futebol',
  basquete: 'Basquete',
  natacao: 'Natação',
  volei: 'Vôlei',
  remo: 'Remo',
  esports: 'eSports',
  futsal: 'Futsal',
  outros: 'Outros',
}

export const SPORT_COLORS: Record<string, string> = {
  futebol: '#CC0000',
  basquete: '#185FA5',
  natacao: '#0F6E56',
  volei: '#854F0B',
  esports: '#534AB7',
  remo: '#993556',
}

export const SPORT_BG: Record<string, string> = {
  futebol: '#FCEBEB',
  basquete: '#E6F1FB',
  natacao: '#E1F5EE',
  volei: '#FAEEDA',
  esports: '#EEEDFE',
  remo: '#FBEAF0',
}

export const TABS = [
  { key: 'geral', label: 'Geral' },
  { key: 'futebol', label: 'Futebol' },
  { key: 'basquete', label: 'Basquete' },
  { key: 'natacao', label: 'Natação' },
  { key: 'esports', label: 'eSports' },
] as const
