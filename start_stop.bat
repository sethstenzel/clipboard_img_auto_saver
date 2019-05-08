@echo off
echo Setting working directory: %~dp0
cd %~dp0
REM user python instead of pythonw to see verbose output.
REM start python clipboard_img_auto_saver.py
start python clipboard_img_auto_saver.py
echo Press any key to continue and kill script...
pause
taskkill /f /im python*
taskkill /f /im pythonw*
timeout 3