from models.vampiro import Vampiro

class Brujah(Vampiro):

    def __init__(self, nombre, generacion, humanidad=7):
        super().__init__(nombre, generacion, humanidad)
        self.furia = 5

    def usar_disciplina(self):
        self.furia += 1
        print(f"{self.nombre} usa Potencia. Furia actual {self.furia}")

    def debilidad_clan(self):
        print(f"{self.nombre} puede entrar en frenesí fácilmente")
