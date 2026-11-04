#atividade veiculos

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False
        self.ligado = True
        print(f"{self.marca} {self.modelo} ligado.")
        estado = "ligado" if self.ligado else "desligado"
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Estado: {estado}")
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas
        print(f"Porta-malas do {self.marca} {self.modelo} aberto.")
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas
        if self.ligado:
            print(f"A {self.marca} {self.modelo} está empinando!")
        else:
            print(f"Não é possível empinar: a {self.marca} {self.modelo} está desligada.")
    carro = Carro("Toyota", "Corolla", 4)
    moto = Moto("Honda", "CB 500", 500)
    carro.mostrar_info()
    carro.ligar()
    carro.mostrar_info()
    carro.abrir_porta_malas()
    moto.mostrar_info()
    moto.empinar()  # A moto está desligada, então a ação não acontece.
    moto.ligar()
    moto.mostrar_info()
    moto.empinar()
    main()
if __name__ == "__main__":
    print("\n=== Moto ===")
    print("=== Carro ===")
def main():
class Carro(Veiculo):
    def abrir_porta_malas(self):
        print("Porta-malas aberto.")
class Carro(Veiculo):
    def mostrar_info(self):
    def ligar(self):
    def __init__(self, marca, modelo):



#atividade 2

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print(f"Olá, eu sou {self.nome} e tenho {self.idade} anos.")

    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.notas = []
        self.notas.append(nota)
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        print(f"Prof. {self.nome} está dando aula de {self.disciplina}.")

    aluno = Aluno("Lucas", 17, "2026001")
    professor = Professor("Helena", 35, "Python")
    aluno.apresentar()
    aluno.adicionar_nota(8.5)
    aluno.adicionar_nota(9.0)
    aluno.adicionar_nota(7.5)
    print(f"Média das notas: {aluno.media():.2f}")
    professor.apresentar()
    professor.dar_aula()
    main()


if __name__ == "__main__":
    print("\n=== Professor ===")
    print("=== Aluno ===")


def main():
    def dar_aula(self):


class Professor(Pessoa):
    def media(self):
        def adicionar_nota(self, nota):


class Aluno(Pessoa):
    def apresentar(self):