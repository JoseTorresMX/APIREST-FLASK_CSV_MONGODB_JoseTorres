import pymongo

#Conectar a la base de datos
cliente=pymongo.MongoClient("mongodb://localhost:27017/")

#Seleciconamos la base de datos
base_de_datos=cliente["practicacsv_db"]

#Seleccionamos la coleccion en la base de datos
coleccion=base_de_datos["AnalisisRLE"]

#Clave-valor que queremos buscar en los documentos
#claveComponent="Component"
#valorComponent="C215_1"

claveStatus="Status"
valorStatus="F"

#Consulta para encontrar un doumento con la clave-valor especifica
#documento=coleccion.find_one({claveComponent: valorComponent, claveStatus: valorStatus})
documento=coleccion.find_one({claveStatus: valorStatus})

#print("Encabezados: ")
#claves=list(documento.keys())

#print(claves)

#Validamos una condicions
if documento:
    #print(f"Informacion de la coleccion:\n", documento)
    #Asignamos una variable, con len para contar.
    total_elementos=len(documento)
    #Imprimimos los valores enontrados
    print(f"Valores encotrados: {total_elementos} con [{claveStatus}] y [{valorStatus}]")


else:
    print(f"El documento no fue encontrado.\nLa(s) clave(S) y/o lo(s) valor(es) no existe(n) en la base de datos.")
#print("Colecciones en la base de datos:\n")
#for coleccion in colecciones:
 #   print(coleccion)