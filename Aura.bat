@echo off
REM 
cd /d "X:\Developing\Aura.dev\Aura.v1" 

REM 
call venv\Scripts\activate

REM 
python main.py %*

REM 
pause
