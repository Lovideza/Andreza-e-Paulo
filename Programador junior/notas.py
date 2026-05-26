notas = [7,5,8]
soma = 0
for i in range(len(notas)):
    soma += notas[i]
media = soma / len(notas)
print(f"Sua média foi {round(media, 2)}")
if media >= 7:
    print("Você está aprovado! Parábens!")
elif media >= 5:
    print("Você está de recuperação!")
else:
    print("Você está reprovado")