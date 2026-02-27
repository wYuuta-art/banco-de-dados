import sqlite3

conn = sqlite3.connect('cursos.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS cursos(
    idcurso INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE,
    descricao TEXT,
    carga INTEGER CHECK (carga >= 0),
    totalaulas INTEGER ,
    ano TEXT DEFAULT CURRENT_DATE
)
''')

cursor.executemany(
    '''
    INSERT INTO cursos
    (nome, descricao, carga, totalaulas, ano)
    VALUES (?, ?, ?, ?, ?) 
    ''',
    [
            ('Computacao', 'computadores', 19, 20, '2025'),
            ('Direito', 'Curso de advogados', 30, 20, '2025'),
    ]
)



cursor.execute('PRAGMA table_info(cursos)')
estrut = cursor.fetchall()

for n in estrut:
    print(n)

conn.commit()
conn.close()