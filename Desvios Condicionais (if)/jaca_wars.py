#assunto: condicional
#questao: Jaca Wars!
#dificuldade: 5
#tags: condicional
import math

D = 100
v = float(input("Digite a velocidade da jaca\n"))
teta = float(input("Digite o valor do angulo em graus\n"))
teta = (teta / 360) * (2 * math.pi)
twov = v * v
sen2teta = math.sin(2 * teta)
g = 9.8
d = (twov * sen2teta) / g

if d > (D - 2) and d < (D + 2):
    print("Acertou!")
elif d < (D - 2):
    print("Muito perto")
elif d > (D + 2):
    print("Muito longe")