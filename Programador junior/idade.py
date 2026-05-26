while True:
    try:
        idade = int(input("Digite sua idade: "))

        if idade < 0 or idade > 120:
            print("Idade inválida!")
            print("Tente novamente!")

        else:
            print(f"Sua idade é: {idade} anos")
            break

    except ValueError:
        print("A idade deve ser um número!")
        print("Tente novamente!")