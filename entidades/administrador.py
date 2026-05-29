from typing import List
from entidades.usuario import Usuario


class Administrador(Usuario):
    def __init__(self, nombre: str, email: str, telefono: str,
                 nombre_usuario: str, contrasena: str):
        super().__init__(nombre, email, telefono, nombre_usuario, contrasena)

def obtener_rol(self) -> str:
    return "Administrador"

def obtner_permisos(self) -> List[str]:
    return [
        "gestionar_servicios",
        "gestionar_barbero",
        "gestionar_clientes",
        "ver_reportes",
        "configurar_chatbot",
        "importar",
        "exportar"
    ]

def gestionar_servicio(self, servicio, accion: str) -> None:
    if accion == "añadir":
        print(f"Servicio '{servicio.nombre}' añadido")
    elif accion == "modificar":
        print(f"Servicio '{servicio.nombre}' modificado")
    elif accion == "eliminar":
        print(f"Servicio '{servicio.nombre}' eliminado")

def ver_reportes(self) -> None:
    print("Generando reportes del sistema")

def __str__(self) -> str:
    return f"Administrador: {self._nombre_usuario}"
