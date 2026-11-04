# 1.Encapsulamento
# Proteger o salário para que so mude seguindo regras
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    # privado: dois sublinhado


def apresentar(self):
    print(f"Sou {self.nome} e ganho R${self.salario}")


# @property deixa ler o salario com se foesse um atributo

@property
def salario(self):
    return self.salario


def dar_aumento(self, porcentagem:):
    if porcentagem <= 0:
        print(f"Aumento invalido para {self.nome}")


      return

self.__salario = self.__salario * (1 + porcentagem / 100)
print(f"{self.nome} recebeu {porcentagem}% de aumento")

ana = Funcionario("ana", 3000)
ana.salario =
4000
print(ana.salario)
ana.apresentar()