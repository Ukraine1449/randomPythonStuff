class Book:
    favorites = []

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
        if self.pages > 100:
            return True
        return False

    def __str__(self):
        return f"{self.title} is {self.pages} pages long, by {self.author}"

    def __eq__(self, other):
        if self.title == other.title and self.author == other.author and self.pages == other.pages:
            return True
        else:
            return False
    # if this is mutable aka it is going to change do this: __hash__ = None

try:
    book = Book('Chiburashka', 'Someone who is eastern european', 72)
    book2 = Book('krokodil', 'Someone who is eastern european', 69)
    book3 = Book('krokodil', 'Someone who is eastern european', 69)
    print(book.title)
    print(book.is_long())
    Book.favorites.append(book)
    Book.favorites.append(book2)
    Book.favorites.append(book3)
    for b in Book.favorites:
        print(b)
    with open("Input.txt", "a") as file:
        file.write(f"\n {book.title}, {book.author}, {book.pages}")
    filer = open("Input.txt", "r")
    data = filer.read().split("\n")
    for i in range(0, len(data)):
        splitthing = data[int(i)].split(',')
        bookauthor = splitthing[1]
        bootitle = splitthing[0]
        bookpages = splitthing[2]
        print(bookpages)
        print(bookauthor)
        print(bootitle)
except FileNotFoundError as ee:
    print(ee)
except Exception as eee:
    print(eee)
    print('Cannot find.')
finally:
    file.close()
