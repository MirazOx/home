const fs = require('fs');
const path = require('path');

const htmlPath = '/Users/miraz/.gemini/antigravity/scratch/miraz-redesign/credentials/index.html';
const html = fs.readFileSync(htmlPath, 'utf8');

// Extract the json data block
const jsonMatch = html.match(/<script type="application\/json" id="inline-certificates-data">(.*?)<\/script>/s);
if (!jsonMatch) {
  console.error("FAIL: Could not find json data block");
  process.exit(1);
}
const data = JSON.parse(jsonMatch[1]);
console.log(`Loaded ${data.length} certificates.`);

// Simulate the JS logic
const THEME_ORDER = [
  'Journalism & Fact-Checking',
  'Research & Data',
  'Science, Data & Technology',
  'English Language & Communication',
  'Career Development & Productivity',
  'Project Management & Leadership',
  'Negotiation & Conflict Resolution',
  'Philosophy, Religion & Ethics',
  'Psychology & Mental Health',
  'Business & Economics',
  'Language Learning',
  'Awards & Recognition'
];

try {
  let ALL = data;
  const themes = [...new Set(data.map(c => c.theme))];
  themes.sort((a,b) => (THEME_ORDER.indexOf(a) - THEME_ORDER.indexOf(b)));
  
  function extractYear(date) {
    const match = String(date || '').match(/(20\d{2}|19\d{2})/);
    return match ? Number(match[1]) : null;
  }
  
  const years = [...new Set(data.map(c => extractYear(c.date)).filter(Boolean))].sort((a,b) => b - a);
  
  console.log("Themes found:", themes);
  console.log("Years found:", years);
  console.log("JS Logic passed successfully!");
} catch (e) {
  console.error("JS Logic failed:", e);
  process.exit(1);
}
