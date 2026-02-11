class animals():
    def __init__(self, name):
        self.name = name

    def sleeping(self):
        print(f"{self.name} is sleeping")


class mamal(animals):
    def birth(self):
        print(f"{self.name} give birth automatally")

class reptiles(animals):
    def birth1(self):
        print(f"{self.name} lay eggs")


class crocodiles(reptiles):
    pass

class Fish(reptiles, mamal):
    pass


croco = crocodiles("Joey")
fish = Fish("Michelle")

fish.birth()
croco.birth1()
croco.sleeping()








