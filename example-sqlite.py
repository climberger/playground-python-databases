import sqlite3

conn = sqlite3.connect('quotes.db')
curr = conn.cursor()
curr.execute('CREATE TABLE IF NOT EXISTS quotes(text text, author text, tags text)')
curr.execute('INSERT INTO quotes VALUES ("Any text", "Fritz Mueller", "any_tag")')
conn.commit()
conn.close()