from typing import List
from entidades.usuario import Usuario

class Cliente(Usuario):
    def __init__(self, nombre: str, email: str, telefono: str,
                nombre_usuario: str, contrasena: str):
        super().__init__(nombre, email, telefono, nombre_usuario, contrasena)
        self._citas_realizadas = []

#Propiedades adicionales
@property
def obtener_rol(self) -> str:
    """Implementación del método abstracto"""
    return "Cliente"

def obtener_permiso(self) -> List[str]:
    return [
        "agendar_cita",
        "reprogramar_cita",
        "cancelar_cita",
        "consultar_disponibilidad",
        "ver_historial",
        "enviar_pqr"
    ]

def agregar_cita(self, cita):
    self._citas_realizadas.append(cita)

def ver_historial(self) -> List:
    return self._citas_realizadas.copy()

def __str__(self) -> str:
    return f"Cliente: {self._nombre_usuario}"
