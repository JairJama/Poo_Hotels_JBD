from .huespedes import Huespedes, Empleado
from .evento import Evento
from .verificaciones_admin import Verificaciones
from .inventario import Inventario
from .gestion_huespedes import GestionHuespedes
from .gestion_empleados import GestionEmpleados
from .gestion_eventos import GestionEventos
from .gestion_inventario import GestionInventario

class Main:
    def __init__(self):
        self.huespedes = Huespedes("", "", "")
        self.empleado_manager = Empleado(0,0,0,0,0,0)
        self.eventos_registrados = []
        self.inventario = Inventario(0, "", 0, "", "")
        
        self.gestor_huespedes = GestionHuespedes(self.huespedes)
        self.gestor_empleados = GestionEmpleados(self.empleado_manager)
        self.gestor_eventos = GestionEventos(self.eventos_registrados)
        self.gestor_inventario = GestionInventario(self.inventario)

    def menu(self):
        while True:
            print("\nIngrese la opcion sobre la que desea interactuar")
            print("1. Huespedes")
            print("2. Empleados")
            print("3. Evento")
            print("4. Inventario")
            print("5. Salir")
            opcion = input("Selecciona una opcion: ")
            
            if opcion == "1":
                self.gestor_huespedes.menu_huespedes()
            elif opcion == "2":
                self.gestor_empleados.menu_empleados()
            elif opcion == "3":
                self.gestor_eventos.menu_eventos()
            elif opcion == "4":
                self.gestor_inventario.menu_inventario()
            elif opcion == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    app = Main()
    app.menu()