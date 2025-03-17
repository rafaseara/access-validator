import json
from modelos.usuario import Usuario

def validar_acesso(nome_usuario, area_desejada, usuarios):
    """
    Faz a validacao do usuario no json e se sua area desejada se encontra na area permitida.
    
    Entrada:
        nome_usuario (str): Nome do usuário.
        area_desejada (str): Área desejada.
    
    Saída:
        bool: Retorna verdadeiro se o usuário tiver acesso, e falso para o contrário.
    """

    nome_usuario = nome_usuario.strip().lower()  
    area_desejada = area_desejada.strip().lower()  

    for usuario in usuarios:
        if usuario.nome.strip().lower() == nome_usuario and area_desejada in [a.strip().lower() for a in usuario.acessos]:
            return True
    return False

def verificar_acesso_input(nome_usuario, area_desejada, usuarios):
    """
    Verifica e exibe se o usuário tem acesso à área solicitada conforme json.
    
    Entrada:
        nome_usuario (str): Nome do usuário.
        area_desejada (str): Área desejada.
        usuarios (list): Lista de usuários e suas permissões.
    """
    
    print(f"\nVerificando acesso para {nome_usuario.capitalize()} na área: {area_desejada}")

    if not usuarios:
        print("⚠️ \"Nenhuma permissão carregada. Verifique o arquivo JSON.\"\n")
        return

    try:
        if not any(usuario.nome.strip().lower() == nome_usuario.strip().lower() for usuario in usuarios):
            raise ValueError("Usuário não encontrado no sistema!")

        if validar_acesso(nome_usuario, area_desejada, usuarios):
            print("✅  \"Acesso permitido!\"\n")
        else:
            print("❌  \"Acesso negado!\"\n")

    except ValueError as e:
        print(f"❌ Erro: {e}\n")
    