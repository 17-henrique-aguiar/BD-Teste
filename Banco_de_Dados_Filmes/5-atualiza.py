import sqlite3

conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# Atualizando dados 
id = 1
cursor.execute(
    """
        UPDATE filmes SET nome = ?
        WHERE id = ?
    """,
    ("Sonic", id)
)

conexao.commit()
print("Dados atualizados")