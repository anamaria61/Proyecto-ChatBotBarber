from enum import Enum


class EstadoCita(Enum):

    """Estados posibles de una cita."""

    PENDIENTE = "Pendiente"
    CONFIRMADA = "Confirmada"
    COMPLETADA = "Completada"
    CANCELADA = "Cancelada"


class TipoNotificacion(Enum):

    """Tipos de notificaciones."""

    CONFIRMACION = "Confirmación"
    CANCELACION = "Cancelación"


class TipoPQR(Enum):

    """Tipos de Peticiones, Quejas, Reclamos."""

    PETICION = "Petición"
    QUEJA = "Queja"
    RECLAMO = "Reclamo"
    SUGERENCIA = "Sugerencia"