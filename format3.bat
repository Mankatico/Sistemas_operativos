@echo off
echo ****************************
echo seleccione una Unidad 
echo ****************************
echo.
echo.
SET /p letra=letra_unidad
SET /p formato=formato_unidad
SET /p label=nombre_del_dispositivo
format %letra%: /fs:%formato% /v:%label% /q
pause