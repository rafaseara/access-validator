import json
from modelos.usuario import Usuario

class JsonManager:
    """Classe para manipulacao de permissoes a partir de um arquivo JSON"""
    @staticmethod
    def carregar_permissoes(caminho):
        """
        Carrega as permissões de um arquivo JSON.
        
        Entrada:
            caminho (str): Caminho do arquivo JSON.
        
        Saída:
            list: Lista de objetos Usuario com permissões.
        """
        try:
            with open(caminho, 'r', encoding='utf-8') as arquivo:  
                dados = json.load(arquivo)
                return [Usuario(usuario['nome'], usuario['acessos']) for usuario in dados['usuarios']]
        except FileNotFoundError:
            print("❌ Erro: O arquivo de permissões não foi encontrado!")
            return []
        except json.JSONDecodeError:
            print("❌ Erro: O arquivo JSON está corrompido ou inválido!")
            return []