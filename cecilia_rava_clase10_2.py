# Declaracion de funcion que permite al usuario ingresar elementos en la lista
def ingresar_elementos():
    lista = []
    seguir = True

    while seguir:
            numero = int(input("Ingrese un numero o '00' para terminar: "))
            if numero == 00:
                seguir = False
            else:
                lista.append(numero)
    return lista

# Importacion de librerias
from functools import reduce

import lista as lista

# Declaracion de la funcion lambda para eliminar elementos duplicados de la lista
eliminar_duplicados = lambda lista: reduce(lambda acc, elemento: acc + [elemento] if elemento not in acc else acc, lista, [])

# Llamado de la funcion para ingresar elementos
mi_lista = ingresar_elementos()
print("Lista ingresada:", mi_lista)

# Llamado de la funcion lambda para eliminar duplicados
nueva_lista = eliminar_duplicados(mi_lista)
print("Lista sin duplicados:", nueva_lista)
