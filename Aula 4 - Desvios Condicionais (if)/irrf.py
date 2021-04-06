#assunto: condicional
#questao: IRRF
#dificuldade: 6
#tags: input condicional
sbruto = float(input("Salario"))
ndep = float(input("dependentes"))

if sbruto <= 1045:
    aliq1 = 0.075 * sbruto
elif sbruto <= 2089.6:
    aliq1 = 0.09 * sbruto
elif sbruto <= 3134.4:
    aliq1 = 0.12 * sbruto
elif sbruto <= 6101.06:
    aliq1 = 0.14 * sbruto
else:
    aliq1 = 671.12

bc = sbruto - aliq1 - (ndep * 189.59)

if bc <= 1903.98:
    aliq2 = 0
    ded = 0
elif bc <= 2826.65:
    aliq2 = 0.075
    ded = 142.8
elif bc <= 3751.05:
    aliq2 = 0.15
    ded = 354.8
elif bc <= 4664.68:
    aliq2 = 0.225
    ded = 636.13
else:
    aliq2 = 0.275
    ded = 869.36

fim = bc * aliq2 - ded
print(fim)