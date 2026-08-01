module.exports = {
  locales: ["en", "hi"],
  input: [
    "frontend/src/**/*.{js,jsx,ts,tsx}"
  ],
  output: "frontend/src/locales/$LOCALE/common.json"
};