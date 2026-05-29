from typing import List
from entidades.usuario import Usuario
from entidades.horario_laboral import HorarioLaboral

class Barbero(Usuario):
    def __init__(self, nombre: str, email: str, telefono: str,
                nombre_usuario: str, contrasena: str):
        super().__init__(nombre, email, telefono, nombre_usuario, contrasena)
        self._horario_laboral = HorarioLaboral()
        self._citas_asignadas = []
        self._citas_completadas = 0

@property
def horario_laboral(self) -> HorarioLaboral:
    return self._horario_laboral

def obtener_rol(self) -> str:
    return "Barbero"

def obtener_permisos(self) -> List[str]:
    """Implementación polimórfica"""
    return [
        "ver _agenda",
        "aceptar_cita",
        "rechazar_cita",
        "marcar_completada",
        "ver_clientes_atendidos",
        "configurar_horario"
    ]

def aceptar_cita(self, cita) -> None:
    cita.confirmar()
    print(f"{self._nombre} aceptó la cita para {cita.fecha_hora}")

def rechazar_cita(self, cita) -> None:
    cita.cancelar("Rechazada por Barbero")
    print(f"{self._nombre} rechazó la cita para {cita.fecha_hora}")

def marcar_completada(self, cita) -> None:
    if cita.completar():
        self._citas_completas += 1
        print(f"{self._nombre} completó una cita (Total: {self._citas_completadas})")

def ver_agenda(self) -> List:
    return self._citas_asignadas.copy()

def __str__(self) -> str:
    return f"Barbero: {self._nombre_usuario}"
