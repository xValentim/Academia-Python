#assunto: condicional
#questao: Ano Bissexto
#dificuldade: 6
#tags: condicional
#OBS.:Pesquise como identificar um ano bissexto
def eh_bissexto(a):
    if a % 4 == 0 and not(a % 100 == 0):
        return True
    #elif a % 4 == 0 and a % 100 == 0 and a % 400 == 0:
    elif a % 400 == 0:
        return True
    else:
        return False