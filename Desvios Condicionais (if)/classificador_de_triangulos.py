#assunto: condicional
#questao: Classificador de triangulos
#dificuldade: 5
#tags: funcao condicional
def classifica_triangulo(a, b, c):
    if (a == b) and (b == c):
        return "equilátero"
    elif (a != b) and (a != c) and (b != c):
        return "escaleno"
    else:
        return "isósceles"