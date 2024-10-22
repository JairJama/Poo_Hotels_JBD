
from datetime import datetime

class Verificaciones:
    @staticmethod
    def fecha_existe(fecha, lista_fechas):
        """ Verifica si la fecha ingresada ya existe en una lista de fechas. """
        try:
            fecha_convertida = datetime.strptime(fecha, "%d/%m/%Y")
            
            for f in lista_fechas:
                if fecha_convertida == f:
                    print("Error: La fecha ya existe.")
                    return True  
            return False  
        except ValueError:
            print("Error: La fecha no es válida.")
            return False
    
    
    @staticmethod
    def verificar_str(valor):
            if isinstance(valor, str) and valor.strip() and valor.replace(" ", "").isalpha():
                return True
                
            else:
                print("Error: Ingrese un caracter válido.")
                return False
        
    def pedir_cadena_valida(mensaje):
        while True:
            valor = input(mensaje)
            if Verificaciones.verificar_str(valor):
                return valor  
            
    @staticmethod
    def verificar_int(valor):
        
        try:
            int(valor)
            if len(valor)==10:                
                return True
            else:
                print("Ingrese los 10 digitos del numero")
        except ValueError:
            print("Error: El valor debe ser un número entero.")
            return False
        
    
    def pedir_numero_valido(mensaje):
        while True:
            valor= input(mensaje)
            if Verificaciones.verificar_int(valor):
                return valor
    @staticmethod    
    def verificar_id(valor):
        while True:
            try:
                int(valor)  
                return True
            except ValueError:
                print("Error: El ID debe ser un número entero.")
                return False
    def pedir_ID_valido(mensaje):
        while True:
            valor= input(mensaje)
            if Verificaciones.verificar_id(valor):
                return valor