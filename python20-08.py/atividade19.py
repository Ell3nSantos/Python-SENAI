import sqlite3


conexao = sqlite3.connect('banco.db')


c = conexao.cursor()


 
c.execute('''
    CREATE TABLE IF NOT EXISTS pessoas(
          
     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
     nome TEXT NOT NULL,
     idade INTEGER NOT NULL,
     email TEXT NOT NULL,
     endereço TEXT NOT NULL,
     trabalho TEXT NOT NULL,
     graduacao TEXT NOT NULL        
    )
''')



nome =  input('Nome: ')
idade =  int(input('Idade: '))
email = input ('Email:')
endereço = input ('Endereço:')
trabalho = input ('Trabalho:')
graduacao = input('Graduação: ')




c.execute('''INSERT INTO pessoas(nome, idade, email, endereço, trabalho, graduacao)
          values (?,?,?,?,?,?)''',(nome, idade, email, endereço, trabalho, graduacao))



conexao.commit()




c.execute('SELECT * FROM pessoas')
dados = c.fetchall()



for dados_tabela in dados:
    print(f'id {dados_tabela[0],dados_tabela[1], dados_tabela[2], dados_tabela[3], dados_tabela[4], dados_tabela[5]}')



conexao.close()    



c = input('Enter para sair')