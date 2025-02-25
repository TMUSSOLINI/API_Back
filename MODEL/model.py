class Carro:
    def __init__(self, id=None, marca=None, modelo=None, ano=None, km=None, imagem=None):
        self._id = id
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._km = km
        self._imagem = imagem

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca
    
    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo
        
    @property
    def ano(self):
        return self._ano
    
    @ano.setter
    def ano(self, ano):
        self._ano = ano

    @property
    def km(self):
        return self._km
    
    @km.setter
    def km(self, km):
        self._km = km

    @property
    def imagem(self):
        return self._imagem
    
    @imagem.setter
    def imagem(self, imagem):
        self._imagem = imagem

    def __iter__(self):
        for key in self.__dict__:
            yield key.replace('_',''), self.__getattribute__(key)



if __name__ == '__main__':
    obj = Carro('teste', 'teste', 'teste','teste', 'teste', 'teste')
    for nome, valor in obj:
        print(nome, valor)