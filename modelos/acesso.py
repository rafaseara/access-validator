import json
from modelos.usuario import Usuario

def validar_acesso(nome_usuario, area_desejada, usuarios):
    nome_usuario = nome_usuario.strip().lower()  
    area_desejada = area_desejada.strip().lower()  

    for usuario in usuarios:
        if usuario.nome.strip().lower() == nome_usuario and area_desejada in [a.strip().lower() for a in usuario.acessos]:
            return True
    return False

def verificar_acesso_input(nome_usuario, area_desejada, usuarios):
    print(f"Verificando acesso para: {nome_usuario.capitalize()} na área: {area_desejada}")

    if not usuarios:
        print("⚠️ \"Nenhuma permissão carregada. Verifique o arquivo JSON.\"")
        return

    try:
        # Verificar se o nome do usuário existe, considerando a comparação insensível a maiúsculas/minúsculas
        if not any(usuario.nome.strip().lower() == nome_usuario.strip().lower() for usuario in usuarios):
            raise ValueError("Usuário não encontrado no sistema!")

        if validar_acesso(nome_usuario, area_desejada, usuarios):
            print("✅  \"Acesso permitido!\"")
        else:
            print("❌  \"Acesso negado!\"")

    except ValueError as e:
        print(f"❌ Erro: {e}")
    