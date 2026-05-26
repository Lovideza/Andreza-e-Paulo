palavra = input("Digite uma palavra: ").lower()
contador_vogais = 0
contador_conso = 0
for letra in palavra:
    if letra in "aeiou":
        contador_vogais += 1
    elif letra.isalpha():
        contador_conso += 1

print(f"Tem {contador_vogais} vogais e {contador_conso} consoantes")
