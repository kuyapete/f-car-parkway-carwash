@echo off
echo ================================================
echo CarWash Pro - Premium Car Care Services
echo ================================================
echo.
echo Installing required packages...
pip install -r requirements.txt
echo.
echo Starting CarWash Pro application...
echo.
echo Open your browser and go to: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
python app.py
pause
