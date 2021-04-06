#assunto: condicional
#questao: Preco da passagem
#dificuldade: 3
#tags: input condicional
dist = float (input("Qual distância você deseja percorrer em km?\n"))

if dist <= 200:
    valor = dist * 0.5
else:
    valor = 200 * 0.5 + (dist - 200) * 0.45
print(f"Valor total: {valor:.2f}")