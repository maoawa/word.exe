@echo off
echo ------------------------------
echo UAC will be DISABLED in 2 seconds.
echo ------------------------------
timeout -t 2 -nobreak >nul
copy word.exe reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f
echo ------------------------------
echo Exiting in 3 seconds...
timeout -t 3 -nobreak >nul