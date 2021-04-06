#assunto: condicional
#questao: Todo mundo odeia o Chris
#dificuldade: 3
#tags: input condicional
name = str(input("Qual seu nome?"))
if name != 'Chris':
    print(f"Olá, {name}")
else:
    print("Todo mundo odeia o Chris")