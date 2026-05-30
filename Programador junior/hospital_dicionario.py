lista_pacientes = []
numero_pacientes = 0
while True:
    nome_paciente = input("Digite o nome do paciente ou 'Sair' para fechar o sistema: ")
    if nome_paciente == "Sair":
        print("Encerrando o sistema...")
        break
    while True:
        idade = int(input("Digite a idade do paciente: "))
        if idade < 0 or idade > 120:
            print("Digite uma idade válida!")
        else:
            lista_pacientes.append({
                "Nome": nome_paciente,
                "Idade": idade
            })
            numero_pacientes += 1
            break

print("\n=== RELATÓRIO DO TURNO ===")
for paciente in lista_pacientes:
    print(f"Paciente: {paciente['Nome']} - Idade: {paciente['Idade']} anos")

print(f"\nTotal de pacientes atendidos: {numero_pacientes}")
print("==========================")
