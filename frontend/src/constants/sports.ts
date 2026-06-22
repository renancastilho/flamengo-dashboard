export const SPORT_LABELS: Record<string, string> = {
  futebol: "Futebol",
  basquete: "Basquete",
  natacao: "Natação",
  volei: "Vôlei",
  remo: "Remo",
  esports: "eSports",
  futsal: "Futsal",
  outros: "Outros",
};

export const SPORT_COLORS: Record<string, string> = {
  futebol: "#CC0000",
  basquete: "#185FA5",
  natacao: "#0F6E56",
  volei: "#854F0B",
  esports: "#534AB7",
  remo: "#993556",
  futsal: "#D97706",
  outros: "#6B7280",
};

export const SPORT_BG: Record<string, string> = {
  futebol: "#FCEBEB",
  basquete: "#E6F1FB",
  natacao: "#E1F5EE",
  volei: "#FAEEDA",
  esports: "#EEEDFE",
  remo: "#FBEAF0",
  futsal: "#FFF7ED",
  outros: "#F3F4F6",
};

export const TABS = [
  { key: "geral", label: "Geral" },
  { key: "futebol", label: "Futebol" },
  { key: "basquete", label: "Basquete" },
  { key: "natacao", label: "Natação" },
  { key: "volei", label: "Vôlei" },
  { key: "remo", label: "Remo" },
  { key: "esports", label: "eSports" },
  { key: "futsal", label: "Futsal" },
] as const;
