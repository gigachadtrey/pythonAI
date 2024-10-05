@echo off
pip install -r requirements.txt > nul 2>nul
call "%~dp0code.py"
exit /b 0