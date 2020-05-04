@echo off

set store_address=%1

cd /d %~dp0

if "%1"=="" (
    echo "Faltou o endereco da loja"
) else (
    python login.py %store_address%
)

cd %HOMEPATH%