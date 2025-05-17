import sqlite3

# Criando a conexão 
conexao = sqlite3.connect('titulo.db')

# Criando o cursor (cursor = é pra poder trabalhar no banco de dados)
cursor = conexao.cursor()

# Criando a tabela
cursor.execute(
    """
        CREATE TABLE FILMES(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ano INTEGER NOT NULL,
            nota REAL NOT NULL
        );
    """
)

# Fecha a conexão
conexao.close()
print("Tabela foi criada")