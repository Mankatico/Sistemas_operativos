@echo off
set /P
xcopy D:\user\ISER2022\Desktop\Archivos D:\backup\Archivos_%date:~-4,4%-%date:~-7,2%-%date:~-10,2%
pause