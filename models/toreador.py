from models.vampiro import Vampiro

class Toreador(Vampiro):

    def __init__(self, nombre, generacion, humanidad=7):
        super().__init__(nombre, generacion, humanidad)
        self.inspiracion = 5

    def usar_disciplina(self):
        self.inspiracion += 2
        print(f"{self.nombre} usa Presencia. Inspiración {self.inspiracion}")

    def debilidad_clan(self):
        print(f"{self.nombre} se distrae con la belleza extrema")
