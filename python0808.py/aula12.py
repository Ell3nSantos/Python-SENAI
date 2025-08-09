# Exercício 1:
# Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.
# try:
#     numero = int (input ('Digite um numero inteiro:'))
#     print (numero)
# except IndexError as erro:
#     print('numero invalido!')

# # Exercício 2:
# # Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.
# try:
#     n1 = int (input('digite um numero'))
#     n2 = int (input('digite um numero'))
#     n1/n2
# except ZeroDivisionError as erro:
#     print(erro)




# Exercício 3:
# Crie uma função que aceite uma lista e um índice como entrada e retorne o parametro do elemento naquele índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).
def verificar(l):
    try:
        n = int(input('teste'))
        l [n]

    except IndexError as erro:
        print(erro)

l = [1,2,3]
verificar(l)








# EXEMPLOS ATIVIDADE:
# def teste():
#     try:
#         n = int(input('Numero: '))
#         z = int(input('Numero: '))


#         n/z
#         # print(n*5)
#         # lista =  [1,3,4]
#         # print(lista[6]) 
#         # div = n /0
#         # print(div)


#     except ZeroDivisionError as erro:
#         print(erro)
#     except ValueError as erro:
#         print(erro)    
#     except TypeError as erro:
#         print(erro)
#     except SyntaxError as erro:
#         print(erro)
#     except IndexError as erro:
#         print(erro)
#     except IndentationError as erro:
#         print(erro)
#     except IndexError as erro:
#         print(erro)                    
#     else:
#         print('erro desconhecido')  
#     finally:
#         print('Fim de carregamento...')        


# teste()


