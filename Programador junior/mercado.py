precos = [12.50, 7.99, 25.00, 3.50, 40.00, 15.75]
maior = max(precos)
menor = min(precos)
total = sum(precos)
caros = []
baratos = []
for preco in precos:
    if preco > 20:
        caros.append(preco)
    else:
        baratos.append(preco)
print(f"Maior preço: R${maior}")
print(f"Menor preço: R${menor}")
print(f"Produtos caros: {caros}; {len(caros)} produtos")
print(f"Produtos baratos: {baratos}; {len(baratos)} produtos")
print(f"Total: R${total}")
if total > 80:
    print(f"Total com desconto: R${round(total * 0.90, 2)}")
    print(f"Você economizou: R${round(total - (total * 0.9), 2)}")