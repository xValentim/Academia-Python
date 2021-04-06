#assunto: condicional
#questao: Multa de velocidade
#dificuldade: 4
#tags: input condicional
v = float(input("Digite a velocidade"))
if v <= 80.00:
    print("Não foi multado")
else:
    multa = (v - 80.00) * 5.00
    print(f'Você foi multado. Multa: R$ {multa:.2f}')