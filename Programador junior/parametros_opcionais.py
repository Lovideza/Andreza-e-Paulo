def potencia(base, expoente=2):
    return base ** expoente
print(potencia(5))
print(potencia(2,3))

def saudacao(nome="Visitante"):
    return(f"Olá, {nome}!")
print(saudacao())
print(saudacao("Paulo"))

def calculadora(a, b, operacao="+"):
    if operacao == "+":
        return a + b
    elif operacao == "-":
        return a - b
    elif operacao == "*":
        return a * b
    elif operacao == "/":
        if b == 0:
            return "Não é possível divisão por zero"
        else:
            return a / b
    else:
        return("Digite uma operação válida")
print(calculadora(10, 5))
print(calculadora(10, 5, "*"))