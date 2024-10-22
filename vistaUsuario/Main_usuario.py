from datetime import datetime
from .verificaciones import VerificadorReservas, VerificadorFecha, VerificacionDatos
from .Facturacion import Facturacion

class Main:
    def __init__(self):
        self.reservas = []

    def mostrar_menu(self):
        print("HOTEL MANABITA")
        print("1. Crear nueva reserva")
        print("2. Modificar Reserva")
        print("3. Cancelar Reserva")
        print("4. Detalles de mis reservas")
        print("5. Salir")

    def crear_reserva(self):
        verificador = VerificacionDatos()

        habitacion_disponible = False
        while not habitacion_disponible:
            habitacion = verificador.verificar_entero("Ingrese el número de su habitación: ")
            if VerificadorReservas.habitacion_disponible(habitacion, self.reservas):
                habitacion_disponible = True
            else:
                print("La habitación ya está reservada por otro usuario. Por favor, elija otra habitación.")

        nombre = verificador.verificar_cadena("Ingrese su nombre: ")
        apellido = verificador.verificar_cadena("Ingrese su apellido: ")
        validador = VerificadorFecha()
        fecha_entrada = validador.solicitar_fecha("Ingrese la fecha de entrada")
        fecha_salida = validador.solicitar_fecha("Ingrese la fecha de salida")

        print("--------------------------------------------------------")
        reserva = Facturacion(nombre, apellido, habitacion, fecha_entrada, fecha_salida, tarifa_diaria=20)
        # Aquí está el cambio - pasamos los argumentos necesarios
        total = reserva.calcular_total(fecha_entrada, fecha_salida, reserva.tarifa_diaria)
        print(f"Total calculado: ${total:.2f}")
        # También debemos pasar los argumentos para generar_factura
        print(reserva.generar_factura(nombre, apellido, habitacion, fecha_entrada, fecha_salida, reserva.tarifa_diaria))
        self.reservas.append(reserva)

    def modificar_reserva(self):
        numHabitacion = int(input("Ingrese el número de habitación reservada que desea modificar: "))
        reserva_encontrada = False
        for reserva in self.reservas:
            if reserva.numero_habitacion == numHabitacion and reserva.activa:
                # Pasamos todos los parámetros requeridos
                resultado = reserva.modificar_reserva(
                    reserva.nombre_cliente,
                    reserva.apellido_cliente,
                    reserva.numero_habitacion,
                    reserva.fecha_entrada,
                    reserva.fecha_salida
                )
                print(resultado)
                reserva_encontrada = True
                break
        if not reserva_encontrada:
            print("Reserva no encontrada o ya cancelada.")

    def cancelar_reserva(self):
        numHabitacion = int(input("Ingrese el número de habitación de la reserva que desea cancelar: "))
        reserva_encontrada = False
        for reserva in self.reservas:
            if reserva.numero_habitacion == numHabitacion and reserva.activa:
                # Pasamos los parámetros requeridos
                resultado = reserva.cancelar_reserva(
                    reserva.apellido_cliente,
                    reserva.nombre_cliente,
                    reserva.numero_habitacion
                )
                print(resultado)
                reserva_encontrada = True
                break
        if not reserva_encontrada:
            print("Reserva no encontrada o ya cancelada.")

    def mostrar_detalles_reservas(self):
        if self.reservas:
            for i, reserva in enumerate(self.reservas, 1):
                if reserva.activa:
                    print(f"\nReserva {i}:")
                    print(reserva.mostrar_detalle_reserva(
                        reserva.nombre_cliente,
                        reserva.apellido_cliente,
                        reserva.numero_habitacion,
                        reserva.fecha_entrada,
                        reserva.fecha_salida,
                        reserva.tarifa_diaria,
                        reserva.activa
                    ))
        else:
            print("No hay reservas registradas.")

    def ejecutar(self):
        op = None
        while op != 5:
            self.mostrar_menu()
            op = int(input("Escoja una opción: "))

            if op == 1:
                self.crear_reserva()
            elif op == 2:
                self.modificar_reserva()
            elif op == 3:
                self.cancelar_reserva()
            elif op == 4:
                self.mostrar_detalles_reservas()
            elif op == 5:
                print("Gracias por usar nuestro sistema de reservas. ¡Hasta pronto!")
            else:
                print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main = Main()
    main.ejecutar()