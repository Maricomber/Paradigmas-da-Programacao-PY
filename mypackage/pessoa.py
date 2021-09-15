class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        return '\nNome: '+str(self.nome + '\nIdade: ')+str(self.idade)

    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def calcularMaisVelho(pessoas):
        pessoaMV = Pessoa('',0)
        for i in pessoas:
            if(i.getIdade() > pessoaMV.getIdade()):
                pessoaMV = i
        return pessoaMV

