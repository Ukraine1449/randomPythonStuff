import mysql.connector as mysql

# enter your server IP address/domain name
HOST = "bgdgjgpghhdzmphd3gih-mysql.services.clever-cloud.com"  # or "domain.com"
# database name, if you want just to connect to MySQL server, leave it empty
DATABASE = "bgdgjgpghhdzmphd3gih"
# this is the user you create
USER = "ui80qmoqohetyn03"
# user password
PASSWORD = "MLFzq9sRBi5LvPV1T0Q2"
# connect to MySQL server
db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
print("Connected to:", db_connection.get_server_info())
c = db_connection.cursor()
c.execute('CREATE TABLE IF NOT EXISTS Clothes (Type TEXT, Number int)')


def additem(item, howmany):
    c.execute(f'INSERT INTO Clothes Values ("{item}", "{howmany}")')
    db_connection.commit()


def update(SetType, SetData, From, FromData):
    c.execute(f'UPDATE Clothes SET {SetType}="{SetData}" WHERE {From}={FromData}')
    db_connection.commit()


additem('tshirt', 5)
additem('swim things', 1)
additem('pairs of socks', 12)
additem('jeans', 1)
additem('shorts', 1)
additem('Warm coat', 1)
additem('jacket', 1)
additem('home pants', 1)
additem('home shorts', 1)