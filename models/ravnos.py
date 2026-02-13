from models.vampiro import Vampiro

class Ravnos(Vampiro):

    def __init__(self, nombre, generacion, humanidad=7):
        super().__init__(nombre, generacion, humanidad)
        self.engaño = 5

    def usar_disciplina(self):
        self.engaño += 3
        print(f"{self.nombre} usa Quimerismo. Engaño {self.engaño}")

    def debilidad_clan(self):
        print(f"{self.nombre} siente compulsión por mentir")
