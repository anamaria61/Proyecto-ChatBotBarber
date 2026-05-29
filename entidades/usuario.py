from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional, List

class Usuario(ABC):
    def __init__(self, nombre: str, email: str, telefono: str, nombre_usuario: str, contrasena: str):
        self._id_usuario = None
        self._nombre = nombre
        self._email = email 
        self._telefono = telefono
        self._nombre_usuario = nombre_usuario
        self._contrasena_hash = self._hash_contrasena(contrasena)
        self._fecha_registro = datetime.now #obtiene la fecha y hora actual del sistema local

#Getters y Setters 
@property
def id_usuario(self):
    return self._id_usuario

@id_usuario.setter
def id_usurio(self, valor: int):
    self._id_usuario = valor

@property
def nombre(self):
    return self._nombre

@nombre.setter 
def nombre(self, valor: str):
    if not valor or len(valor.strip()) == 0:
        raise ValueError("EL nombre no puede estar vacío")
    self._nombre = valor

@property
def email(self):
    return self._email

@email.setter
def email(self, valor: str):
    if "@" not in valor or "." not in valor:
        raise ValueError("Email inválido")
    self._email = valor

def _hash_contrasena(self, contrasena: str) -> str:
    """Simula el hasheo de la contraseña"""
    import hashlib
    return hashlib.sha256(contrasena.encode()).hexdigest()

def verificar_contraseña(self, contrasena: str) -> bool:
    """Verifica si la contraseña es correcta"""
    return self._contrasena_hash == self._hash_contrasena(contrasena)


@abstractmethod
def obtener_rol(self) -> str:
    """Retorna el rol correspondiente del usuario"""
    pass

@abstractmethod
def obtener_permisos(self) -> List[str]:
    """Retorna la lista de permisos del usuario."""
    pass

def actualizar_perfil(self, nombre: str = None, email: str = None, telefono: str = None) -> None:
    """Actualiza los datos del perfil"""
    if nombre:
        self.nombre = nombre
    if email:
        self.email = email
    if telefono:
        self.telefono = telefono
    print(f"Perfil actualizado para {self._nombre_usuario}")

def __str__(self) -> str:
    return f"Usuario: {self._nombre_usuario} ({self.obtener_rol()})"