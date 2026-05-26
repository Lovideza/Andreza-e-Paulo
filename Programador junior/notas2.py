notas = [6, 8, 9, 3, 10, 7]

maior = max(notas)
menor = min(notas)
media = sum(notas) / len(notas)

print(f"A maior nota da sala foi {maior}, a menor foi {menor} e a media foi {round(media, 2)}")

contador = 0

for i in range(len(notas)):
    if notas[i] >= 7:
        contador += 1

print(f"A sala teve {contador} alunos aprovados")





notas = [6, 8, 9, 3, 10, 7]

maior = max(notas)
menor = min(notas)
media = sum(notas) / len(notas)

print(f"A maior nota da sala foi {maior}, a menor foi {menor} e a média foi {round(media, 2)}")

contador = 0
for n in notas:
    if n >= 7:
        contador += 1

print(f"A sala teve {contador} alunos aprovados")