/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        flamengo: {
          red: '#CC0000',
          dark: '#990000',
        },
      },
    },
  },
  plugins: [],
}
