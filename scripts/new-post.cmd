@echo off
setlocal
chcp 65001 >nul
python -X utf8 "%~dp0blog.py" new %*
set "blog_exit=%errorlevel%"
if "%~1"=="" pause
exit /b %blog_exit%
