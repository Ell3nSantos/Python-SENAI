dicionario_ecommerce = {
'livros': {
'a': 50.0, 
'b': 80.0, 
'c': 100.0
},

 'tablets': {
 'd': 1.000, 
 'e': 2.000, 
 'f': 3.000
 },

'fones_de_ouvido': {
'g': 80.0, 
'h': 100.0, 
'i': 150.00
}
}
print (dicionario_ecommerce)


seção1 = input('seção:')
seção2 = input ('seção:')
seção3 = input ('seção:')

produto1 = input ('digite o produto:')
produto2 = input ('digite o produto:')
produto3 = input ('digite o produto:')

carrinho = [produto1, produto2, produto3]
valores =[dicionario_ecommerce[seção1][produto1], dicionario_ecommerce[seção2][produto2], dicionario_ecommerce[seção3][produto3]]
soma = sum (valores)

print (carrinho)
print ('R$', soma)

