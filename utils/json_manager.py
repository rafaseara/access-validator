import json
from modelos.usuario import Usuario

class JsonManager:
    @staticmethod
    def carregar_permissoes(caminho):
        try:
            with open(caminho, 'r', encoding='utf-8') as arquivo:  # Especificando codificação UTF-8
                dados = json.load(arquivo)
                return [Usuario(usuario['nome'], usuario['acessos']) for usuario in dados['usuarios']]
        except FileNotFoundError:
            print("❌ Erro: O arquivo de permissões não foi encontrado!")
            return []
        except json.JSONDecodeError:
            print("❌ Erro: O arquivo JSON está corrompido ou inválido!")
            return []