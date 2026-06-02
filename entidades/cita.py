from datetime import datetime, timedelta
from typing import Optional
from utilidades.estados_tipos import EstadoCita

class Cita:
    def __init__(self, cliente, barbero, servicio, fecha_hora: datetime):
        self._id = None
        self._cliente = cliente
        self._barbero = barbero
        self._servicio = servicio
        self._fecha_hora = fecha_hora
        self._duracion_minutos = servicio.duracion_minutos
        self._estado = EstadoCita.PENDIENTE
        self._fecha_creacion = datetime.now()
        self._fecha_modificacion = datetime.now()

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, valor: int):
        self._id = valor

    @property
    def fecha_hora(self) -> datetime:
        return self._fecha_hora
    
    @property 
    def estado(self) -> EstadoCita:
        return self._estado
    
    @property
    def cliente(self):
        return self._cliente
    
    @property 
    def barber(self):
        return self._barbero
    
    def confirmar(self) -> None:
        if self._estado == EstadoCita.PENDIENTE:
            self._estado = EstadoCita.CONFIRMADA
            self._fecha_modificacion = datetime.now()
            print(f"Cita confirmada para {self._fecha_hora}")
    
