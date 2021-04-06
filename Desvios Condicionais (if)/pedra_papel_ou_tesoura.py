#assunto: condicional
#questao: Pedra papel ou tesoura
#dificuldade: 6
#tags: funcao condicional
def pedra_papel_tesoura(p1, p2):
    if (p1 or p2) not in ['pedra', 'papel', 'tesoura']:
        return 'Escolha pedra, papel ou tesoura para jogar'

    if p1 == p2:
        return 'empate'
    elif p1 == 'pedra' and p2 == 'papel':
        return 'dois'
    elif p1 == 'pedra' and p2 == 'tesoura':
        return 'um'
    elif p1 == 'papel' and p2 == 'pedra':
        return 'um'
    elif p1 == 'papel' and p2 == 'tesoura':
        return 'dois'
    elif p1 == 'tesoura' and p2 == 'pedra':
        return 'dois'
    elif p1 == 'tesoura' and p2 == 'papel':
        return 'um'