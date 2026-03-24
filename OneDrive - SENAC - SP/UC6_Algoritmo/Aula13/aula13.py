import pymysql as pySQL

conexao = pySQL.connect(
    host="localhost", # endereço do servidor
    user="root", # usuário do MySQL
    password="", # senha do MySQL
    database="bd_livariaonline" #  branco que você criou
    port=3306 # porta padrão do MySQL
)

# cursos versao dicionário
cursor = conexao.cursor(pySQL.cursors.DictCursor)

# buscar registros
cursor.execute("SELECT * FROM clientes")
todos = cursor.fetchall()

for cliente in todos:
    print(cliente["nome"], cliente["email"])
