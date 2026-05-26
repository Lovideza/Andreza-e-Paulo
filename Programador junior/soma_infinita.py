numeros = []
while True:
    num = int(input("Digite um número para adicionar à soma (0 para sair): "))
    if num == 0:
        print("Encerrando...")
        break
    else:
        numeros.append(num)
        print(f"Quantidade de números: {len(numeros)}")
        print(f"Soma: {sum(numeros)}")