from src.main.python.LivrariaOnline.server.MockDatabase import MockDatabase


class Database:
    def __init__(self):
        self.db = MockDatabase()

    def getBooksUser(self, idUser: str):
        return self.db.getBooksUser(idUser)

    def getBooks(self):
        return self.db.getBooks()

    def setBookToUser(self, idBook: str, idUser: str):
        return self.db.setBookToUser(idBook, idUser)

    def login(self, user: str, password: str):
        return self.db.login(user, password)


if __name__ == '__main__':
    main()
