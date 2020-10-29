"""
# encode: utf-8

Class for DataMining data from OpenLibrary

"""
from src.main.python.webAPI.client.protocol.REST import REST
from src.main.python.webAPI.client.security.NoneSecurity import NoneSecurity


class OpenLibrary(object):
    def __init__(self):
        self.__url = 'https://openlibrary.org'
        security = NoneSecurity()
        self.rest = REST(security)

    def searchBookByTitle(self, queryText: str, page: int):
        url = self.__url + "/search.json?title=" + queryText + "&page=" + str(page)
        return self.rest.sendGet(urlCommand = url, command = "")

    def searchBookByAuthor(self, queryText: str, page: int):
        url = self.__url + "/search.json?author=" + queryText + "&page=" + str(page)
        return self.rest.sendGet(urlCommand = url, command = "")


if __name__ == '__main__':
    main()
