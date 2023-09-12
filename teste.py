# teste.py
import moeda

preco = float(input("Digite o preço: "))

print(f"Preço original: R${preco:.2f}")
print(f"Aumento de 10%: R${moeda.aumentar(preco, 10):.2f}")
print(f"Diminuição de 5%: R${moeda.diminuir(preco, 5):.2f}")
print(f"Dobro do preço: R${moeda.dobro(preco):.2f}")
print(f"Metade do preço: R${moeda.metade(preco):.2f}")
