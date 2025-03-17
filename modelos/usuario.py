class Usuario:
    """Classe de um usuario com suas caracteristicas"""
    def __init__(self, nome, acessos):
        """
        Inicializa um usuário com nome e permissões de acesso.
        
        Entrada:
            nome (str): Nome do usuário.
            acessos (list): Áreas de acesso do usuário.
        """
        
        self._nome = nome
        self._acessos = acessos
    
    @property
    def nome(self):
        return self._nome

    @property
    def acessos(self):
        return self._acessos