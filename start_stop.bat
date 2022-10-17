@echo off
echo Setting working directory: %~dp0
cd %~dp0

REM use pythonw instead of python to hide python window.
REM start pythonw clipboard_img_auto_saver.py

py clipboard_img_auto_saver.py
echo Press any key to continue and kill script...
pause
taskkill /f /im python*
taskkill /f /im pythonw*
timeout 3
