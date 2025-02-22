# #self = this(c#, Java)

# class pessoa:
#     def __init__(self, nome:str, idade:int):
#         self.nome = nome
#         self.idade = idade
        
#     def aniversário(self):
#         self.idade += 1
#         print(f"Feliz aniversário !")
        
#     def cumprimentar(self):
#         print(f"Ola {self.nome} como vai? você tem {self.idade} anos de idade")
        
# people = pessoa("Vitor", 10)
# people.cumprimentar()
# people.aniversário()
# people.cumprimentar()


# class pessoa:
#     populacao:int = 0
#     def __init__(self, nome:str):
#         self.nome = nome
#         pessoa.populacao += 1
        
#     @classmethod
#     def mostrarPopulacao(cls):
#         print(f"População atual é {cls.populacao}")
        
# people1 = pessoa("Vitor")
# people1 = pessoa.mostrarPopulacao()


# class somar:
#     @staticmethod
#     def somar(a:int, b:int):
#         result:int = a + b
#         print(result)
        
# calcular = somar.somar(5,10)


class Conta_bancaria:
    saldo_conta:int = 0
    total_contas = 0
    def __init__(self):
        self.taxa_juros = 0
        Conta_bancaria.total_contas += 1

    @classmethod
    def depositar(cls, valor:int):
        if(cls.saldo_conta >= 0):
            cls.saldo_conta += valor
            print("Valor depositado com sucesso")
        else:
            print("O valor não pode ser depositado com sucesso")

    @classmethod
    def sacar(cls):
        def Saacar(dinheiro:int):
            cls.saldo_conta -= dinheiro
            if(cls.saldo_conta < 0):
                cls.saldo_conta = dinheiro;
                if(cls.saldo_conta < 0 ):
                    cls.saldo_conta = 0
                print("Saldo insuficiente")

        pergunta = int(input("Qual valor a ser sacado? (valor minímo de 25R$)"))
        if(pergunta):
            if(pergunta < cls.saldo_conta):
                if(pergunta >= 0 and pergunta >= 25):
                    Saacar(pergunta)
            else:
                print("Valor inválido")
            

    def verificar_saldo(cls):
        print(f"Seu saldo atual é de {cls.saldo_conta}")

    def ajustar_taxa_juros(self, taxa:float):
        if(taxa > 0):
            self.taxa_juros = taxa
        else:
            print("Valor inválido, a taxa precisa ser positiva")

    def mostrar_total_contas(self):
        print(f"O total de contas é de {self.total_contas}")

conta = Conta_bancaria()
conta.depositar(100)
conta.verificar_saldo()
conta.sacar()
conta.verificar_saldo()
conta.mostrar_total_contas()
conta.ajustar_taxa_juros(0.5)