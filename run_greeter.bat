@echo off
REM Run the Wave Greeter application
REM This batch file launches the Python script using Anaconda

REM Change to the script directory
cd /d "%~dp0"

REM Run the Python script with pythonw (no console window)
start "" pythonw wave_greeter.py

REM Alternative: If pythonw doesn't work, uncomment the line below
REM start "" python wave_greeter.py