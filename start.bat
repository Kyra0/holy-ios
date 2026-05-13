@echo off
title CyberAgent - Ali Arda
color 0B
echo.
echo =====================================================
echo   CYBERAGENT v1.0 - Kisisel AI Sistem Ajani
echo =====================================================
echo.

:: Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [HATA] Python bulunamadi! Lutfen Python 3.10+ yukleyin.
    pause
    exit /b 1
)

:: Install deps if needed
echo [*] Bagimliliklar kontrol ediliyor...
pip install -r requirements.txt -q --no-warn-script-location

echo.
echo [*] CyberAgent baslatiliyor...
echo [*] Tarayicinizda acin: http://localhost:5000
echo.

:: Open browser after 2 seconds
start /b cmd /c "timeout /t 2 >nul && start http://localhost:5000"

:: Run server
python agent_server.py

pause
