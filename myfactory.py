# -*- coding: utf-8 -*-


class Area(object):
    TYPE = None

    def __init__(self, largura, comprimento):
        self.largura = largura
        self.comprimento = comprimento

    def calcular(self):
        raise NotImplementedError()

    @classmethod
    def checar_calculo(cls, tipo_calculo):
        return tipo_calculo == cls.TYPE

class Quadrado(Area):
    TYPE = 'Quadrado'

    def calcular(self):
        return self.largura * self.comprimento

class TrianguloRetangulo(Area):
    TYPE = 'TrianguloRetangulo'

    def calcular(self):
        return (self.largura ** 2) + (self.comprimento ** 2) ** 2


# factory
class AreaFactory(object):
    TIPOS_CALCULO = [Quadrado, TrianguloRetangulo]
    def __init__(self, tipo, largura, comprimento):
        self.tipo = tipo
        self.largura = largura
        self.comprimento = comprimento

    def rodar(self):
        for obj in self.TIPOS_CALCULO:
            if obj.checar_calculo(self.tipo):
                return obj(self.largura, self.comprimento).calcular()

if __name__ == '__main__':
    calculo = AreaFactory('TrianguloRetangulo', 5, 5)
    print(calculo.rodar())
