from funcionario import Funcionario

nome = input('Digite o nome do funcionário: ')
salario = float(input('Digite o salário do funcionário: '))
imposto = float(input('Digite o valor de imposto do funcionario: '))

funcionario1 = Funcionario(nome,salario)

funcionario1.setImposto(imposto)

opcao = int(input('\nDeseja aumentar o salário do funcionário? \n1-Sim \n2- Não \n'))

if(opcao == 1):
    porcentagem = float(input('\nDigite o valor em porcentagem que deseja aumentar: '))
    funcionario1.aumentarSalario(porcentagem)

print(funcionario1)