#Armazenar mais de uma informação em variaveis
#manter a sequencia dos dados em uma variavel 
#O lower() metodo retorna uma string onde todos os 
#caracteres sao minusculos
#Simbolos e numeros sao ignorados
'''
cor_cliente = input('Digite a cor desejada: ')
cores=('amarelo','verde','azul','vermelho')

if cor_cliente.lower() in cores:
    print('sim')
else:
    print('Não temos esta cor em estoque')

#juntar listas

cores = ['amarelo','verde','azul','vernelho','roxo']
valores=[10,20,30,40,50]

duas_listas = zip(cores, valores)

print(list(duas_listas))



#Criar uma lista de frutas a apartir do input fornecido por virgulas:

frutas_usuario = input('Digite o nome das frutas separados por virgula: ')

frutas_lista = frutas_usuario.split(',')

print(frutas_lista)
'''

#Tuples (Tuplas)
#As tuplas são usadas para armazenar vários itens em uma unica variavel.
cores_list = ['amarelo','verde','azul','vermelho']
cores_tuples=('amarelo','verde','azul','vermelho')

cores_list.append('roxo')

print(type(cores_list))
print(type(cores_tuples))

duas_listas = cores_list * 2 
print(duas_listas)