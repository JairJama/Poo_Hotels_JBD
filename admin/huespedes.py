


class Huespedes:
    def __init__(self, nombre, apellido, telefono):
        self._nombre = nombre
        self._apellido = apellido
        self._telefono = telefono
        self.lista_huespedes = []  

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def telefono(self):
        return self._telefono

    def registrar_huesped(self, nombre, apellido, telefono):
        nuevo_huesped = Huespedes(nombre, apellido, telefono)
        self.lista_huespedes.append(nuevo_huesped)
        print(f"Huésped registrado: {nuevo_huesped.nombre} {nuevo_huesped.apellido}, Teléfono: {nuevo_huesped.telefono}")

    def mostrar_huespedes(self):
        if len(self.lista_huespedes) > 0:
            print("\nHuéspedes registrados:")
            for i, huesped in enumerate(self.lista_huespedes, 1):
                print(f"{i}. {huesped.nombre} {huesped.apellido}, Teléfono: {huesped.telefono}")
            return True
        else:
            print("No hay huéspedes registrados.")
            return False

    def actualizar_huesped(self, indice, campo, nuevo_valor):
        """
        Actualiza la información de un huésped específico
        campo: 1 = nombre, 2 = apellido, 3 = teléfono
        """
        try:
            if 0 <= indice < len(self.lista_huespedes):
                huesped = self.lista_huespedes[indice]
                
                if campo == 1:
                    huesped._nombre = nuevo_valor
                elif campo == 2:
                    huesped._apellido = nuevo_valor
                elif campo == 3:
                    huesped._telefono = nuevo_valor
                
                print(f"\nHuésped actualizado: {huesped.nombre} {huesped.apellido}, Teléfono: {huesped.telefono}")
                return True
            else:
                print("\nÍndice de huésped no válido")
                return False
        except Exception as e:
            print(f"\nError al actualizar huésped: {str(e)}")
            return False


class Empleado(Huespedes):
    def __init__(self, nombre, apellido, telefono, IdEmpleado, Horario, puesto):
        super().__init__(nombre, apellido, telefono)  
        self._IdEmpleado = IdEmpleado
        self._puesto = puesto
        self._Horario = Horario
        self.lista_empleados = [] 

    @property
    def IdEmpleado(self):
        return self._IdEmpleado

    @property
    def Horario(self):
        return self._Horario

    @property
    def puesto(self):
        return self._puesto

    def registrar_empleado(self, nombre, apellido, telefono, IdEmpleado, Horario, puesto):
        nuevo_empleado = Empleado(nombre, apellido, telefono, IdEmpleado, Horario, puesto)
        self.lista_empleados.append(nuevo_empleado)  
        print(f"El Empleado registrado es {nuevo_empleado.nombre} {nuevo_empleado.apellido}, Teléfono: {nuevo_empleado.telefono}, ID= {nuevo_empleado.IdEmpleado}")

    def mostrar_empleados(self):
        if len(self.lista_empleados) > 0:
            print("\nEmpleados registrados:")
            for i, empleado in enumerate(self.lista_empleados, 1):
                print(f"{i}. {empleado.nombre} {empleado.apellido}")
                print(f"   ID: {empleado.IdEmpleado}")
                print(f"   Teléfono: {empleado.telefono}")
                print(f"   Puesto: {empleado.puesto}")
                print(f"   Horario: {empleado.Horario}")
            return True
        else:
            print("No hay empleados registrados.")
            return False

    def actualizar_informacion_empleado(self, IdEmpleado, campo, nuevo_valor):
        try:
            empleado = next((e for e in self.lista_empleados if e.IdEmpleado == IdEmpleado), None)
            if empleado:
                if campo == 1:
                    empleado._nombre = nuevo_valor
                elif campo == 2:
                    empleado._apellido = nuevo_valor
                elif campo == 3:
                    empleado._telefono = nuevo_valor
                elif campo == 4:
                    empleado._puesto = nuevo_valor
                
                print(f"\nEmpleado actualizado:")
                print(f"Nombre: {empleado.nombre} {empleado.apellido}")
                print(f"ID: {empleado.IdEmpleado}")
                print(f"Teléfono: {empleado.telefono}")
                print(f"Puesto: {empleado.puesto}")
                return True
            else:
                print("\nEmpleado no encontrado")
                return False
        except Exception as e:
            print(f"\nError al actualizar empleado: {str(e)}")
            return False