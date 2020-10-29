import unittest

import pandas

from src.main.python.LivrariaOnline.server.MockDatabase import MockDatabase


class test_MockBooks(unittest.TestCase):
    def test_createDBUsers(self):
        db = MockDatabase("test_users.csv", "test_books.csv")
        db.createUsersDatabase()
        dfUsers = pandas.read_csv("test_users.csv", sep=";")
        self.assertGreater(len(dfUsers), 0)

    def test_createDBBooks(self):
        db = MockDatabase("test_users.csv", "test_books.csv")
        db.createBooksDatabase()
        dfUsers = pandas.read_csv("test_books.csv", sep=";")
        self.assertGreater(len(dfUsers), 0)

    def test_getBooksUser(self):
        db = MockDatabase("test_users.csv", "test_books.csv")
        id_client = 1
        response = db.getBooksUser(id_client)
        self.assertIn('title_suggest', response)

    def test_getBooks(self):
        db = MockDatabase("test_users.csv", "test_books.csv")
        response = db.getBooks()
        self.assertIn('title_suggest', response)

    def test_setBookToUser(self):
        db = MockDatabase("test_users.csv", "test_books.csv")
        idBook = "98"
        idUser = "1"
        response = db.setBookToUser(idBook, idUser)
        self.assertIn('emprestado', response)

    def test_login(self):
        db = MockDatabase("test_users.csv", "test_books.csv")
        usr = "assis"
        psw = "123"
        response = db.login(usr, psw)
        self.assertEqual(response, "1")
        psw = "1"
        response = db.login(usr, psw)
        self.assertEqual(response, 0)
