"""
# encode: utf-8

interface for protocol types

This API only use REST in this project, but this class is necessary to facilitate
a future implementation of SOAP or another protocol type

"""

import requests

from src.main.python.webAPI.client.APISecurity import APISecurity


class APIClient(object):
    __listHeader: dict
    __security: APISecurity

    def __init__(self, security: APISecurity):
        super(APIClient, self).__init__()
        self.__security = security
        self.__listHeader = {}

    def addHeader(self, name: str, value: str):
        self.__listHeader[name] = value

    def sendPost(self, urlCommand: str, command: str):
        return requests.post(urlCommand, data = command, headers = self.__listHeader)

    def sendGet(self, urlCommand: str, command: str):
        return requests.get(urlCommand, data = command, headers = self.__listHeader)

    def sendPut(self, urlCommand: str, command: str):
        return requests.put(urlCommand, data = command, headers = self.__listHeader)

    def sendPatch(self, urlCommand: str, command: str):
        return requests.patch(urlCommand, data=command, headers=self.__listHeader)

    def sendDelete(self, urlCommand: str, command: str):
        return requests.delete(urlCommand, data=command, headers=self.__listHeader)


if __name__ == '__main__':
    main()
