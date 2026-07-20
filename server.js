const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 3000;

app.get('/api/container-feed', (req, res) => {
  const feedPath = path.join(__dirname, 'container-feed.json');
  const data = JSON.parse(fs.readFileSync(feedPath, 'utf8'));
  res.json(data);
});

app.use(express.static(path.join(__dirname, 'public')));

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Dashboard running on port ${PORT}`);
});
