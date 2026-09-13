@echo off
setlocal
chcp 65001 >nul
python -X utf8 "%~dp0blog.py" publish %*
exit /b %errorlevel%
