# Hi, I'm Jose Torres! 👋
# CSV y Diccionarios
En esta practica se hace la lectura de archivos csv previamente adquirido, pero se han agregado otrs archivos csv, esto para testear sus funciones. El objetivo de esta practica es sencillo, leer y guardar el csv en la base de datos.

## Objetivo
    1. Leer el archivo CSV
    2. Transformar el CSV a diccionarios con Python
    3. Almacenar el diccionario en una lista
    4. Insertar los datos del diccionarios en la base de datos.

## CSV x MongoDB & Python
El programa se desarrollo en el lenguaje de Python, en el IDE Visual Studio Code (VSCode) y como base de datos MongoDB. Este programa tiene origen a una practica solicitada por el profesor Oscar Cobos, para la materia Analisis Inteligente de Datos 1 de la unidad 2.

Haciendo investigacion, se llego a la conclusion de usar No-SQL, esto se debe a que los datos se guardan en forma de documentos. En un principio era leer un archivo CSV con cierta estructura, esto se realizo de manera exitosa, pero al ser proporcionado un segundo archivo csv, el programa fallo, pues el codigo estaba destinado para el primer CSV. Pues ahora el objetivo era leer el archivo csv sin importar su estructura, es decir, leerlo aun que tenga 2,3 o 4 columnas, hasta tener mas 10 columnas.

Esto se hizo posible gracias al No-SQL, puesto que, no lleva una estructura como tal, permitiendo que podamos guardar prodaticamente cualquier archivo CSV sin importar su tamaño, cantidad de columnas y nombre de sus encabezados.

Asi mismo, Python no provee una caracteristica llamada Diccionarios, pues estos permite almacenar pares de clave-valor. Todo el programa se desarrollo en entornos virtuales.

## Contexto
Ahora que sabemos de que va el programa, lectura de CSV y guardaro en bases de datos, se le agregaron caracteristicas propias por el programador, la cuales se muestran a continuacion:

    1. Conexion a MongoDB.
    2. Se creo una clase y se definio una funcion.
    2. Para hacerlo mas dinamico, se creo una carpeta contenedora de CSVs.
    3. De la carpeta se seleccionan solo lo que tenga ".csv" o se puede dejar vacio, para ver el contenido de la carpeta.
    4. Se agrego el dataset proporcionado por el profesor.
    5. Se agregaron mas de 10 datasets a la carpeta.
    6. Se lee la carpeta y se muestra al usuario.
    7. Se lista los archivo con respectivos indices.
    8. El usuario puede seleccionar el dataset, posterirormente se muestra el contenido.
    9. Se le pregunta al usuario, si desea almacenar el datasets en la base de datos.
    10. Se almacena el dataset en la base de datos con el nombre propio del dicho dataset y termina el programa.

Claro esta que, se puede ir detallando mas el programa, pero hasta cierto punto cumple con su proposito, almacenar cualquier CSV sin importar su estructura en una base de datos.
## 🚀 About Me
Estudiante de la poderosisima carrer de Ingenieria en Tecnologias de Informacion y Comunicacion. Ya en noveno semetre gente.

Saludos para quien vea este Readme
