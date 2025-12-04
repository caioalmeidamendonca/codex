@echo off
chcp 65001 >nul
title AI DEBUG TOOL - Setup

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║     AI DEBUG TOOL        ║          Setup Automático       ║
echo ║                      Versão 2.0                            ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

REM Verificar Python
echo [1/4] Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ❌ Python não encontrado!
    echo.
    echo Por favor, instale Python 3.8 ou superior:
    echo https://www.python.org/downloads/
    echo.
    echo IMPORTANTE: Marque a opção "Add Python to PATH" durante a instalação
    echo.
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✓ Python %PYTHON_VERSION% encontrado
echo.

REM Verificar pip
echo [2/4] Verificando pip...
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ❌ pip não encontrado!
    echo.
    echo Instalando pip...
    python -m ensurepip --default-pip
    if errorlevel 1 (
        echo ❌ Falha ao instalar pip
        pause
        exit /b 1
    )
)
echo ✓ pip encontrado
echo.

REM Atualizar pip
echo [3/4] Atualizando pip...
python -m pip install --upgrade pip --quiet
if errorlevel 1 (
    echo ⚠️  Aviso: Não foi possível atualizar o pip
) else (
    echo ✓ pip atualizado
)
echo.

REM Instalar dependências
echo [4/4] Instalando dependências...
echo.
echo Instalando pacotes necessários:
echo   - anthropic (Claude API)
echo   - customtkinter (Interface gráfica)
echo   - Pillow (Processamento de imagens)
echo.

python -m pip install -r requirements.txt --upgrade

if errorlevel 1 (
    echo.
    echo ❌ Erro ao instalar dependências
    echo.
    echo Tentando instalação individual...
    python -m pip install anthropic>=0.40.0
    python -m pip install customtkinter>=5.2.0
    python -m pip install Pillow>=10.0.0
    
    if errorlevel 1 (
        echo.
        echo ❌ Falha na instalação
        echo.
        echo Por favor, tente instalar manualmente:
        echo   pip install anthropic customtkinter Pillow
        echo.
        pause
        exit /b 1
    )
)

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║              ✓ Instalação Concluída com Sucesso!          ║
echo ╚════════════════════════════════════════════════════════════╝
echo.
echo 🚀 Para iniciar o aplicativo, execute:
echo    start.bat
echo.
echo 📚 Para mais informações, consulte o README.md
echo.

REM Perguntar se deseja iniciar agora
set /p START="Deseja iniciar o aplicativo agora? (S/N): "
if /i "%START%"=="S" (
    echo.
    echo Iniciando AI DEBUG TOOL...
    timeout /t 2 /nobreak >nul
    start.bat
) else (
    echo.
    echo Você pode iniciar o aplicativo a qualquer momento executando start.bat
    pause
)
