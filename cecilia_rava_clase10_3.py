# Declaracion de funcion que recibe como argumento una cadena

# Declaracion de variables
cadena = input()

# Declaracion de la funcion lambda descrita en el enunciado
def titulo(cadena):
    return ' '.join(word.capitalize() for word in cadena.split())

# Llamadon a la funcion
resultado = titulo(cadena)
print("Cadena ingresada:", cadena)
print("Cadena obtenida:", resultado)

