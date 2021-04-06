#assunto: condicional
#questao: Calculo de aumento de salario
#dificuldade: 3
#tags: funcao condicional
def calcula_aumento(s):
    if s > 1250:
        s = s * 0.1
    else:
        s = s * 0.15
    return s