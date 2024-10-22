from datetime import datetime
class Facturacion:
    def __init__(self, nombre_cliente, apellido_cliente, numero_habitacion, fecha_entrada, fecha_salida, tarifa_diaria):
        self.nombre_cliente = nombre_cliente
        self.apellido_cliente = apellido_cliente
        self.numero_habitacion = numero_habitacion
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.tarifa_diaria = tarifa_diaria
        self.activa = True

    def calcular_total(self, fecha_entrada, fecha_salida, tarifa_diaria):
        dias = (fecha_salida - fecha_entrada).days
        return dias * tarifa_diaria

    def mostrar_detalle_reserva(self, nombre_cliente, apellido_cliente, numero_habitacion, 
                                fecha_entrada, fecha_salida, tarifa_diaria, activa):
        total = self.calcular_total(fecha_entrada, fecha_salida, tarifa_diaria)
        detalle = f"""
        Detalle de la Reserva:
        ---------------------
        Cliente: {nombre_cliente} {apellido_cliente} 
        Habitación: {numero_habitacion}
        Fecha de Entrada: {fecha_entrada.strftime('%d/%m/%Y')}
        Fecha de Salida: {fecha_salida.strftime('%d/%m/%Y')}
        Tarifa Diaria: ${tarifa_diaria:.2f}
        Total a Pagar: ${total:.2f}
        Estado: {'Activa' if activa else 'Cancelada'}
        """
        return detalle

    def generar_factura(self, nombre_cliente, apellido_cliente, numero_habitacion, 
                        fecha_entrada, fecha_salida, tarifa_diaria):
        total = self.calcular_total(fecha_entrada, fecha_salida, tarifa_diaria)
        iva = total * 0.15
        total_con_iva = total + iva
        factura = f"""
        FACTURA
        -------
        Cliente: {nombre_cliente} {apellido_cliente}
        Detalle:
        - Alojamiento en habitación {numero_habitacion}
        - Desde: {fecha_entrada.strftime('%d/%m/%Y')}
        - Hasta: {fecha_salida.strftime('%d/%m/%Y')}
        
        Subtotal: ${total:.2f}
        IVA (15%): ${iva:.2f}
        Total: ${total_con_iva:.2f}
        """
        return factura

    def cancelar_reserva(self, apellido_cliente, nombre_cliente, numero_habitacion):
        self.activa = False
        # Usamos los parámetros recibidos para mantener la consistencia con la firma del método
        return f"La reserva para {apellido_cliente}, {nombre_cliente} en la habitación {numero_habitacion} ha sido cancelada."

    def modificar_reserva(self, nombre_cliente, apellido_cliente, numero_habitacion, 
                    fecha_entrada, fecha_salida):
        print("¿Qué desea modificar?")
        print("1. Nombre del cliente")
        print("2. Apellido del cliente")
        print("3. Número de habitación")
        print("4. Fecha de entrada")
        print("5. Fecha de salida")
        print("6. Volver al menú principal")
        
        op_mod = int(input("Escoja una opción: "))
        
        if op_mod == 1:
            self.nombre_cliente = input("Ingrese el nuevo nombre: ")
            nombre_cliente = self.nombre_cliente
        elif op_mod == 2:
            self.apellido_cliente = input("Ingrese el nuevo apellido: ")
            apellido_cliente = self.apellido_cliente
        elif op_mod == 3:
            self.numero_habitacion = int(input("Ingrese el nuevo número de habitación: "))
            numero_habitacion = self.numero_habitacion
        elif op_mod == 4:
            nueva_fecha = input("Ingrese la nueva fecha de entrada (DD/MM/YYYY): ")
            self.fecha_entrada = datetime.strptime(nueva_fecha, "%d/%m/%Y")
            fecha_entrada = self.fecha_entrada
        elif op_mod == 5:
            nueva_fecha = input("Ingrese la nueva fecha de salida (DD/MM/YYYY): ")
            self.fecha_salida = datetime.strptime(nueva_fecha, "%d/%m/%Y")
            fecha_salida = self.fecha_salida
        elif op_mod == 6:
            return "Volviendo al menu principal..."
        else:
            return "Opcion invalida."
        
        # Actualizar los atributos con los valores posiblemente modificados
        self.nombre_cliente = nombre_cliente
        self.apellido_cliente = apellido_cliente
        self.numero_habitacion = numero_habitacion
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        
        return "Reserva modificada exitosamente."