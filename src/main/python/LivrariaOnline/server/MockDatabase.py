import csv
from datetime import date, timedelta
import pandas

from src.main.python.dataMining.OpenLibrary import OpenLibrary


class MockDatabase:
    def __init__(self, fileUsers: str = "users.csv", fileBooks: str = "books.csv"):
        self.__fileUsers = fileUsers
        self.__fileBooks = fileBooks

    def createUsersDatabase(self):
        dfUsers = pandas.DataFrame([["1", "Assis", "123"]], columns=["id", "user", "pass"])
        dfUsers = dfUsers.append(pandas.DataFrame([["2", "Joao", "123"]], columns=["id", "user", "pass"]))
        dfUsers = dfUsers.set_index("id")
        dfUsers.to_csv(path_or_buf=self.__fileUsers, sep=";", na_rep="", header=True)

    def createBooksDatabase(self):
        openLibrary = OpenLibrary()
        response = openLibrary.searchBookByAuthor("machado de assis", 1)
        dfBooksTemp = pandas.read_json(response.text)
        dfBooksTemp = dfBooksTemp['docs']
        dfBooks = pandas.DataFrame()
        for book in dfBooksTemp:
            dfTemp = pandas.DataFrame.from_dict(book.items()).set_index(0).T
            dfBooks = dfBooks.append(dfTemp, ignore_index=True)

        dfBooks = dfBooks[["title_suggest"]]
                          #"title",
                          #"subtitle",
                          #"subject",
                          #"isbn"
                          #"author_name",
                          #"publish_year",
                          #"language"
        dfBooks["rented_to"] = 0
        dfBooks["rented_status"] = "disponível"
        dfBooks["rented_date"] = ""
        dfBooks["penalty_rule"] = ""
        dfBooks.index.names = ['id']
        dfBooks.to_csv(path_or_buf=self.__fileBooks, sep=";", na_rep="", header=True, quoting=csv.QUOTE_ALL)
        self.setBookToUser("1", "1")
        self.setBookToUser("2", "1", date.today() - timedelta(days=1))
        self.setBookToUser("3", "1", date.today() - timedelta(days=2))
        self.setBookToUser("4", "1", date.today() - timedelta(days=3))
        self.setBookToUser("5", "1", date.today() - timedelta(days=4))
        self.setBookToUser("6", "1", date.today() - timedelta(days=5))
        self.setBookToUser("7", "1", date.today() - timedelta(days=6))
        self.setBookToUser("8", "1", date.today() - timedelta(days=7))
        self.setBookToUser("9", "1", date.today() - timedelta(days=8))
        self.setBookToUser("10","1", date.today() - timedelta(days=9))

    def isDatabaseExists(self, table: str):
        dfTeste = None
        try:
            dfTeste = pandas.read_csv(table, sep=";")
        except FileNotFoundError:
            dfTeste = None
        except Exception as e:
            print(f'erro ao carregar arquivo {table}: {e.__class__}')

        if dfTeste is None:
            return False
        else:
            return True

    def createDB(self):
        if not self.isDatabaseExists(self.__fileBooks):
            self.createBooksDatabase()

        if not self.isDatabaseExists(self.__fileUsers):
            self.createUsersDatabase()

    def getBooksUser(self, idUser: str ):
        dfBooks = self.__loadDfBooks()
        dfBooks = dfBooks.loc[dfBooks['rented_to'] == idUser]
        dfBooks = self.__updatePenaltyRule(dfBooks)
        dfBooks = dfBooks.astype({'rented_date': 'str'})
        return dfBooks.to_json().__str__()

    def getBooks(self):
        if not self.isDatabaseExists(self.__fileBooks):
            self.createBooksDatabase()
        return pandas.read_csv(self.__fileBooks, sep=";")[["id", "title_suggest", "rented_status"]].to_json().__str__()

    def setBookToUser(self, idBook: str, idUser: str, dt = date.today()):
        dfBooks = self.__loadDfBooks()
        dfBooks.loc[idBook, 'rented_to'] = idUser.isnumeric()
        dfBooks.loc[idBook, 'rented_status'] = 'emprestado'
        dfBooks.loc[idBook, 'rented_date'] = dt
        dfBooks['rented_to'] = pandas.to_numeric(dfBooks['rented_to'], errors='coerce')
        dfBooks.to_csv(path_or_buf=self.__fileBooks, sep=";", na_rep="", header=True, quoting=csv.QUOTE_ALL)
        return self.getBooksUser(idUser)

    def __loadDfUsers(self):
        if not self.isDatabaseExists(self.__fileUsers):
            self.createUsersDatabase()

        dfUsers = pandas.read_csv(self.__fileUsers, sep=";")
        dfUsers.columns = dfUsers.columns.str.replace('["]', '')
        dfUsers = dfUsers.astype({'pass': 'str'})
        dfUsers = dfUsers.astype({'id': 'str'})
        return dfUsers

    def __loadDfBooks(self):
        if not self.isDatabaseExists(self.__fileBooks):
            self.createBooksDatabase()
        dfBooks = pandas.read_csv(self.__fileBooks, sep=";")
        dfBooks.columns = dfBooks.columns.str.replace('["]', '')
        dfBooks = dfBooks.astype({'id': 'str'})
        dfBooks = dfBooks.astype({'rented_to': 'str'})
        dfBooks = dfBooks.astype({'penalty_rule': 'str'})
        dfBooks['rented_date'] = pandas.to_datetime(dfBooks['rented_date'])
        dfBooks = dfBooks.set_index("id")
        return  dfBooks

    def __updatePenaltyRule(self, dfBooks):
        dfBooks.loc[dfBooks['rented_date'] <= pandas.to_datetime(date.today() - timedelta(days=3)), ['penalty_rule']] = ''
        dfBooks.loc[(dfBooks['rented_date'] >= pandas.to_datetime(date.today() - timedelta(days=6))) &
               (dfBooks['rented_date'] < pandas.to_datetime(date.today() - timedelta(days=3))), ['penalty_rule']] = 'Até 3 dias atraso, Multa = 3%, Juros ao Dia = 0.2%'
        dfBooks.loc[(dfBooks['rented_date'] >= pandas.to_datetime(date.today() - timedelta(days=8))) &
                    (dfBooks['rented_date'] < pandas.to_datetime(date.today() - timedelta(days=6))), ['penalty_rule']] = 'Até 5 dias atraso, Multa = 5%, Juros ao Dia = 0.4%'
        dfBooks.loc[dfBooks['rented_date'] < pandas.to_datetime(date.today() - timedelta(days=8)), ['penalty_rule']] = 'Acima 5 dias atraso, Multa = 7%, Juros ao Dia = 0.6%'
        return dfBooks

    def login(self, user, password):
        dfUsers = self.__loadDfUsers()
        dfUsers = dfUsers.loc[dfUsers['user'].str.lower() == user.lower()]
        dfUsers = dfUsers.loc[dfUsers['pass'] == password]
        if dfUsers.size > 0:
            return dfUsers.iloc[0]['id']
        else:
            return False


if __name__ == '__main__':
    main()
