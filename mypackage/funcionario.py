import pessoa

class Funcionario(pessoa.Pessoa):

    def __init__(self, nome, salario_bruto):
        self.nome = nome
        self.salario_bruto = salario_bruto

    def __str__(self):
        return '\nFuncionario: '+str(self.nome)+'\nSalário: '+str(self.salario_liquido)

    def getSalarioBruto(self):
        return self.salario_bruto
    
    def getSalarioLiquido(self):
        return self.salario_liquido

    def setImposto(self, imposto):
        self.imposto = imposto
        self.atualizaSalarioLiquido()

    def setSalarioBruto(self, salario):
        self.salario_bruto = salario
        self.atualizaSalarioLiquido()
    
    def salarioMedio(funcionarios):
        valor = 0.0;
        for func in funcionarios:
            valor = valor + func.getSalarioBruto()
        
        valor = valor / len(funcionarios)
        return print('\nO salário médio é: '+str(valor))

    def atualizaSalarioLiquido(self):
        self.salario_liquido = self.salario_bruto - self.imposto
    
    def aumentarSalario(self, porcentagem):
        valor = (self.salario_bruto * porcentagem)/100 + self.salario_bruto
        self.salario_bruto = valor
        self.atualizaSalarioLiquido()
