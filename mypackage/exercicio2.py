from funcionario import Funcionario

nome = input('\nDigite o nome do primeiro funcionário: ')
salario = float(input('Digite o salário do primeiro funcionário: '))

funcionario1 = Funcionario(nome,salario)

nome = input('\nDigite o nome do segundo funcionário: ')
salario = float(input('Digite o salário do segundo funcionário: '))

funcionario2 = Funcionario(nome,salario)

funcionarios = [funcionario1,funcionario2]

Funcionario.salarioMedio(funcionarios)