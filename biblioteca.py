class Pessoa:
    def __init__(self, nome, idade, peso, tipo):
        self.nome= nome
        self.peso= peso
        self.idade= idade
        self.sangue= tipo
        self.comendo = False
        self.dormindo = False
        self.falando = False

    def apresentar(self):
        print(f"olá! meu nome é {self.nome}, meu peso é {self.peso},"
              f" minha idade é  {self.idade} e meu tipo sanguíneo é {self.sangue}.")

    def comer(self,comida): #comer é uma função e não precisa colocar ali em cima que tem as características
        if self.comendo == True:
            print(f"{self.nome} Já está comendo")
        elif self.falando == True:
            print(f"{self.nome} não pode comer porque está falando ")
        elif self.dormindo == True:
            print(f"{self.nome} não pode comer nem falar agora porque está domindo")
        else:
            print(f"{self.nome} foi comer {comida}")
            self.comendo = True

    def nao_comer(self):
        if self.comendo == True:
            print(f"{self.nome} parou de comer")
            self.comendo = True

    def falar(self, amigos):
        if self.falando == True:
            print(f"{self.nome} Já está falando")
        elif self.falando == True:
            print(f"{self.nome} não pode falar porque está comendo ")
        elif self.falando == True:
            print(f"{self.nome} não pode falar agora porque está domindo")
        else:
            print(f"{self.nome} foi falar com {amigos}")
            self.falando = True

    def dormir (self):
        if self.dormindo == True:
            print(f"{self.nome} está dormindo")
        elif self.dormindo == True:
            print(f"{self.nome} não pode dormir porque está comendo ")
        elif self.dormindo == True:
            print(f"{self.nome} não pode falar nem comer agora porque está domindo")
        else:
            print(f"{self.nome} não pode dormir porque já está fazendo alguma coisa")
            self.dormindo = True

    def parou_dormir(self):
        print(f"{self.nome} parou de dormir")
        self.dormindo = True






