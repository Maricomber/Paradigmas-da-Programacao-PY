from pessoa import Pessoa

nome = input("\nDigite o nome da primeira pessoa: ")
idade = int(input("Digite a idade da primeira pessoa: "))

pessoa1 = Pessoa(nome, idade)

nome = input("\nDigite o nome da segunda pessoa: ")
idade = int(input("Digite a idade da primeira pessoa: "))

pessoa2= Pessoa(nome, idade)

pessoas = [pessoa1, pessoa2]

print('\nA pessoa mais velha é: ')
print(Pessoa.calcularMaisVelho(pessoas))