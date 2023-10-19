#Importamos lo modulos o librerias
import os
import csv
from pymongo import MongoClient

#Conexion entre la app y mongodb
client=MongoClient('localhost',27017)

#Seleccionamos la base de datos, si no existe la creara.
db=client['practicacsv_db']

#Creamos un clase y definimos una funcion
class PracticaCSV:
    def LecturaCSV(self):
        #Ruta de la carpeta
        ruta_carpeta = './src/resources/csv'
        
        #Extencion del archivo
        extencion_archivo = ""
        
        #Lista para almacenar archivos con la extension
        archivos_con_extencion = []
        
        #Lectura de la carpeta con ListDir
        archivos_carpeta = os.listdir(ruta_carpeta)
       
        #For para iterar sobre todos los archivos en las carpetas
        for archivo in archivos_carpeta:
            #Comprobando si el archivo tiene la extension deseada
            if archivo.endswith(extencion_archivo):
                #agregamos el elemento al final de la lista
                archivos_con_extencion.append(archivo) 

        #Se imprime la lista de archivos con extencion (CSV)
        print(f"Archivos con la extension [{extencion_archivo}]:")
        
        #Se imprime los archivos que contiene la carpeta/ruta carpeta
        print("\nArchivos en carpeta:\n", archivos_con_extencion)
        print("\nLista de archivos")

        #Se agrega indices a la lsita de archivos
        for indice, archivo in enumerate(archivos_con_extencion, start=1):
            print(f"[{indice}] {archivo}") #Se muestran los archivos indexados/enumenrados

        try:
            #Se le pregunta al usuario que CSV quiere ver.
            indice_seleccionado=int(input("Por favor, ingrese el numero del archivo a seleccionar: "))

            if 1<=indice_seleccionado <= len(archivos_con_extencion): #Con 'len' contamos el nuemro de elementos de una lista.
                archivo_seleccionado=archivos_con_extencion[indice_seleccionado-1] 
                ruta_completa=os.path.join(ruta_carpeta, archivo_seleccionado)#Unimos uno o mas componenetes de un ruta.
                print(f"Has seleccionado el archivo: {ruta_completa}")#Mostramos al usuario el csv que ha seleccionado.

                with open(ruta_completa,'r') as archivo: #Abrimos el CSV y lo leemos
                    contenido=csv.DictReader(archivo) #Se lee el archivo CSV como un diccionario
                    
                    #Inicializamos una lista para almacenar el diccionario en filas
                    data=[]

                    #Se itera sobre las filas del archivo CSV y se convierte en un diccionario(s)
                    for fila in contenido:
                       print(fila) #Se imprime/muestra el contenido del CSV ya transformado en diccionario(s).
                       data.append(fila) #Se agrega cada fila como un diccionario a la lista
                
            else:
                print("Indice invalido. Por favor, ingrese un numero valido.")
        except ValueError:
            print("Indice invlaido,Por favor, ingresa un numero valido.")

        except Exception as e:
            print(f"Ocurrio un error: {e}")

        #Posteriormente despues de abrir, leer e imprimir el CSV, se le pregunta al usuario
        # si quiere guardarlo en la base de datos    
        opcion=int(input(f"\n¿Guardar [{archivo_seleccionado}] en la base de datos? \n1. Si \n2. No \nRespuesta: "))
        if opcion==1:                  
            print(f"\nEstamos trabajando con: '{archivo_seleccionado}'")#Se le indica al susario que csv esta trabajando.

            #Seleccionamos la coleccion en la que deseamos guardar los datos 
            #Esto se hace, usando el nombre del archivo sin la extencion como el nombre de la coleccion
            nombre_coleccion=archivo_seleccionado.split('.')[0]#Dividimos el nombre y la extension, quedando solo el nombre 
            coleccion=db[nombre_coleccion]#Guarda la coleccion con el nombre del archivo CSV
            coleccion.insert_many(data)#Inserta los datos del diccionario en la coleccion
            
        else:
            return f"El archivo '{archivo_seleccionado}' no se guardo."
        
#Construccion de la aplicacion
app_main = PracticaCSV() #Creamos una instancia a la clase
app_main.LecturaCSV() #Mandamos a llamar a la clase

#Cerramos la conexion con la base de datos
client.close()