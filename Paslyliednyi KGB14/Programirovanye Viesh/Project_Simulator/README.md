# ReactorLab - Simulador de Reator Químico

## Execução Local

### Backend (FastAPI)
```bash
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend (React + Vite)
```bash
# Configurar PATH com Node.js (se não instalado globalmente)
$env:PATH = "C:\Users\valter.mascarenhas\AppData\Local\Temp\node-portable-v20\node-v20.11.0-win-x64;$env:PATH"

npm start
# ou
npm run dev
```

Acesse:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## Deploy

### Docker
```bash
docker build -t reactorlab .
docker run -p 8000:8000 -p 3000:3000 reactorlab
```

### Heroku
```bash
heroku login
heroku create seu-app-name
git push heroku main
```

### AWS EC2
1. SSH na instância
2. Clonar repositório
3. Instalar Python, Node.js e dependências
4. Rodar `npm run build` para build do frontend
5. Rodar FastAPI com uvicorn

### Render
1. Conectar repositório GitHub
2. Criar novo Web Service
3. Build Command: `pip install -r requirements.txt && npm install && npm run build`
4. Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

## Estrutura do Projeto

```
.
├── main.py              # FastAPI server
├── Simulator.py         # Simulação química
├── App.jsx              # Componente React principal
├── Dashboard.jsx        # Dashboard da simulação
├── Controls.jsx         # Controles de entrada
├── Plot.jsx             # Gráficos (recharts)
├── api.js               # Cliente API (axios)
├── package.json         # Dependências Node.js
├── requirements.txt     # Dependências Python
├── vite.config.js       # Config Vite
├── index.html           # HTML principal
└── Dockerfile           # Config Docker
```

## Ambiente

- Python 3.11+
- Node.js 20.11.0+
- FastAPI 0.104+
- React 18+
- Vite 5+
