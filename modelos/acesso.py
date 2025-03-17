import json
from usuario import Usuario

def validar_acesso(nome_usuario, area_desejada, usuarios): 
    for usuario in usuarios:
        if usuario.nome == nome_usuario and area_desejada in usuario.acessos:
            return True
    return False 

def verificar_acesso_input(nome_usuario, area_desejada, usuarios):
    print(f"🔍 Verificando acesso para: {nome_usuario} na área: {area_desejada}")

    if not usuarios:
        print("⚠️ Nenhuma permissão carregada. Verifique o arquivo JSON.")
        return

    try:
        if not any(usuario.nome == nome_usuario for usuario in usuarios):
            raise ValueError("Usuário não encontrado no sistema!")

        if validar_acesso(nome_usuario, area_desejada, usuarios):
            print("✅ Acesso permitido!")
        else:
            print("❌ Acesso negado!")

    except ValueError as e:
        print(f"❌ Erro: {e}")
    