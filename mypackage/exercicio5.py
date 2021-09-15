from aluno import Aluno

nome = input('\nDigite o nome do aluno: ')
idade = int(input('Digite a idade do aluno: '))
nota1 = float(input('Digite a nota 1 do aluno: '))
nota2 = float(input('Digite a nota 2 do aluno: '))
nota3 = float(input('Digite a nota 3 do aluno: '))

notas = [nota1,nota2,nota3]

aluno = Aluno(nome,idade,notas)

print(aluno)