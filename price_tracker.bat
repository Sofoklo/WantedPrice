@echo off
start chrome.exe  http://127.0.0.1:8000/
cmd /k "cd /d C:\Users\Zeko\Desktop\price_tracker\Scripts & activate & cd /d    C:\Users\Zeko\Desktop\price_tracker\src & python manage.py runserver"