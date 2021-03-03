from src.main.python.webAPI.client.protocol.REST import REST
from src.main.python.webAPI.client.security.NoneSecurity import NoneSecurity


class GoodReads(object):
    def __init__(self):
        self.__url = 'https://www.goodreads.com'
        security = NoneSecurity()
        self.rest = REST(security)

    def searchBook(self, queryText: str):
        command = "search: " + queryText
        url = self.__url + "/search/index.xml"
        return self.rest.sendGet(urlCommand = url, command = command)