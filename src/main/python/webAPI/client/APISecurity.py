"""
# encode: utf-8

interface for security types

This API doesn't need security in this project, but this class is necessary to facilitate
a future implementation of OAUTH or other security

"""
from abc import abstractmethod


class APISecurity(object):
    def __init__(self):
        pass

    @abstractmethod
    def getHeaderSecurityName(self):
        return None

    @abstractmethod
    def getHeaderSecurityValue(self):
        return None


if __name__ == '__main__':
    main()
