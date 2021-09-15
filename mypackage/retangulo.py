import math

class Retangulo:
    def __init__(self, base, altura):
            self.base = base
            self.altura = altura
            self.area = base *altura
            self.perimetro = (2*altura)+(2*base)
            self.diagonal = math.sqrt(math.pow(altura,2)+math.pow(base,2))

    def __str__(self):
        return '\nArea: '+str(self.area)+str('\nPerimetro: ')+str(self.perimetro
        )+str('\nDiagonal: ')+str(self.diagonal)
        #+ '\nPerimetro: ')+str(self.perimetro)

    def getArea(self):
        return self.area
    
    def getPerimetro(self):
        return self.perimetro

    def getDiagonal(self):
        return self.diagonal