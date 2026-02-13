from abc import ABC, abstractmethod

class Vampiro(ABC):

    def __init__(self, nombre, generacion, humanidad=7):
        self.nombre = nombre
        self.generacion = generacion
        self.__humanidad = humanidad
        self.__salud = 100
        self.__hambre = 0

    @abstractmethod
    def usar_disciplina(self):
        pass

    @abstractmethod
    def debilidad_clan(self):
        pass

    def presentarse(self):
        print(f"{self.nombre} / Generación: {self.generacion} / Humanidad: {self.__humanidad}")

    def alimentarse(self, puntos):
        self.__hambre -= puntos
        if self.__hambre < 0:
            self.__hambre = 0
        print(f"{self.nombre} reduce su hambre a {self.__hambre}")

    def cazar(self):
        self.__hambre += 2
        if self.__hambre > 10:
            self.__hambre = 10
        print(f"{self.nombre} ahora tiene hambre {self.__hambre}")

    def recibir_danio(self, puntos):
        self.__salud -= puntos
        if self.__salud < 0:
            self.__salud = 0
        print(f"{self.nombre} salud actual {self.__salud}")

    def esta_vivo(self):
        return self.__salud > 0

    def get_humanidad(self):
        return self.__humanidad

    def set_humanidad(self, valor):
        if 0 <= valor <= 10:
            self.__humanidad = valor

    @staticmethod
    def la_mascarada():
        print("La Mascarada debe mantenerse intacta.")
