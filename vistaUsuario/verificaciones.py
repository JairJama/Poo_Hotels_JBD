from datetime import datetime   

class VerificadorReservas():
    @staticmethod
    def habitacion_disponible(habitacion, reservas):
        for reserva in reservas:
            if reserva.numero_habitacion == habitacion and reserva.activa:
                return False
        return True
    
class VerificadorFecha:
    def __init__(self):
        pass
    
    def solicitar_fecha(self, mensaje):
        while True:
            fecha_str = input(mensaje + " (formato: DD/MM/YYYY): ")
            try:
                fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
                if fecha < datetime.now():
                    print("La fecha no puede ser en el pasado. Inténtalo de nuevo.")
                else:
                    return fecha
            except ValueError:
                print("Formato de fecha inválido. Inténtalo de nuevo.")

class VerificacionDatos:
    
    def verificar_entero(self, mensaje):
        while True:
            valor = input(mensaje)
            try:
                valor_entero = int(valor)
                return valor_entero
            except ValueError:
                print("Por favor, ingrese un número válido.")

    def verificar_cadena(self, mensaje):
        while True:
            valor = input(mensaje)
            if valor.isalpha():
                return valor
            else:
                print("Por favor, ingrese solo letras.")