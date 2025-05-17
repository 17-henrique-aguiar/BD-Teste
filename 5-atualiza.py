import sqlite3

conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# Atualizando dados 
id = 2
cursor.execute(
    """
        UPDATE filmes SET nome = ?
        WHERE id = ?
    """,
    ("Homem Aranha", id)
)

conexao.commit()
print("Dados atualizados")