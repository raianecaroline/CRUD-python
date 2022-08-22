import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='bdteste',
)
cursor = conexao.cursor()

#CREATE
#nome_produto = "refrigerante"
#valor_produto = 5
#comando = f'INSERT INTO vendas (nome_produto, valor_produto) VALUES ("{nome_produto}", "{valor_produto}")'
#cursor.execute(comando)
#conexao.commit() # quando edita o banco de dados

#READ
#comando = f'SELECT * FROM vendas'
#cursor.execute(comando)
#resultado = cursor.fetchall() # ler o banco de dados
#print(resultado)

#UPDATE
#nome_produto = "refrigerante"
#valor_produto = 10
#comando = f'UPDATE vendas SET valor_produto = {valor_produto} WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit() # quando edita o banco de dados

#DELETE
#nome_produto = "refrigerante"
#comando = f'DELETE vendas WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit() # quando edita o banco de dados

cursor.close()
conexao.close()
