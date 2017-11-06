@echo off
echo Run this program from the directory where the input file is stored..!!
echo.
set /P file=Enter file name: 
for /f %%a in (%file%) do call :process %%a
goto :eof
:process
set srv=%1
for /f "tokens=2" %%b in ('nslookup %srv%^|find /i "Name:"') do (
	if %errorlevel% EQU 0 echo %%b >> results.txt
	if %errorlevel% NEQ 0 echo HostNameNotResolved >> results.txt
)