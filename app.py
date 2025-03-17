from utils.json_manager import JsonManager
from modelos.acesso import verificar_acesso_input

def main():
    usuarios = JsonManager.carregar_permissoes('permissoes.json')

    nome_usuario = input("Digite seu nome: ")
    area_desejada = input("Digite a área que deseja acessar: ").strip()

    verificar_acesso_input(nome_usuario, area_desejada, usuarios)

if __name__ == "__main__":
    main()