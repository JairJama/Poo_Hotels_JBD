

class Evento:
    def __init__(self, nombre_evento, fecha_evento, duracion, evento_ID):
        self._fecha_evento = fecha_evento
        self._duracion = duracion
        self._nombre_evento = nombre_evento
        self._evento_id = evento_ID
        
    @property
    def fecha_evento(self):
        return self._fecha_evento

    @fecha_evento.setter
    def fecha_evento(self, value):
        self._fecha_evento = value

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, value):
        self._duracion = value

    @property
    def nombre_evento(self):
        return self._nombre_evento

    @nombre_evento.setter
    def nombre_evento(self, value):
        self._nombre_evento = value

    @property
    def evento_id(self):
        return self._evento_id

    @evento_id.setter
    def evento_id(self, value):
        self._evento_id = value
        
    def agregar_evento(self):
        print(f"El evento agregado es {self.evento_id}: {self.nombre_evento} con una duración de {self.duracion} para la fecha {self.fecha_evento}.")

    def modificar_evento(self):
        print(f"El evento modificado ahora es {self.evento_id}: {self.nombre_evento} con una duración de {self.duracion} para la fecha {self.fecha_evento}.")