# def hello():#Tudo que esta dentro da identação, quando chamada ira ser executada!
#     print()
#     print("Ola!!!")
#     print("Voçe esta passando por um teste sobre (def), estou te testando e aprendendo como funciona")
#     print()
# hello()

#=====================================================================================================================

# def hello(nome):#Tudo que esta dentro da identação, quando chamada ira ser executada!
#     print()
#     print("Ola!!!", nome)
#     print("Voçe esta passando por um teste sobre (def), estou te testando e aprendendo como funciona")
#     print()
# hello("Ederson")

#===================================================================================================================

# def hello(nome):#Tudo que esta dentro da identação, quando chamada ira ser executada!
#     print()
#     print("Ola!!!", nome)
#     print()
# a = input("Digite algo: ")
# hello(a)

#=========================================================================================================

# def hello(nome):#Tudo que esta dentro da identação, quando chamada ira ser executada!
#     print()
#     print("Ola!!!", nome)
#     print("Voçe esta passando por um teste sobre (def), estou te testando e aprendendo como funciona")
#     print()
# hello("Ederson")
# hello("heinrich")
# hello("nana")

#================================================================================================================

# def hello(nome, idade):#Tudo que esta dentro da identação, quando chamada ira ser executada!
#     print()
#     print("Ola!!!", nome, "\nSua idade é: ", idade)
#     print()
# nome = input("Digite o nome: ")
# idade = int(input("Digite a idade"))
# hello(nome, idade)

#===================================================================================

# def calcular_pagamento(qtd_horas, valor_hora):
#     horas = float(qtd_horas)
#     taxa = float(valor_hora)
#     if horas <= 40:
#         salario = horas*taxa
#     else:
#         h_excd = horas - 40
#         salario = 40*taxa+(h_excd*(1.5*taxa))
#     print(salario)
# a = float(input("Informe as horas trabalhadas: "))
# b = float(input("informe valor da hora: "))
# calcular_pagamento(a, b)

#==========================================================================

def soma(x, y):
    result = x + y
    return result
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
res = soma(a, b)
print("Soma: ", res)