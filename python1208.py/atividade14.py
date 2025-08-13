with open('exemplo.py', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)






# encoding= 'utf-8' PARA ARQUIVOS QUE TENHAM Ç OU ~
# with open('exemplo2.txt','r', encoding= 'utf-8') as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)





# import os
# # with open('novo_diretorio', 'w') as novo_arquivo:
# os.mkdir('novo_arquivo')

# with open('exemplo.txt', 'r') as arquivo:
#     conteúdo = arquivo.read()
#     print(conteúdo)​





# import os
# os.rename('exemplo.txt', 'exemplo_rename')






# import os
# with os.scandir('c:/Users/aluno/Desktop/aula12/') as entrada:
#       for arquivo in entrada:
#          print(f'Diretório encontrado: {arquivo.name}')