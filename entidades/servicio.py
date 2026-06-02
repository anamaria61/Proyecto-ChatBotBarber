class Servicio:
    def __init__(self, nombre: str, descripcion: str, duracion_minutos: int, precio: float):
        self._id = None
        self._nombre = nombre
        self._descripcion = descripcion
        self._duracion_minutos = duracion_minutos
        self._precio = precio

    @property
    def nombre(self) -> str:
        return self._nombre

    @property.setter 
    def nombre(self, valor: str):
        if not valor:
            raise ValueError("El nombre del serviciono puede estar vacío")
        self._nombre = valor

    @property
    def precio(self) -> float:
        return self._precio

    @property.setter
    def precio(self, valor: float):
        if valor <0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor

    @property
    def duracion_minutos(self) -> int:
        return self._duracion_minutos

    def __str__(self) -> str:
        return f"{self._nombre} - ${self._precio:.2f}  ({self._duracion_minutos} min)"
