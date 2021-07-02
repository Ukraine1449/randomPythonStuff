import database
from third import Book

def printmenu():
    printt = ("""
    Choose an option:
    1. Print all
    2. Get all with specific Name/Author/Pages
    3. Get one with specific Name/Author/Pages
    4. Get multiple with specific Name/Author/Pages
    5. Add a book
    6. Delete specific
    7. Clear table
    8. Update a specific one
    9. Close
    """)
    print(printt)


while True:
    printmenu()
    inputt = input()
    if inputt == "1":
        print(database.getall())
    elif inputt == "2":
        print('Please put the data type you want to find and the variable of it')
        inputy = input('Type: ')
        if inputy == 'Pages':
            inputyy = int(input('Var: '))
        else:
            inputyy = input('Var: ')
        database.selectspecificall(inputy, inputyy)
    elif inputt == "3":
        print('Please put the data type you want to find and the variable of it')
        inputy = input('Type: ')
        inputyy = input('Var: ')
        database.seletctspecificone(inputy, inputyy)
    elif inputt == "4":
        print(
            'Please put the data type you want to find and the variable of it, please also put the number of them you want')
        inputy = input('Type: ')
        inputyy = input('Var: ')
        inputyyy = input('How many: ')
        database.selectspecificmany(inputy, inputyy, int(inputyyy))
    elif inputt == "5":
        print('Please put title, author and pages of book')
        inputy = input('Title: ')
        inputyy = input('Author: ')
        inputyyy = input('Pages: ')
        database.add(inputy, inputyy, inputyyy)
    elif inputt == "6":
        print('Please put type and var')
        inputy = input('Type: ')
        inputyy = input('Var: ')
        database.deletespecific(inputy, inputyy)
    elif inputt == "7":
        inputt = input("Are you sure? Type y if you are sure.")
        if inputt.lower() == 'y':
            database.deleteall(True)
    elif inputt == "8":
        print('Please put what you want to replace typpe and var, then what you want to replace type and var')
        inputy = input('Type to replace: ')
        inputyy = input('Var to replace: ')
        inputyyy = input('Type: ')
        inputyyyy = input('Vara: ')
        database.update(inputy, inputyy, inputyyy, inputyyyy)
    elif inputt == "9":
        database.close()
    else:
        break
