def obter_idade_valida():
    while True: 
        try:  
            idade = int(input("Digite a idade do paciente: "))
            if idade < 0 or idade > 120:
                print("Digite uma idade válida!")
                continue
            else:
                return idade
        except ValueError:
            print("Digite somente números")
            continue
def obter_cor_valida(nome_paciente):
    while True:
        cor_pulseira = input("Escreva a cor da pulseira(Vermelha/Amarela/Verde): ")
        
        if cor_pulseira == "Vermelha":
            print(f"Encaminhar {nome_do_paciente} imediatamente para a Emergência!")
            return cor_pulseira
        elif cor_pulseira == "Amarela":
            print(f"Encaminhar {nome_do_paciente} para a Sala de Espera Prioritária.")
            return cor_pulseira
        elif cor_pulseira == "Verde":
            print(f"Encaminhar {nome_do_paciente} para o Atendimento Geral.")
            return cor_pulseira
        else:
            print("Cor inválida. Por favor, faça a triagem novamente.")

lista_pacientes = []
numero_pacientes = 0

while True:
    nome_paciente = input("Digite o nome do paciente ou 'Sair' para fechar o sistema: ")
    if nome_paciente == "Sair":
        print("Encerrando o sistema...")
        break
    else:
        idade = obter_idade_valida()
        cor_pulseira = obter_cor_valida(nome_paciente)
        lista_pacientes.append({
            "Nome": nome_paciente,
            "Idade": idade,
            "Pulseira": cor_pulseira
        })
        numero_pacientes += 1

print("\n=== RELATÓRIO DO TURNO ===")
for paciente in lista_pacientes:
    print(f"Paciente: {paciente['Nome']} - Idade: {paciente['Idade']} anos - Pulseira: {paciente['Pulseira']}")

print(f"\nTotal de pacientes atendidos: {numero_pacientes}")
print("==========================")