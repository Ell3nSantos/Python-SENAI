print('Mercado Y')
produtos = ['','Arroz', 'feijão','Carne','salgadinho']
precos = ['',10.50, 8.00,10.0,5.25]
print(f'''Produtos a venda', 
      {produtos[1]} R$ - {precos[1]}
      {produtos[2]} R$ - {precos[2]}
      {produtos[3]} R$ - {precos[3]}
      {produtos[4]} R$ - {precos[4]}
''')
carrinho = []
meu_total  = []


produto_1 = int(input('Escolha o produto pelo ID - 1 - 2 - 3 - 4'))
produto_2 = int(input('Escolha o produto pelo ID - 1 - 2 - 3 - 4'))


carrinho.append(produtos[produto_1])
carrinho.append(produtos[produto_2])


meu_total.append(precos[produto_1])
meu_total.append(precos[produto_2])


soma  =  sum(meu_total)
print('-------//------')
print(f'R$ {soma}')
print(f'''Seus produtos: 
      
      1 - {produtos[produto_1]}
      2 - {produtos[produto_2]}
      
      
      ''')










# tupla = (1,2,3,4,5,6)
# a,b,c,d,e,f = 1,2,3,4,5,6
# tupla = a,b,c,d,e,f
# print(tupla)


# estrutura de dados:
# guardar dados


nome = 'Julia'
lista = [1,2,3]
tuplas = (1,2,3)
conjuntos = {1,2,3}
dicionarios = {'keys': 'Values'}


pessoa =  {
'nome':'Paulo',
'Idade': 25,
'Endereço':'Rua r, nº 25',
'Curso':'Python 60h',
'livros': ['Harari','Taleb','X'],
'dados sensiveis':(12131,213221,4546545,'@paulo.com'),
'anos_viagem': {2022,2023,2024,2024},
'arvores genealogica':{
'Mãe':'Maria',
'Pai':'Caio',
'Filhos':2,


},
'Animais': input('Digite seu bichinho:  ')



}



print(pessoa['arvores genealogica']['Mãe'])


pessoa['veiculos'] = ['Jeep','Ferrari']


print(pessoa)









list()
tuple()
set()
dict()




# d = dict(n = 10, x = 20)
# print(d)
# lista =  [1,2,2,3,3,4,5,6,6]
# print(lista)
# conjuntos = {1,2,2,3,3,4,5,6,6}
# print(conjuntos)


# # c  =  set(range(1,12))
# # print(c)




dicionario =  {}




produto1 = input('p: ')
produto2 = input('p: ')


dicionario['Produtos'] = [produto1, produto2]
print(dicionario)