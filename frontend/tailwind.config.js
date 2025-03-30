export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        primary: "#E3A048",   // Company gold
        secondary: "#19202B", // Company dark blue/black
        accent: "#DC3545",    // Example accent color (like alerts)
        background: "#F4F5F7", // Light gray background
        card: "#FFFFFF",
        darkCard: "#1F2937",
      },
    },
  },
  plugins: [],
};
