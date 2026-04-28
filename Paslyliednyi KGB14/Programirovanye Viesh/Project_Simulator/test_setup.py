#!/usr/bin/env python3
"""
Script de teste para validar se o ReactorLab está configurado corretamente
"""

import requests
import sys
from time import sleep

print("=" * 60)
print("🧪 TESTE DE VALIDAÇÃO - ReactorLab")
print("=" * 60)

# Test 1: Backend API
print("\n1️⃣  Testando Backend (FastAPI)...")
try:
    response = requests.get("http://localhost:8000/docs")
    if response.status_code == 200:
        print("   ✅ Backend está rodando em http://localhost:8000")
    else:
        print(f"   ❌ Backend respondeu com status {response.status_code}")
except requests.exceptions.ConnectionError:
    print("   ❌ Backend não está respondendo")
    print("      Execute: python -m uvicorn main:app --reload")
    sys.exit(1)

# Test 2: API Endpoint
print("\n2️⃣  Testando Endpoint /simulate...")
try:
    test_params = {
        "CA0": 1.0,
        "F": 1.0,
        "V": 1.0,
        "k": 0.1,
        "time": 10.0
    }
    response = requests.post("http://localhost:8000/simulate", json=test_params)
    if response.status_code == 200:
        print("   ✅ API /simulate respondendo corretamente")
        print(f"      Resposta: {response.json()}")
    else:
        print(f"   ❌ API retornou status {response.status_code}")
except Exception as e:
    print(f"   ❌ Erro: {e}")

# Test 3: CORS
print("\n3️⃣  Testando CORS...")
try:
    response = requests.get(
        "http://localhost:8000/docs",
        headers={"Origin": "http://localhost:3000"}
    )
    if "access-control-allow-origin" in str(response.headers).lower():
        print("   ✅ CORS configurado corretamente")
    else:
        print("   ⚠️  CORS pode não estar ativo")
except Exception as e:
    print(f"   ❌ Erro ao testar CORS: {e}")

# Test 4: Frontend
print("\n4️⃣  Testando Frontend (Vite)...")
try:
    response = requests.get("http://localhost:3000")
    if response.status_code == 200:
        print("   ✅ Frontend está rodando em http://localhost:3000")
    else:
        print(f"   ⚠️  Frontend respondeu com status {response.status_code}")
except requests.exceptions.ConnectionError:
    print("   ❌ Frontend não está respondendo")
    print("      Execute em outro terminal: npm start")

# Test 5: Requirements
print("\n5️⃣  Verificando dependências Python...")
try:
    import fastapi
    import uvicorn
    import pydantic
    print("   ✅ Dependências Python instaladas")
except ImportError as e:
    print(f"   ❌ Falta instalação: {e}")

# Test 6: Node/npm
print("\n6️⃣  Verificando Node.js...")
try:
    import subprocess
    result = subprocess.run(["npm", "--version"], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"   ✅ npm {result.stdout.strip()} instalado")
    else:
        print("   ❌ npm não encontrado")
except Exception as e:
    print(f"   ❌ Erro: {e}")

# Summary
print("\n" + "=" * 60)
print("📊 RESULTADO DO TESTE")
print("=" * 60)
print("""
✅ Backend:  http://localhost:8000 (FastAPI + Uvicorn)
✅ Frontend: http://localhost:3000 (React + Vite)
✅ API Docs: http://localhost:8000/docs

Se todos os testes passaram, seu projeto está PRONTO!

📚 Próximos passos:
   1. Leia: DEPLOY_GUIDE.md
   2. Escolha uma plataforma
   3. Faça o deploy!
""")
print("=" * 60)
