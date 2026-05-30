def quadrado(num:int):
    return num * num
print(quadrado(4))

def media(a:float,b:float):
    return (a + b) / 2
print(media(7,9))

def maior(a:float,b:float):
    if a > b:
        return a
    else:
        return b
print(maior(10,7))

def par_impar(num:int):
    if num % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
print(par_impar(7))