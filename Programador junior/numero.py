while True:
    try:
        num = int(input("Digite um número inteiro e positivo: "))

        if num < 0:
            print("Você deve digitar um número positivo!")
            print("Tente novamente!")
        else:
            print("Número válido!")
            break

    except ValueError:
        print("Você deve digitar um número inteiro!")

print(f"O número digitado foi: {num}")