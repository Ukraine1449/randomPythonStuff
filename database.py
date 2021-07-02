import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()
c.execute(f"CREATE TABLE IF NOT EXISTS Books (Title TEXT, Author Text, Pages int)")


def add(Title, Author, Pages):
    c.execute(f'INSERT INTO Books Values ("{Title}", "{Author}", {Pages})')
    conn.commit()


def getall():
    c.execute('SELECT * FROM Books')
    conn.commit()
    return c.fetchall()


def insertmultiple(tuple):
    c.executemany('INSERT INTO Books VALUES(?, ?, ?)', tuple)
    conn.commit()


def selectspecificall(Where, What):
    print(Where, What)
    if Where == "Pages":
        c.execute(f'SELECT * FROM Books WHERE {Where}="{What}"')
    else:
        c.execute(f'SELECT * FROM Books WHERE {Where}="{What}"')
    print(c.fetchall())


def seletctspecificone(Where, What):
    if Where == "Pages":
        c.execute(f'SELECT * FROM Books WHERE {Where}={What}')
    else:
        c.execute(f'SELECT * FROM Books WHERE {Where}="{What}"')
    return c.fetchone()


def selectspecificmany(Where, What, Howmany):
    if Where == "Pages":
        c.execute(f'SELECT * FROM Books WHERE {Where}={What}')
    else:
        c.execute(f'SELECT * FROM Books WHERE {Where}="{What}"')
    return c.fetchmany(Howmany)


def deletespecific(Where, What):
    if Where == "Pages":
        c.execute(f'DELETE FROM Books WHERE {Where}={What}')
    else:
        c.execute(f'DELETE FROM Books WHERE {Where}="{What}"')
    conn.commit()


def deleteall(Confirm):
    if Confirm:
        c.execute('DELETE FROM Books')


def update(SetType, SetData, From, FromData):
    if SetType == 'Pages':
        int(SetData)
        c.execute(f'UPDATE Books SET {SetType}={SetData} WHERE {From}="{FromData}"')
    if From == "Pages":
        int(FromData)
        c.execute(f'UPDATE Books SET {SetType}="{SetData}" WHERE {From}={FromData}')
    c.execute(f'UPDATE Books SET {SetType}="{SetData}" WHERE {From}="{FromData}"')


def close():
    c.connection.close()


books = [
    ('Mumitrol', 'Idk', 72),
    ('No clue', 'Me', 69),
    ('Test', 'someone', 420)
]
insertmultiple(books)
add('Chiburashka', 'Someone', 65)
print(selectspecificmany("Title", "Mumitrol", 2))
update("Title", "Boogaloo book", "Title", "Mumitrol")
print(getall())
# c.execute('UPDATE Books SET Title="Mumitrol updated" WHERE Title="Mumitrol"')
# conn.commit()
