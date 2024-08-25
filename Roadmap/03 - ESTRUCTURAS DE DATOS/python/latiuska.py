"""
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */
"""

# Listas (array en Python no existe) Guarda elementos de forma ordenada
"""
Ordenadas
Mutables
Se pueden trabajar y manipular
Su orden es el orden de inserción de cada elemento

"""
my_list = ["Gael", "Lati", "Tyaro", "Evee"]
my_list1 = ["Agus", "Albert"]
my_list.append("Ivonne") #Añadir datos
my_list.remove("Ivonne") #Elimina el elemento indicado
my_list.pop() #Elimina el último elemento de la lista
my_list.extend(my_list1) #Añade los elementos de una lista a la otra
my_list.insert(1, "Caco") #Añade un elemento en la posicion indicada
my_list.reverse() #Invierte el orden de los elementos de la lista
#my_list.clear() #Borra los elementos de la lista
my_list.sort #Ordena los elementos de la lista
my_list.count("Agus") #Cuenta la cantidad de veces que aparece el elemento indicado
print(my_list)

# Tuplas
"""
Ordenadas
Inmutables
Para poder modificarlas tenemos que transformarlas en una lista y luego volverlas a tupla
"""
my_tupla = (1, "hola", 58, "adiós")
print(my_tupla[-1]) #Imprime el último valor de la tupla
#my_tupla = tuple(sorted(my_tupla)) #Ordenamos la tupla
print(my_tupla)

# Set
"""
Desordenados por lo que no soportan indexado
Son mutables, se pueden modificar con add o remove, por ejemplo.
Solo admite elementos únicos, si hay duplicados solo mostrará uno
{} Crea un diccionario vacio
() Si necesitamos un set vacío usar ()"""

#Declaracion

my_set = set([1,2,5,4,5,5]) #Si usamos la palabra Set tenemos que poner los elementos entre corchetas para que los tome como un único conjunto
my_set1 = {1,5,5,8,4,} #Si no usamos la palabra set ponemos los valores entre llaves
len(my_set) #Nos indica la cantidad de elementos que tiene el set
9 in my_set #Verificamos si un valor está en el set. Devuelve True or False
10 not in my_set #Verificamos si un valor no está en el set. Devuelve True or False
my_set.add(15) #Añadimos elementos al set. Si el elemento ya existe no lo añade
my_set.discard(5) #Elimina el elemento. Si el elemento no existe, no hace nada
#my_set.remove(5) #Elimina el elemento. Si el elemento no existe, da un mensaje de error
#my_set.clear() #Elimina todos los elementos del conjunto
my_set.pop() #Elimina un elemento de forma aleatoria
my_set|my_set1 # | Une ambos conjuntos
my_set & my_set1 # & Nos devuelve los valores comunes a ambos conjuntos
my_set - my_set1 # - Nos devuelve los elements no comunes
print(my_set)

# Diccionarios
"""
Se escriben entre {}
Están compuestos por una clave y un valor: "nombre"(clave):"Juan"(valor)
Ambos están separados por dos puntos, y todo el conjunto se encierra entre {}
La clave tiene que ser siempre un dato inmutable, como una cadena. El valor puede ser de cualquier tipo.
Para recuperar el valor pasamos la clave
"""
my_diccionario = {"Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Argentina": "Buenos Aires",
    "Francia": "Paris"}
print("La capital de Uruguay es", my_diccionario["Uruguay"])
del(my_diccionario["Francia"]) #Borra la capital de Francia
for pais, capital in my_diccionario.items(): #Con items mostramos todos los valores del diccionario
    print("La capital de {} es {}".format(pais, capital))
my_diccionario["Brasil"] = "Brasilia" #Añadimos un elemento al diccionario
my_diccionario.update({"Paraguay": "Asuncion"}) #Añadimos con update. La informacion a añadir va entre ({})
if "Brasil" in my_diccionario: #Verificamos si un elemento se encuentra en el diccionario
    print("La capital de Brasil es", my_diccionario["Brasil"])
print(my_diccionario.items()) #Imprime un conjunto de las claves y los valores del diccionario
print(my_diccionario.keys()) #Imprime un conjunto de las claves del diccionario
print(my_diccionario.values()) #Imprime un conjunto con los valores del diccionario

# Extra (Agenda)
"""
Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 """

def agenda():
    mi_agenda = {}

    def insertar_contacto():
        telefono = input("Inserte el numero de teléfono: ")
        if telefono.isdigit() and len(telefono) <= 11:
            mi_agenda[nombre] = telefono
        else:
            print("La longitud del teléfono debe de ser igual o menor a 11. Introduce un telefono válido")

    while True:

        print("*"*50)
        print("Mi agenda")
        print("*"*50)
        print('''
        1 - Crear un contacto
        2 - Eliminar un contacto
        3 - Buscar un contacto
        4 - Actualizar un contacto
        5 - Salir''')

        opcion = input("\n Elige una opción:")

        match opcion:
            case "1":
                nombre = input("Introduce el nombre del contacto:")
                insertar_contacto()
            case "2":
                nombre = print(input("Ingrese el nombre del contacto a eliminar: "))
                if nombre in mi_agenda:
                    del mi_agenda[nombre]
                    print("El contacto se ha eliminado correctamente")
            case "3":
                nombre = input("Introduce el nombre del cliente a buscar: ")
                if nombre in mi_agenda:
                    print(f"El número de telefono de {nombre} es: {mi_agenda[nombre]}.")
                else:
                    print("El nombre buscado no existe")
            case "4":
                nombre = input("Introduce el nombre del contacto a actualizar: ")
                if nombre in mi_agenda:
                    insertar_contacto()
                else:
                    print("El nombre que has introducido no se encuentra en la agenda")
            case "5":
                print("Muchas gracias por haber utilizado la agenda")
                break
            case _:
                print("Opción no válida. Tienes que seleccionar una de las opciones del 1 al 5")
agenda()
