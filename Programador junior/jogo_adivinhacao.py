import random
while True:
    numero_secreto = random.randint(1, 20)
    num_tentativas = 0
    print("======= Jogo da adivinhação =======")
    while True:
        try:
            print(f"===== Você tem {5 - num_tentativas} tentativas =====")
            if num_tentativas == 5:
                print("Você perdeu!")
            else:
                palpite = int(input("Adivinhe o número aleátorio entre 1 e 20: "))
                if palpite < 1 or palpite > 20:
                    print("Você saiu do alcance, tente novamente:")
                    continue
                elif palpite > numero_secreto:
                    print("O número secreto é menor")
                    num_tentativas += 1
                    continue
                elif palpite < numero_secreto:
                    print("O número secreto é maior")
                    num_tentativas += 1
                    continue
                else:
                    print("Você acertou!")
            print(f"O número secreto era: {numero_secreto}")
            num_tentativas = 5
            while True:
                escolha = input("Jogar novamente?(S/N): ")
                if escolha == "S":
                    print("Sorteando novo número...")
                    print("===================================")
                    break
                elif escolha == "N":
                    print("Encerrando...")
                    exit()
                else:
                    print("Digite uma opção disponível")
                    continue
            break
        except ValueError:
            print("Digite apenas números inteiro")
            print("===================================")
            continue