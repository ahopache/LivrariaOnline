# encode: utf-8

import unittest

from src.main.python.webAPI.client.APIClient import APIClient
from src.main.python.webAPI.client.protocol.REST import REST
from src.main.python.webAPI.client.security.NoneSecurity import NoneSecurity


class checkREST(unittest.TestCase):
    def test_constructor(self):
        security = NoneSecurity()
        rest = REST(security)
        self.assertTrue(isinstance(rest, APIClient))

    def test_sendPost(self):
        url = 'https://w3schools.com/python/demopage.asp'
        command = ""
        security = NoneSecurity()
        rest = REST(security)
        response = rest.sendPost(url, command)
        self.assertTrue(response.status_code, 400)

    def test_sendGet(self):
        url = 'https://w3schools.com/python/demopage.asp'
        command = ""
        security = NoneSecurity()
        rest = REST(security)
        response = rest.sendGet(url, command)
        self.assertTrue(response.status_code, 400)

    def test_sendPatch(self):
        url = 'https://w3schools.com/python/demopage.asp'
        command = ""
        security = NoneSecurity()
        rest = REST(security)
        response = rest.sendPatch(url, command)
        self.assertTrue(response.status_code, 400)

    def test_sendPut(self):
        url = 'https://w3schools.com/python/demopage.asp'
        command = ""
        security = NoneSecurity()
        rest = REST(security)
        response = rest.sendPut(url, command)
        self.assertTrue(response.status_code, 400)

    def test_sendDelete(self):
        url = 'https://w3schools.com/python/demopage.asp'
        command = ""
        security = NoneSecurity()
        rest = REST(security)
        response = rest.sendDelete(url, command)
        self.assertTrue(response.status_code, 400)