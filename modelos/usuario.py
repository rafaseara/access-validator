class Usuario:
    def __init__(self, nome, acessos):
        self._nome = nome
        self._acessos = acessos
    
    @property
    def nome(self):
        return self._nome

    @property
    def acessos(self):
        return self._acessos