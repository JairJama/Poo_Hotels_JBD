from .verificaciones_admin import Verificaciones
from .evento import Evento

class GestionEventos:
    def __init__(self, eventos_registrados):
        self.eventos_registrados = eventos_registrados

    def menu_eventos(self):
        while True:
            print("\nIngrese la operación a realizar:")
            print("1. Asignar evento")
            print("2. Modificar evento")
            print("3. Volver al menú principal")
            opcion = input("Seleccione una opción (1-3): ")
            if opcion == "1":
                self.asignar_evento()
            elif opcion == "2":
                self.modificar_evento()
            elif opcion == "3":
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")

    def asignar_evento(self):
        nombre_evento = Verificaciones.pedir_cadena_valida("Ingrese el nombre del evento: ")
        while True:
            fecha_evento = input("Ingrese la fecha del evento: ")
            eventin = next((e for e in self.eventos_registrados if e.fecha_evento == fecha_evento), None)
            if eventin:
                print("Ya hay un evento asignado a esa fecha. Por favor, ingrese otra fecha.")
            else:
                break
        duracion = input("Ingrese la duración del evento: ")
        evento_ID = input("Ingrese el ID del evento: ")
        eventop = Evento(nombre_evento, fecha_evento, duracion, evento_ID)
        self.eventos_registrados.append(eventop)
        eventop.agregar_evento()

    def modificar_evento(self):
        if self.eventos_registrados:
            evento_id = input("Ingrese el ID del evento que desea modificar: ")
            evento = next((e for e in self.eventos_registrados if e.evento_id == evento_id), None)
            if evento:
                print("Seleccione el campo a modificar:")
                print("1. Nombre del evento")
                print("2. Fecha del evento")
                print("3. Duración del evento")
                opcion = input("Seleccione una opción (1-3): ")
                if opcion == "1":
                    evento.nombre_evento = input("Ingrese el nuevo nombre del evento: ")
                elif opcion == "2":
                    evento.fecha_evento = input("Ingrese la nueva fecha del evento (YYYY-MM-DD): ")
                elif opcion == "3":
                    evento.duracion = input("Ingrese la nueva duración del evento: ")
                else:
                    print("Opción no válida.")
                evento.modificar_evento()
            else:
                print("Evento no encontrado.")
        else:
            print("No hay eventos registrados.")