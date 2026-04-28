# ReactorLab - Simulador de Reator Químico

Projeto full-stack que conecta um backend Python/FastAPI com um frontend React/Vite. O Render está configurado para deploy automático a partir do repositório GitHub.

## ✅ O que o projeto faz
- Simula um reator químico usando parâmetros de entrada.
- Exibe gráficos interativos com Recharts.
- Fornece API REST em FastAPI.
- Serve a interface React em produção.

## 🚀 Como rodar localmente

### 1. Backend
```bash
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 2. Frontend
```bash
npm install
npm run dev
```

### URLs locais
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API docs: http://localhost:8000/docs

## 🔧 Build para produção

```bash
npm install
npm run build
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

Em produção, o FastAPI serve o build React em `dist/`.

## 🌐 Deploy automático no Render

Este projeto está configurado para deploy automático usando `render.yaml`.

### Como configurar no Render
1. Faça login em https://render.com
2. Clique em **New** > **Web Service**
3. Conecte seu repositório GitHub
4. Selecione o branch `master`
5. O Render detectará o arquivo `render.yaml` e usará as configurações abaixo

### Comandos de deploy
- Build Command: `pip install -r requirements.txt && npm install && npm run build`
- Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### O que acontece no deploy
- O frontend React é compilado em `dist/`
- O backend FastAPI serve a aplicação estática
- A API continua disponível em `/simulate`

## 📁 Estrutura principal do projeto

```
.
├── main.py
├── Simulator.py
├── App.jsx
├── Dashboard.jsx
├── Controls.jsx
├── Plot.jsx
├── api.js
├── package.json
├── requirements.txt
├── vite.config.js
├── index.html
├── render.yaml
├── Dockerfile
```

## 📌 Dependências principais
- Python 3.11+
- FastAPI
- Uvicorn
- React 18
- Vite 5
- Axios
- Recharts

## 📝 Observação
Se você quiser testar a versão de produção localmente, execute `npm run build` e depois rode o backend com Uvicorn.

