import os

#command_line='mkdir /home/labservidores/Documentos/test1 && chmod -R 777 /home/labservidores/Documentos/test1'
#linea=str(command_line)
#os.system(linea)
comando=str(input("Digita el nombre con el que vas a crear el usuario: "))
command_line='sudo useradd '+comando
linea=str(command_line)
os.system(linea)
ruta='/home/labservidores/Escritorio/'+comando
ruta_actual=str('sudo mkdir '+ruta)
os.system(ruta_actual)
permisos='sudo chown '+comando+':'+comando+" -R "+ruta
permisos_a=str(permisos)
os.system(permisos_a)
os.system('cat /etc/passwd')
os.system('ls -lh')
print("Creacion del usuario, ahora le asignaremos una carpeta por defecto en esta ruta: "+ruta+' y permisos aignados')