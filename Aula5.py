#Operadores lógicos 
'''
# Operador AND 
renda_ac_5m = True
n_l = True

if renda_ac_5m and n_l:
    print('Financiamento Aprovado')
else: 
    print('Financiamento Reprovado')

idd_lucas = 21
idd_carol = 19
    
if idd_lucas >= 18 and idd_carol >= 18:
    print('Pelo menos um dos dois e maior de idade')
else: 
    print('Lucas e Carol são maiores de idade')

# Operador OR 

renda_ac_5m = True
n_l = False

if renda_ac_5m or n_l:
    print('Financiamento Aprovado')
else:  
    print('Financiamento Reprovado')

'''
'''
idd_lucas = 21
idd_carol = 19

#Operador OR 
if idd_lucas >= 18 or idd_carol >= 18:
    print('Pelo menos um dos dois e maior de idade')
else: 
    print('Lucas e Carol são maiores de idade')
    

# Multiplos operadores de comparação 

v = 20 

if 20 <= v <40:
#if v >= 20 and v <40:
    print('Produto foi aceito')
else:
    print('Produto não aceito')


# FOR 

# Imprimir de 1 a 5 

for n in range (1,20,2):
    print(n)

l = ['rio','sampa','belo','curitiba']

for lj in l:
    print(lj)
    print('Acabou o for')

for i in range (4):
    print(i)
    print(l[i])
# FOR para STRINGS

#for letra in 'google':
 # print(letra)

palavra = 'google'

for letra in palavra:
    print(letra + ' esta dentro da palavra google')
'''
