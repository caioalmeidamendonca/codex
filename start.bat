@echo off
chcp 65001 >nul
title AI DEBUG TOOL Generator Pro

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║         AI DEBUG TOOL Generator Pro - Iniciando...         ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

REM Verificar se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python não encontrado!
    echo.
    echo Execute setup.bat primeiro para instalar as dependências.
    echo.
    pause
    exit /b 1
)

REM Verificar se as dependências estão instaladas
python -c "import anthropic, customtkinter" >nul 2>&1
if errorlevel 1 (
    echo ⚠️  Dependências não encontradas!
    echo.
    echo Execute setup.bat primeiro para instalar as dependências.
    echo.
    pause
    exit /b 1
)

REM Iniciar aplicação
echo ✓ Iniciando aplicação...
echo.
python main.py

if errorlevel 1 (
    echo.
    echo ❌ Erro ao executar o aplicativo
    echo.
    echo Se o problema persistir:
    echo 1. Execute setup.bat novamente
    echo 2. Verifique se todas as dependências foram instaladas
    echo 3. Consulte o README.md para mais informações
    echo.
    pause
)
