from .verificaciones_admin import Verificaciones


class GestionHuespedes:
    def __init__(self, huespedes):
        self.huespedes = huespedes

    def menu_huespedes(self):
        while True:
            print("\nIngrese la operación a realizar:")
            print("1. Registrar Huésped")
            print("2. Mostrar Huespedes registrados")
            print("3. Actualizar información del huésped")
            print("4. Volver al menú principal")
            opcion = input("Seleccione una opción (1-4): ")
            
            if opcion == "1":
                self.registrar_huesped()
            elif opcion == "2":
                self.mostrar_huespedes()
            elif opcion == "3":
                self.actualizar_huesped()
            elif opcion == "4":
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

    def actualizar_huesped(self):
        if not self.huespedes.mostrar_huespedes():
            return

        try:
            while True:
                try:
                    indice = int(input("\nIngrese el número del huésped que desea actualizar: ")) - 1
                    if 0 <= indice < len(self.huespedes.lista_huespedes):
                        break
                    print("Número de huésped no válido. Intente nuevamente.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")

            print("\n¿Qué información desea actualizar?")
            print("1. Nombre")
            print("2. Apellido")
            print("3. Teléfono")
            
            while True:
                try:
                    campo = int(input("Seleccione una opción (1-3): "))
                    if campo in [1, 2, 3]:
                        break
                    print("Opción no válida. Por favor, seleccione 1, 2 o 3.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")

            if campo == 1:
                nuevo_valor = Verificaciones.pedir_cadena_valida("Ingrese el nuevo nombre: ")
            elif campo == 2:
                nuevo_valor = Verificaciones.pedir_cadena_valida("Ingrese el nuevo apellido: ")
            else:  
                nuevo_valor = Verificaciones.pedir_numero_valido("Ingrese el nuevo teléfono: ")

            self.huespedes.actualizar_huesped(indice, campo, nuevo_valor)

        except Exception as e:
            print(f"\nError durante la actualización: {str(e)}")

    def registrar_huesped(self):
        nombre = Verificaciones.pedir_cadena_valida("Ingrese el nombre del huésped: ")
        apellido = Verificaciones.pedir_cadena_valida("Ingrese el apellido del huésped: ")
        telefono = Verificaciones.pedir_numero_valido("Ingrese el número de teléfono del huésped: ")
        self.huespedes.registrar_huesped(nombre, apellido, telefono)

    def mostrar_huespedes(self):
        self.huespedes.mostrar_huespedes()