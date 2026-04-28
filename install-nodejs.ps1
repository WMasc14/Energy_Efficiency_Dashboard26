# Script para instalar Node.js v18 LTS em Windows
# Executar como Administrador

Write-Host "=== Instalador de Node.js ===" -ForegroundColor Cyan

# Tentar com nvm-windows (mais confiável)
Write-Host "Tentando instalar nvm-windows..." -ForegroundColor Yellow

$nvmUrl = "https://github.com/coreybutler/nvm-windows/releases/download/1.1.11/nvm-setup.exe"
$nvmPath = "$env:TEMP\nvm-setup.exe"

Write-Host "Baixando NVM (Node Version Manager)..." 

try {
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    $ProgressPreference = 'SilentlyContinue'
    Invoke-WebRequest -Uri $nvmUrl -OutFile $nvmPath -ErrorAction Stop
    
    Write-Host "Download concluído. Iniciando instalação..." -ForegroundColor Green
    Start-Process -FilePath $nvmPath -Wait
    
    Write-Host "NVM instalado! Agora instale Node.js com:" -ForegroundColor Green
    Write-Host "  nvm install 18.19.0" -ForegroundColor Cyan
    Write-Host "  nvm use 18.19.0" -ForegroundColor Cyan
    
} catch {
    Write-Host "Erro ao baixar NVM. Acesse nodejs.org manualmente." -ForegroundColor Red
    Write-Host "https://nodejs.org/en/download" -ForegroundColor Cyan
}
