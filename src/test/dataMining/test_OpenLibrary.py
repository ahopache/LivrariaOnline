import unittest

from src.main.python.dataMining.OpenLibrary import OpenLibrary


class test_OpenLibrary(unittest.TestCase):
    def test_constructor(self):
        openLibrary = OpenLibrary()

        self.assertTrue(isinstance(openLibrary, OpenLibrary))

    def test_getBooks(self):
        openLibrary = OpenLibrary()

        response = openLibrary.searchBookByAuthor("machado de assis", 1)
        self.assertEqual(response.status_code, 200)
