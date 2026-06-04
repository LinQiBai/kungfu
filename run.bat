@echo off
call conda activate gongfa
cd /d %~dp0
python main.py
pause
