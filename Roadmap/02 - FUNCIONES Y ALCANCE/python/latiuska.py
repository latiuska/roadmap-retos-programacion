""
Función simple 
"""
def funcion_simple():
    print("Esta es una función simple")
funcion_simple()

"""
Funcion con retorno 
"""
def funcion_con_retorno():
    return "Esta es una función con retorno"

retorno = funcion_con_retorno()
print(retorno)

"""
Función con argumento
"""
def funcion_arg(nombre):
    print(f"Esta es una función con argumento. Hola {nombre}")
funcion_arg("Laura")

"""
Función con varios argumentos
"""
def funcion_args(nombre, lenguaje):
    print(f"Esta es una función con varios argumentos. Hola {nombre}, {lenguaje} es una excelente opción")
funcion_args("Laura", "Python")

"""
Función con argumento predefinido
"""
def funcion_arg_def(nombre = "Laura"):
    print(f"Esta es una función con un argumento definido. Hola {nombre}")
funcion_arg_def()

"""
Función con retorno de varios valores
"""
def funcion_retorno_varios_valores():
    return "Laura", "Python"
nombre, lenguaje=funcion_retorno_varios_valores()
print(nombre)
print(lenguaje)

"""
Función con número variable de argumentos
"""
def variable_arg_var(*name): #Podemos pasar más de un nombre
    for names in name:
        print(f"Hola {names}")

variable_arg_var("Layra", "Gael", "Tyaro")

"""
Función con número variable de argumentos y claves
"""
def variable_key_arg_var(**names): #Podemos pasar más de un nombre y claves
    for param, name in names.items():
        print(f"{param} {name}")

variable_key_arg_var(
    nombre ="Layra",
    alias = "Latiuska",
    edad= "49")

"""
Función dentro de otra función
"""
def funcion_externa():
    def funcion_interna():
        print("Función interna: Hola Python")
    funcion_interna() #Si no la llamo no se ejecuta al llamar a la función externa
funcion_externa()

"""
Funciones Built-in (ya dentro del lenguaje) 
"""
#PRINT
print("hola")
#LEN
print(len("hola"))
#TYPE
print(type("hola"))
#LOWER
print("HOLA".lower())
#UPPER
print("hola".upper())

"""
Otras => string:
capitalize
title
count
find
isdigit
isalnum
isalpha
replace
strip
split
etc.
Otras => listas:
append
count
extend
index
insert
pop
remove
reverse
sort
clear
Otras => Tuplas
add
discard
copy
update
difference
intersection
etc.
"""

"""
Variables locales y globales = scope de la variable
"""

global_variable = "python"
def hola():
    local_var = "hola" #Solo funciona dentro del ámbito de la función
    print(f" {local_var} {global_variable}")
hola()

"""
Extra
"""

"""Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda"""

def extra(text1, text2) -> int:
    count = 0
    for number in range (1,101):
        if number % 3 == 0 and number % 5 == 0:
            print(text1+text2)
        elif number % 3 == 0:
            print(text1)
        elif number % 5 == 0:
            print(text2)
        else:
            print(number)
            count += 1
    return count

print(extra("Fizz","Buzz"))


