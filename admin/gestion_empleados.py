from .verificaciones_admin import Verificaciones

class GestionEmpleados:
    def __init__(self, empleado_manager):
        self.empleado_manager = empleado_manager

    def menu_empleados(self):
        while True:
            print("\nIngrese la operación a realizar:")
            print("1. Registrar Empleado")
            print("2. Asignar tarea")
            print("3. Registrar horario")
            print("4. Actualizar información del empleado")
            print("5. Mostrar empleados")
            print("6. Volver al menú principal")
            opcion = input("Seleccione una opción (1-6): ")
            if opcion == "1":
                self.registrar_empleado()
            elif opcion == "2":
                self.asignar_tarea_empleado()
            elif opcion == "3":
                self.registrar_horario_empleado()
            elif opcion == "4":
                self.actualizar_info_empleado()
            elif opcion == "5":
                self.mostrar_empleados()
            elif opcion == "6":
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")

    def actualizar_info_empleado(self):
        if not self.empleado_manager.mostrar_empleados():
            return

        try:
            while True:
                IdEmpleado = input("\nIngrese el ID del empleado que desea actualizar: ")
                empleado = next((e for e in self.empleado_manager.lista_empleados if e.IdEmpleado == IdEmpleado), None)
                if empleado:
                    break
                print("ID de empleado no encontrado. Intente nuevamente.")

            print("\n¿Qué información desea actualizar?")
            print("1. Nombre")
            print("2. Apellido")
            print("3. Teléfono")
            print("4. Puesto")
            
            while True:
                try:
                    campo = int(input("Seleccione una opción (1-4): "))
                    if campo in [1, 2, 3, 4]:
                        break
                    print("Opción no válida. Por favor, seleccione 1, 2, 3 o 4.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")

            if campo == 1:
                nuevo_valor = Verificaciones.pedir_cadena_valida("Ingrese el nuevo nombre: ")
            elif campo == 2:
                nuevo_valor = Verificaciones.pedir_cadena_valida("Ingrese el nuevo apellido: ")
            elif campo == 3:
                nuevo_valor = Verificaciones.pedir_numero_valido("Ingrese el nuevo teléfono: ")
            else:  
                nuevo_valor = input("Ingrese el nuevo puesto: ")

            self.empleado_manager.actualizar_informacion_empleado(IdEmpleado, campo, nuevo_valor)

        except Exception as e:
            print(f"\nError durante la actualización: {str(e)}")

    def registrar_empleado(self):
        nombre = Verificaciones.pedir_cadena_valida("Ingrese el nombre del empleado: ")
        apellido = Verificaciones.pedir_cadena_valida("Ingrese el apellido del empleado: ")
        telefono = Verificaciones.pedir_numero_valido("Ingrese el número de teléfono del empleado: ")
        IdEmpleado = Verificaciones.pedir_ID_valido("Ingrese el ID del empleado: ")
        Horario = input("Ingrese el horario del empleado: ")
        puesto = input("Ingrese el puesto del empleado: ")
        
        self.empleado_manager.registrar_empleado(nombre, apellido, telefono, IdEmpleado, Horario, puesto)

    def asignar_tarea_empleado(self):
        if self.empleado_manager.lista_empleados:
            IdEmpleado = input("Ingrese el ID del empleado: ")
            self.empleado_manager.asignar_tarea(IdEmpleado)
        else:
            print("No hay empleados registrados")

    def registrar_horario_empleado(self):
        if self.empleado_manager.lista_empleados:
            IdEmpleado = input("Ingrese el ID del empleado: ")
            self.empleado_manager.registrar_horario(IdEmpleado)
        else:
            print("No hay empleados registrados")
            
    def mostrar_empleados(self):
        self.empleado_manager.mostrar_empleados()