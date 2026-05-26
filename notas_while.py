notas = []
while True:
    try:
        print("Digite -1 para sair")
        nota = float(input("Digite uma nota: "))
        if nota == -1:
            print("Encerrando...")
            break
        elif nota < 0 or nota > 10:
            print("Tente novamente!")
            print("Nota inválida!")
        else:
            notas.append(nota)
    except ValueError:
        print("Tente novamente!")
        print("Você deve digitar um número!")
qtd_notas = len(notas)
media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)
print(f"Quantidade de notas: {qtd_notas}")
print(f"Média: {round(media, 2)}")
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")