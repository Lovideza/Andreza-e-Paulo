notas = [6, 8, 9, 3, 10, 7, 4, 5]
aprovados = []
reprovados = []
for i in range(len(notas)):
    if notas[i] >= 7:
        aprovados.append(notas[i])
    else:
        reprovados.append(notas[i])
print(f"Lista de notas aprovadas: {aprovados} {len(aprovados)} notas ; Lista de notas raprovadas: {reprovados} {len(reprovados)} notas")