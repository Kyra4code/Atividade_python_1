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


class somar:
    @staticmethod
    def somar(a:int, b:int):
        result:int = a + b
        print(result)
        
calcular = somar.somar(5,10)