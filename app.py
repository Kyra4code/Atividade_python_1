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
    taxa_juros = 0;
    total_contas = 0;

    def __init__(self, saldo_inicial:int, name:str):
        Conta_bancaria.total_contas += 1;
        self.saldo_conta:int = saldo_inicial;
        self.titular = name;
    
    def depositar(self, valor:int):
        if(self.saldo_conta >= 0):
            self.saldo_conta += valor
            print("Valor depositado com sucesso")
        else:
            print("O valor não pode ser depositado com sucesso")

    
    def sacar(self):
        def Saacar(dinheiro:int):
            if(dinheiro <= self.saldo_conta):
                self.saldo_conta -= dinheiro
                print(f"valor sacado é de {dinheiro}")
            else:
                print("Não foi possível sacar")


        pergunta = int(input("Qual valor a ser sacado? (valor minímo de 25R$) \n"))
        if(pergunta < self.saldo_conta):
            if(pergunta >= 0 and pergunta >= 25):
                Saacar(pergunta)
        else:
            print("Valor invalido")

    def verificar_saldo(self):
        print(f"Seu saldo atual é de {self.saldo_conta}")

    @classmethod
    def ajustar_taxa_juros(self, taxa:float):
        if(taxa > 0):
            self.taxa_juros = taxa
            print(f"Sua taxa de juros atual é de {cls.taxa_juros}")
        else:
            print("Valor inválido, a taxa precisa ser positiva")

    @classmethod
    def mostrar_total_contas(cls):
        print(f"O total de contas é de {Conta_bancaria.total_contas}")

    @staticmethod
    def converter_moeda(valor_normal:int, taxa_conversão:int):
        v1 = valor_normal;
        v2 = taxa_conversão;
        valor_convertido = (v1 * v2 / 100) * v1
        print(f"sua conversão deu: {valor_convertido}");

    @staticmethod
    def dias_no_ano():
        print("um ano tem 365");


conta = Conta_bancaria(5, "vitor");
conta.depositar(100);
conta.verificar_saldo();
conta.sacar();
conta.verificar_saldo();
conta.mostrar_total_contas();
conta2 = Conta_bancaria(0, "Jubileu");
conta.mostrar_total_contas();
conta.ajustar_taxa_juros(0.5);