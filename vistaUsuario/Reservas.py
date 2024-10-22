from datetime import datetime

from datetime import datetime

class Reservas():
    def __init__(self, habitacion, huesped, apeHuesped, fecha_inicio, fecha_fin):
        self._habitacion = habitacion
        self._huesped = huesped
        self._apeHuesped = apeHuesped
        self._fecha_inicio = fecha_inicio
        self._fecha_fin = fecha_fin
        self._activa = True 

    # Getters
    def get_habitacion(self):
        return self._habitacion

    def get_huesped(self):
        return self._huesped

    def get_apeHuesped(self):
        return self._apeHuesped

    def get_fecha_inicio(self):
        return self._fecha_inicio

    def get_fecha_fin(self):
        return self._fecha_fin

    def is_activa(self):
        return self._activa

    # Setters
    def set_habitacion(self, habitacion):
        self._habitacion = habitacion

    def set_huesped(self, huesped):
        self._huesped = huesped

    def set_apeHuesped(self, apeHuesped):
        self._apeHuesped = apeHuesped

    def set_fecha_inicio(self, fecha_inicio):
        self._fecha_inicio = fecha_inicio

    def set_fecha_fin(self, fecha_fin):
        self._fecha_fin = fecha_fin

    def set_activa(self, activa):
        self._activa = activa

    def crear_reserva(self, habitacion, huesped, apeHuesped, fecha_inicio, fecha_fin):
        print(f"Número de habitación: {habitacion}")
        print(f"Huésped: {apeHuesped}, {huesped}")
        print(f"Fecha de entrada: {fecha_inicio.strftime('%d/%m/%Y')}")
        print(f"Fecha de salida: {fecha_fin.strftime('%d/%m/%Y')}")

    def modificar_reserva(self, habitacion, huesped, apeHuesped, fecha_inicio, fecha_fin):
        print("¿Qué desea modificar?")
        print("1. Nombre del huésped")
        print("2. Apellido del huésped")
        print("3. Número de habitación")
        print("4. Fecha de entrada")
        print("5. Fecha de salida")
        print("6. Menú principal")
        op_mod = None
        while op_mod != 6:
            op_mod = int(input("Escoja una opción: "))
            if op_mod == 1:
                huesped = input("Ingrese el nuevo nombre: ")
                self.set_huesped(huesped)
                print("Nombre del huésped actualizado con éxito.")
            elif op_mod == 2:
                apeHuesped = input("Ingrese el nuevo apellido: ")
                self.set_apeHuesped(apeHuesped)
                print("Apellido del huésped actualizado con éxito.")
            elif op_mod == 3:
                habitacion = int(input("Ingrese el nuevo número de habitación: "))
                self.set_habitacion(habitacion)
                print("Número de habitación actualizado con éxito.")
            elif op_mod == 4:
                fecha_inicio = ingresar_fecha("entrada")
                fecha_fin = ingresar_fecha("salida", fecha_inicio)
                self.set_fecha_inicio(fecha_inicio)
                self.set_fecha_fin(fecha_fin)
                print("Fechas actualizadas.")
            elif op_mod == 5:
                fecha_fin = ingresar_fecha("salida", self.get_fecha_inicio())
                self.set_fecha_fin(fecha_fin)
                print("Fecha de salida actualizada.")
            elif op_mod == 6:
                print("Regresando al menú principal...")
                break
            else:
                print("Opción inválida, por favor intente de nuevo.")
            self.crear_reserva(self.get_habitacion(), self.get_huesped(), self.get_apeHuesped(), self.get_fecha_inicio(), self.get_fecha_fin())
        
    def cancelar_reserva(self, habitacion, huesped, apeHuesped):
        self.set_activa(False)
        print(f"La reserva para {apeHuesped}, {huesped} en la habitación {habitacion} ha sido cancelada.")

def ingresar_fecha(tipo_fecha, fecha_inicio=None):
    while True:
        fecha_str = input(f"Ingrese la fecha de {tipo_fecha} (dd/mm/yyyy): ")
        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            if tipo_fecha == "salida" and fecha_inicio and fecha <= fecha_inicio:
                print("La fecha de salida debe ser posterior a la fecha de entrada.")
            else:
                return fecha
        except ValueError:
            print("Formato de fecha incorrecto. Intente de nuevo.")