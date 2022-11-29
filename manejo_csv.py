3import csv


def llenar(vector, cnt_personas):
    for i in range(cnt_personas):
        vector.append([])
        for j in range(3):
            dato = str(input("Digite el "+vector[0][j]+" de la persona: "))
            vector[i+1].append(dato)


def creando(vector,direccion):  # Función crear archivo csv

    """dire = 'C:\\python\\original.csv'"""  # Directorio a guardar el archivo csv

    # with open permite abrir el archivo y crearlo con la sentencia 'w'
    with open(direccion, 'w', newline='')as csvfile:

        """lista = [['Código', 'Nombre', 'Apellido'], ['1', 'Pedro', 'Arias'], [
            '2', 'Juan', 'García']] """ # lista a guardar dentro del archivo plano

        # el objeto csv.writer permite dar los parámetros de como debe ser creado el archivo plano
        writer = csv.writer(csvfile, delimiter=';')

        # el objeto writerows me permite escribir toda la lista en líneas separadas
        writer.writerows(vector)
        
        print("Se ha guardado el archivo")


def leyendo(direccion):  # Función leer archivo csv

    "dire = direccion"  # Directorio donde se encuentra el archivo csv

    # with open permite abrir el archivo y leerlo por medio de la sentencia 'r'
    with open(direccion, 'r', newline='')as csvfile:

        # el objeto csv.reader permite leer el archivo por medio de los parametro dados
        reader = csv.reader(csvfile, delimiter=';')

        for row in reader:  # Me permite hacer el recorrido del archivo plano para imprimirlo en pantalla

            print(row)  # Imprime la lista línea por línea


def agregando(direccion,vector):  # Función agregar al final del archivo csv

    "dire = 'D:\\Python\\original.csv' " # Directorio donde se encuentra el archivo csv

    # with open permite abrir el archivo y leerlo por medio de la sentencia 'r'
    with open(direccion, 'r', newline='')as csvfile:

        # el objeto csv.reader permite leer el archivo por medio de los parametro dados
        reader = csv.reader(csvfile, delimiter=';')

        # La variable data cumple la función de una lista, la cual recibe los datos del csv y los almacena
        data = [line for line in reader]

    # with open permite abrir el archivo y crearlo con la sentencia 'w'
    with open(direccion, 'w', newline='')as csvfile:

        # Lista a agregar al final del archivo
        "lista = [['3', 'Jorge', 'Moncada'], ['4', 'Lucas', 'Marulanda']]"

        # el objeto csv.writer permite dar los parámetros de como debe ser creado el archivo plano
        writer = csv.writer(csvfile, delimiter=';')

        # Escribo los datos que contenia el csv de nuevo
        writer.writerows(data)

        # Escribo en el archivo csv los datos de la lista a agregar
        writer.writerows(vector)


def eliminando(dire,search):  # Funcion eliminar, esta elimina la línea que se entrega por parámetro

    "dire = 'C:\\Users\\ander\\OneDrive\\Escritorio\\Sistemas_Operativos\\ted.csv' " # Dirección del documento

    # with open permite abrir el archivo y leerlo por medio de la sentencia 'r'
    with open(dire, 'r', newline='')as csvfile:

        # el objeto csv.reader permite leer el archivo por medio de los parametro dados
        reader = csv.reader(csvfile, delimiter=';')

        # La variable data cumple la función de una lista, la cual recibe los datos del csv y los almacena
        data = [line for line in reader]

    # with open permite abrir el archivo y crearlo con la sentencia 'w'
    with open(dire, 'w', newline='')as csvfile:

        # el objeto csv.writer permite dar los parámetros de como debe ser creado el archivo plano
        writer = csv.writer(csvfile, delimiter=';')

        # llamando a la lista data se elimina la linea dada utilizando la función pop
        data.pop(search)

        # Escribo los datos que contiene la lista modificada.
        writer.writerows(data)


# guardar la lista anterior para actualizar el documento, consultar ¿Cómo retornar una lista en python?

x = 0

while (x != 5):
    vector = [['id', 'nombre', 'apellido']]
    print("\n Menu Principal\n Opcion 1: Crear un Archivo Csv \n Opcion 2: Leer un archivo csv \n Opcion 3: Para actualizar un archivo Csv \n Opcion 4: Para buscar y eliminar un dato dentro de un archivo Csv \n Opcion 5: Salir")

    x = (int(input(" Opcion a escoger :")))

    if (x == 1):

        y = 1

        while (y != 0):

            y = (int(input("\n SubMenu\n Has entrado al Submenu \n Opcion 1: Llenar lista por teclado \n Opcion 2: Leer lista a guardar en archivo Csv \n Opcion 0: Salir al menu principal \n Opcion a escoger:")))

            if (y == 1):
                cnt_personas = int(input("Digite la cantidad de personas a registrar: "))
                llenar(vector, cnt_personas)
            if(y==2):
                print(vector)
                t=str(input("Quieres guardar este archivo como csv: s=si n=no \n Si deseas sobreescribirlo regresa al submenu y crea un nuevo vector: "))
                if(t=="s"):
                    ruta=str(input("Digita la ruta en la que se va a guardar el archivo: "))
                    nombre=str(input("Digita el nombre del archivo: "))
                    creando(vector, ruta+"\\"+nombre+'.csv')
    if(x==2):
        dir=str(input("Digita la ruta completa donde se encuentra el archivo a leer: "))    
        leyendo(dir)
    if(x==3):
        dir=str(input("Digita la ruta completa donde se encuentra el archivo a Actualizar: "))
        leyendo(dir)
        cnt_personas = int(input("Digite la cantidad de personas a registrar: "))
        llenar(vector, cnt_personas)
        agregando(dir, vector)
        leyendo(dir)
    if(x==4):
        dir=str(input("Digita la ruta completa donde se encuentra el archivo a editar: "))
        cnt_personas = int(input("Digite la linea de codigo a eliminar: "))
        eliminando(dir,cnt_personas)
    if(x==5):
        print((" Hasta pronto"))
