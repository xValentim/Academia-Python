#assunto: condicional
#questao: Emprestimo bancario
#dificuldade: 4
#tags: input condicional
valor = float(input("Qual o valor da casa?\n"))
salario = float(input("Qual o valor do seu salário?\n"))
anos = float(input("Em quantos anos você deseja pagar?\n"))
meses = anos * 12
if valor / meses < 0.3 * salario:
    print("Empréstimo aprovado")
else:
    print("Empréstimo não aprovado")