import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER
)
''')
# cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
#
# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#                    (f"User{i}", f"example{i}@gmail.com", f"{i * 10}", "1000"))
# for i in range(1, 11):
#     if i % 2 != 0:
#         cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500, f'User{i}'))
# ids_to_delete = cursor.execute('''
# SELECT id FROM Users WHERE id % 3 = 1
# ''').fetchall()
# for (id_to_delete,) in ids_to_delete:
#     cursor.execute('''
#     DELETE FROM Users WHERE id = ?
#     ''', (id_to_delete,))
# cursor.execute('''
# SELECT username, email, age, balance FROM Users WHERE age != 60
# ''')
# results = cursor.fetchall()
# for username, email, age, balance in results:
#     print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

# cursor.execute('DELETE FROM Users WHERE id = ? ', (6,))
cursor.execute('SELECT SUM(balance) FROM Users')
total1 = cursor.fetchone()[0]
cursor.execute('SELECT COUNT(*) FROM Users')
total2 = cursor.fetchone()[0]
print(total1, total1/total2)

connection.commit()
connection.close()