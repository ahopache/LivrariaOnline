"""
# encode: utf-8

class to use when no security is needed in API

"""
from src.main.python.webAPI.client.APISecurity import APISecurity


class NoneSecurity(APISecurity):
    def __init__(self):
        pass

    def getHeaderSecurityName(self):
        return ""

    def getHeaderSecurityValue(self):
        return ""


if __name__ == '__main__':
    main()
