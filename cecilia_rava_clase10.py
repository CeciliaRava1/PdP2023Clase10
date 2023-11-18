# Declaracion de la clase empleado, junto con los atributos rol, edad y tareas
class Empleado:
    def __init__(self, rol, edad, tareas):
        self.rol = rol
        self.edad = edad
        self.tareas = tareas

# Declaracion de funcion que permite el ingreso de un empleado
def ingresar_empleado():
    rol = input("Ingrese el rol del empleado: ")
    edad = int(input("Ingrese la edad del empleado: "))
    tareas = input("Ingrese las tareas del empleado (separadas por comas): ").split(',')
    return Empleado(rol, edad, tareas)

# Declaracion de funcion lambda que determina la cantidad de empleados atareados
# Un empleado esta atareado cuando realiza dos o mas tareas
def empleados_atareados(empleados):
    return list(filter(lambda empleado: len(empleado.tareas) >= 2, empleados))

# Ingreso de cantidad de empleados por parte del usuario
# Ingreso de los empleados por parte del usuario
if __name__ == "__main__":
    cantidad_empleados = int(input("Ingrese la cantidad de empleados: "))
    
    empleados = []
    for _ in range(cantidad_empleados):
        nuevo_empleado = ingresar_empleado()
        empleados.append(nuevo_empleado)

    atareados = empleados_atareados(empleados)

    print("\nEmpleados Atareados:")
    for empleado in atareados:
        print(f"Rol: {empleado.rol}, Edad: {empleado.edad}, Tareas: {', '.join(empleado.tareas)}")
