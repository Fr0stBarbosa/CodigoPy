'''
from funcao import somar,multi
from itens.cadastro import cliente

somar()
multi()
cliente()
'''

'''
#Desafio de Funções I
def dobro(n):
    return n *2

def quad(n):
    return n ** 2

num = float(input('Insira um numero para saber seu dobro ao quadrado: '))

print(dobro(quad(num)))
'''
#Desafio de Funções II
#largura = comprimento
def calc_tinta(rendimento, altura, largura):
    area_parede = altura * largura #area que sera pintada
    quantidade_tinta = area_parede / rendimento
    return quantidade_tinta

# Solicita as informações ao usuário
rendimento = float(input("Informe o rendimento da tinta em metros quadrados por litro: "))
altura = float(input("Informe a altura da parede (em metros): "))
largura = float(input("Informe a largura da parede (em metros): "))

# Calcula a quantidade de tinta necessária
quant_tinta = calc_tinta(rendimento, altura, largura)

# Imprime o resultado
print(f"Você necessita de {quant_tinta:.2f} latas de tinta.")

