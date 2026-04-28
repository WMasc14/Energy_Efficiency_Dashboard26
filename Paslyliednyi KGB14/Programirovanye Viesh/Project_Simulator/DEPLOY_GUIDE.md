# 🚀 GUIA DE DEPLOY - ReactorLab

## ✅ Status Atual

Seu projeto está **100% configurado** e rodando localmente!

- ✅ Backend FastAPI (Python): http://localhost:8000
- ✅ Frontend React (Vite): http://localhost:3000
- ✅ Documentação API: http://localhost:8000/docs

---

## 📋 Opções de Deploy

### 1️⃣ RENDER (Recomendado - Grátis, Fácil) ⭐

**Passos:**

1. Acesse [render.com](https://render.com)
2. Faça login com GitHub
3. Clique em **"New Web Service"**
4. Selecione seu repositório
5. Configure:
   - **Name:** reactorlab
   - **Runtime:** Python 3.11
   - **Build Command:** 
     ```bash
     pip install -r requirements.txt && npm install && npm run build
     ```
   - **Start Command:** 
     ```bash
     uvicorn main:app --host 0.0.0.0 --port $PORT
     ```
6. Deploy automático!

**Vantagens:** Gratuito, fácil, autodeploy no push

---

### 2️⃣ HEROKU (Clássico) 

**Passos:**

1. Instale [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Execute:
   ```bash
   heroku login
   heroku create seu-app-name
   git push heroku main
   ```
3. Abra: `heroku open`

**Nota:** Heroku removeu plano gratuito. Tente Render ou AWS.

---

### 3️⃣ AWS (Robusto)

**Opção A: EC2**
1. Lance instância EC2 (Ubuntu)
2. SSH na instância
3. Clone repositório
4. Instale Python 3.11, Node.js 20
5. Execute:
   ```bash
   pip install -r requirements.txt
   npm install && npm run build
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
6. Use Nginx como proxy reverso (opcional)

**Opção B: ElasticBeanstalk**
1. Instale EB CLI
2. Execute: `eb init` e `eb create`
3. Deploy: `eb deploy`

**Opção C: App Runner (mais simples)**
1. Crie repositório GitHub
2. AWS App Runner → "Create Service"
3. Selecione repositório
4. Configure porta 8000

---

### 4️⃣ DOCKER (Qualquer servidor)

**Build:**
```bash
docker build -t reactorlab .
```

**Rodar localmente:**
```bash
docker run -p 8000:8000 reactorlab
```

**Deploy em Docker Hub:**
```bash
docker login
docker tag reactorlab seu-user/reactorlab
docker push seu-user/reactorlab
```

---

### 5️⃣ GOOGLE CLOUD RUN (Grátis, Serverless)

```bash
gcloud run deploy reactorlab \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

---

## 🛠️ Pré-requisitos por Plataforma

| Plataforma | Reqs | Custo | Facilidade |
|-----------|------|-------|-----------|
| **Render** | GitHub | Grátis | ⭐⭐⭐⭐⭐ |
| **AWS EC2** | Cartão | $5-20/mês | ⭐⭐⭐ |
| **Docker** | Docker | Varia | ⭐⭐⭐⭐ |
| **Google Cloud Run** | Cartão | Grátis (limite) | ⭐⭐⭐⭐ |
| **Heroku** | Cartão | $7/mês | ⭐⭐⭐⭐ |

---

## 📦 Arquivos de Configuração Criados

- ✅ `requirements.txt` - Dependências Python
- ✅ `package.json` - Dependências Node.js
- ✅ `Dockerfile` - Container Docker
- ✅ `Procfile` - Para Heroku
- ✅ `vercel.json` - Para Vercel (se usar)
- ✅ `.dockerignore` - Arquivos ignorados no Docker
- ✅ `deploy.bat` / `deploy.sh` - Scripts de automação
- ✅ `.env.example` - Variáveis de ambiente

---

## 🚨 Checklist Pré-Deploy

Antes de fazer deploy em produção:

- [ ] Commit todo o código: `git add . && git commit -m "initial"`
- [ ] Criar repositório GitHub (se não tiver)
- [ ] Testar build local: `npm run build`
- [ ] Testar backend: `python main.py` (ou uvicorn)
- [ ] Verificar variáveis de ambiente (.env)
- [ ] Testar API endpoints: `http://localhost:8000/docs`

---

## 🎯 Próximos Passos

1. **Escolha uma plataforma** (Render é recomendado)
2. **Siga os passos** específicos acima
3. **Teste a aplicação** após deploy
4. **Configure domínio** (opcional)

---

## 💡 Dicas

- **CORS:** Já está configurado no backend para qualquer origem
- **Proxy:** Vite redireciona `/api/*` para backend
- **Build:** Frontend build em `dist/` (Vite)
- **Logs:** Verifique logs da plataforma se houver erro

---

## 🆘 Troubleshooting

### Erro de porta
```bash
# Se porta 8000 está em uso:
lsof -i :8000  # Linux/Mac
netstat -ano | findstr :8000  # Windows
```

### Node.js/npm não encontrado
- Windows: Use `npm.bat` (já criado)
- Linux/Mac: Instale Node.js 20+

### Build falha
```bash
npm run build  # Testar build localmente
npm install --legacy-peer-deps  # Se houver conflitos
```

---

## 📞 Suporte

Se precisar de ajuda com deploy:
1. Verifique a documentação da plataforma escolhida
2. Consulte os logs de erro
3. Teste tudo localmente primeiro

**Bom deploy! 🎉**
