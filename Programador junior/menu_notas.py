def obter_nota_valida(ordem):
    while True:
        try:
            nota = float(input(f"Digite a {ordem} nota: "))
            if nota > 10 or nota < 0:
                print("Digite uma nota válida")
                continue
            else:
                return nota
        except ValueError:
            print("Digite somente números")   

def calcular_media(lista_notas):
    if len(lista_notas) == 0:
        print("Nenhuma nota válida foi inserida")
        return 0
    else:
        media = sum(lista_notas) / len(lista_notas)
        return media
            
lista_notas = []

while True:
    print("==== Sistema de cálculo de média ====")
    nota1=obter_nota_valida("primeira")
    lista_notas.append(nota)
    nota2=obter_nota_valida("segunda")
    lista_notas.append(nota)
    print("=====================================")
    break

media = calcular_media(lista_notas)
if media >= 7:
    print(f"A sua média é: {media} - O aluno está aprovado")
else:
    print(f"A média é: {media} - O aluno está reprovado")
print("=====================================")