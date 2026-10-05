@echo off
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Starting server...
python main.py
pause
