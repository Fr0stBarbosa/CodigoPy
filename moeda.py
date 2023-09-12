
# Crie um modulo cahamdo moeda.py que tenha as funcoes
# incorporadas aumentar(), diminuir(),dobro() e metade().
# faça tambem um programa que importa esse modulo e use algumas
# dessas funções crie modulo teste.py

def aumentar(preço, taxa):
    return  preço + (preço * taxa/100)
    

def diminuir(preço,taxa):
    return preço - (preço * taxa/100)
    
def dobro(preço):
    return  preço * 2

def metade(preço):
    return preço / 2