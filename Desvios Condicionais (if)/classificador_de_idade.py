#assunto: condicional
#questao: Classificador de idade
#dificuldade: 3
#tags: funcao condicional
def classifica_idade(i):
    if i <= 11:
        return('crianca')
    elif i > 11 and i <= 17:
        return('adolescente')
    elif i > 17:
        return('adulto')