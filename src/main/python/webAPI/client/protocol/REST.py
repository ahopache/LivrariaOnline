"""
# encode: utf-8

class for send API using REST protocol

"""
from src.main.python.webAPI.client.APIClient import APIClient
from src.main.python.webAPI.client.APISecurity import APISecurity


class REST(APIClient):
    def __init__(self, security: APISecurity):
        self.security = security
        super(REST, self).__init__(security)
        self.__setHeaders()

    def __setHeaders(self):
        super(REST, self).addHeader("Accept", "application/json")
        super(REST, self).addHeader("Accept-Encoding", "[gzip, deflate, br]")
        super(REST, self).addHeader("Accept-Language", "[pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7]")
        super(REST, self).addHeader("Cache-Control", "no-cache")
        super(REST, self).addHeader("Connection", "keep-alive")
        super(REST, self).addHeader("Content-Type", "application/json")
        super(REST, self).addHeader("charset", "UTF-8")

        if self.security.getHeaderSecurityName() != "":
            super(REST, self).addHeader(self.security.getHeaderSecurityName(), self.security.getHeaderSecurityValue())


if __name__ == '__main__':
    main()
