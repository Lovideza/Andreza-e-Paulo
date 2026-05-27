while True:
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        op = input("Qual operação você deseja fazer? +, - , /, *(Digite 0 para sair): ")
        if op == "+" :
            soma = num1 + num2
            print(f"Soma: {soma}")
        elif op== "-" :
            sub = num1 - num2
            print(f"Subtração: {sub}")
        elif op== "/" :
            if num2 = 0:
                print("Divisão por zero não é possível!")
            else:
                div = num1 / num2
                print(f"Divisão: {div}")
        elif op== "*" :
            mult = num1 * num2
            print(f"Multiplicação: {mult}")
        elif op == "0":
            print("Encerrando...")
            break
        else:
            print("Operação inválida!")
            print("Tente novamente")
    except ValueError:
        print("Você deve digitar um número!")
