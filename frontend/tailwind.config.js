import { defineConfig } from 'tailwindcss'

export default defineConfig({
  content: [
    './index.html',
    './src/**/*.{js,ts,jsx,tsx}',
  ],
  darkMode: 'class', // Enables dark mode via class strategy
  theme: {
    extend: {
      colors: {
        // Company brand colors
        primary: '#E3A048',   // Gold
        secondary: '#19202B', // Dark blue/black
        accent: '#DC3545',    // Accent (for alerts/errors)

        // UI-specific palette
        background: '#F4F5F7',
        card: '#FFFFFF',
        darkCard: '#1F2937',
      },
    },
  },
  plugins: [],
});
