#assunto: condicional
#questao: Teste de maioridade
#dificuldade: 3
#tags: funcao condicional
def verifica_idade(i):
    if i < 18:
        return "Não está liberado"
    elif i >= 18 and i < 21:
        return "Liberado BRASIL"
    elif i >= 21:
        return "Liberado EUA e BRASIL"
