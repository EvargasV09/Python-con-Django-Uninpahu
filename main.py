from models.brujah import Brujah
from models.toreador import Toreador
from models.ravnos import Ravnos
from models.vampiro import Vampiro


def main():
    vampiro1 = Brujah("Darius", 10)
    vampiro2 = Toreador("Isabella", 9)
    vampiro3 = Ravnos("Arjun", 11)

    vampiros = [vampiro1, vampiro2, vampiro3]

    for vampiro in vampiros:
        vampiro.presentarse()
        vampiro.usar_disciplina()
        print("-----")

    Vampiro.la_mascarada()


if __name__ == "__main__":
    main()
