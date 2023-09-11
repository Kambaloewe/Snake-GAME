@echo off
color 5

title Checking Python Version
python --version | findstr "3.11."
if %errorlevel%==0 (
    echo Python 3.11.0 or higher is already installed
) else (
    echo Python 3.11.0 or higher is not installed
    echo Please install Python 3.11.0 or higher and add it to your PATH
)


cd tools
title Checking for updates
echo Checking for updates...
python update.py



