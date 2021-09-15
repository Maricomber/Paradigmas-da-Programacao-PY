import pessoa

class Aluno(pessoa.Pessoa):
    
    def __init__(self, nome, idade, notas):
        resultado = 0.0
        count = 0
        media = 60

        self.nome = nome
        self.idade = idade
        self.notas = notas

        for nota in notas:
            resultado += nota

        if(resultado >= media):
            self.situacao = 'APROVADO'
            self.pontos_faltanes = 0
        else:
            self.situacao = 'REPROVADO'
            self.pontos_faltanes = media-resultado

    def __str__(self):
        retorno = '\nNome: '+str(self.nome)+str('\nSituacao: ')+str(self.situacao)
        if(self.pontos_faltanes > 0):
            retorno += str('\nPontos faltantes: ')+str(self.pontos_faltanes)
        return retorno
    
