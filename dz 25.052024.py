import sqlite3

conn = sqlite3.connect('AnimalKingdom.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Animals (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Назва_звіра TEXT NOT NULL,
        Тип_звіра TEXT NOT NULL
    )
''')

animals = [
    ('Лев', 'Ссавець'),
    ('Крокодил', 'Плазун'),
    ('Орел', 'Птах'),
    ('Морська черепаха', 'Плазун'),
    ('Мавпа', 'Ссавець')
]

cursor.executemany('''
    INSERT INTO Animals (Назва_звіра, Тип_звіра)
    VALUES (?, ?)
''', animals)

cursor.execute('''
    UPDATE Animals
    SET Назва_звіра = 'Сокіл'
    WHERE Назва_звіра = 'Орел'
''')

cursor.execute('''
    SELECT * FROM Animals
    WHERE Тип_звіра = 'Ссавець'
''')
mammals = cursor.fetchall()
print("Звірі типу 'Ссавець':")
for mammal in mammals:
    print(mammal)

cursor.execute('''
    SELECT * FROM Animals
''')
all_animals = cursor.fetchall()
print("\nВсі записи про звірів:")
for animal in all_animals:
    print(animal)