import sys
from vistaUsuario.Main_usuario import Main as UserMain
from admin.main_admin import Main as AdminMain

class MainSystem:
    def __init__(self):
        self.user_main = UserMain()
        self.admin_main = AdminMain()

    def display_menu(self):
        print("\nHOTEL MANABITA - SISTEMA PRINCIPAL")
        print("1. Acceso Usuario")
        print("2. Acceso Administrador")
        print("3. Salir")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Seleccione una opción: ")

            if choice == "1":
                print("\nAccediendo al sistema de usuario...")
                self.user_main.ejecutar()
            elif choice == "2":
                print("\nAccediendo al sistema de administrador...")
                self.admin_main.menu()
            elif choice == "3":
                print("Gracias por usar el sistema del Hotel Manabita. ¡Hasta pronto!")
                sys.exit(0)
            else:
                print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

if __name__ == "__main__":
    main_system = MainSystem()
    main_system.run()