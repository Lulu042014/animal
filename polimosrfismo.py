class Animal:
    def __init__(self, nome):
        self.nome = nome

    def som(self):
        return "Som de animal genérico"

    def __str__(self):
        return f"{self.__class__.__name__} - Nome: {self.nome}"


class Mamifero(Animal):
    def __init__(self, nome, pelo=True):
        super().__init__(nome)
        self.pelo = pelo

    def som(self):
        return "Som de mamífero"

    def caracteristicas(self):
        return f"Possui pelo: {'Sim' if self.pelo else 'Não'}"


class Ave(Animal):
    def __init__(self, nome, voa=True):
        super().__init__(nome)
        self.voa = voa

    def som(self):
        return "Som de ave"

    def caracteristicas(self):
        return f"Pode voar: {'Sim' if self.voa else 'Não'}"


class Cachorro(Mamifero):
    def som(self):
        return "Latido"


class Gato(Mamifero):
    def som(self):
        return "Miado"


class Papagaio(Ave):
    def som(self):
        return "Fala"


# Criando instâncias das classes
animais = [
    Cachorro("Rex"),
    Gato("Mia"),
    Papagaio("Louro"),
    Mamifero("Elefante"),
    Ave("Pinguim")
]

# Exibindo informações e sons dos animais
for animal in animais:
    print(f"{animal} faz: {animal.som()}")
    if isinstance(animal, Mamifero):
        print(animal.caracteristicas())
    elif isinstance(animal, Ave):
        print(animal.caracteristicas())
    print("-" * 30)
