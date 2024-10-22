from .verificaciones_admin import Verificaciones

class GestionInventario:
    def __init__(self, inventario):
        self.inventario = inventario

    def menu_inventario(self):
        while True:
            print("\nIngrese la operación a realizar:")
            print("1. Agregar item al inventario")
            print("2. Remover item del inventario")
            print("3. Mostrar inventario")
            print("4. Volver al menú principal")
            opcion = input("Seleccione una opción (1-4): ")
            if opcion == "1":
                productoID = Verificaciones.pedir_ID_valido("Ingrese el ID del producto: ")
                nombre = Verificaciones.pedir_cadena_valida("Ingrese el nombre del item: ")
                cantidad = Verificaciones.pedir_ID_valido("Ingrese la cantidad a agregar: ")
                categoria = Verificaciones.pedir_cadena_valida("Ingrese la categoría del item: ")
                proveedor = Verificaciones.pedir_cadena_valida("Ingrese el proveedor del item: ")
                self.inventario.agregarProducto(productoID, nombre, cantidad, categoria, proveedor)
            elif opcion == "2":
                nombre = Verificaciones.pedir_cadena_valida("Ingrese el nombre del item a remover: ")
                cantidad = Verificaciones.pedir_numero_valido("Ingrese la cantidad a remover: ")
                self.inventario.eliminarProducto(nombre, cantidad)
            elif opcion == "3":
                self.inventario.mostrar_inventario()
            elif opcion == "4":
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
