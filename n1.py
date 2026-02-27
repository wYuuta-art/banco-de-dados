import sqlite3

# Cria um arquivo cadastro.db e conecta
conn = sqlite3.connect('cadastro.db')
cursor = conn.cursor()

# Criando tabela "usuarios" com peso e salario
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE,
    sexo TEXT CHECK(sexo IN ('M', 'F')),
    nascimento TEXT,
    peso REAL,
    altura REAL,
    salario INTEGER,
    nacionalidade TEXT NOT NULL DEFAULT 'Brasil'
)
''')
cursor.execute('''
ALTER TABLE usuarios
ADD COLUMN email TEXT
''')

cursor.execute('''
ALTER TABLE usuarios
RENAME COLUMN nome TO nome_completo
''')

cursor.executemany(
    '''
    INSERT INTO usuarios
    (nome_completo, sexo, nascimento, peso, altura, salario, email)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''',
    [
        ("Lira", "M", "2007-02-24", 69.70, 1.80, 500000, "lira@email.com"),
        ("Maria", "F", "2004-01-10", 55.00, 1.65, 320000, "maria@email.com")
    ]
)

cursor.execute("SELECT * FROM usuarios")
dados = cursor.fetchall()
for usuario in dados:
    id, nome, sexo, nascimento, peso, altura, salario, nacionalidade = usuario
    salario_real = salario / 100
    print(f"ID: {id} | Nome: {nome} | Sexo: {sexo} | Nascimento: {nascimento} | "
          f"Peso: {peso}kg | Altura: {altura}m | Salário: R$ {salario_real:.2f} | "
          f"Nacionalidade: {nacionalidade}")

# -------------------------
# MOSTRAR ESTRUTURA
# -------------------------
print("\n Estrutura da tabela:")
cursor.execute("PRAGMA table_info(usuarios)")
estrutura = cursor.fetchall()

for coluna in estrutura:
    print(coluna)


conn.commit()  # Salva as mudanças no banco

conn.close()
