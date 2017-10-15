# -*- coding: utf-8 -*-
import config
import requests
import requests
import log

# this is HTTP API
# https://core.telegram.org/bots/api


offset = 0  # параметр необходим для подтверждения обновления
data = {'offset': 0, 'limit': 5, 'timeout': 0}


class Bot:
    URL = 'https://api.telegram.org/bot'  # URL на который отправляется запрос
    token = ''

    # constructor
    def __init__(self, token):
        self.token = token
        log.info('CREATE instanse Bot: token = ' + token)

    # do request and get response
    def doRequest(self, method, sendData=None):
        try:
            url = self.URL + self.token + '/' + method
            log.error('doRequest: url = ' + url + ' data = ')
            response = requests.post(url, sendData)  # собственно сам запрос
            log.debug(response.text)
        except BaseException as e:
            log.error('Error request: method = ' + method + ' data = ' + sendData + e.message)
            return False

        if (not response.status_code == 200) or (not response.json()['ok']):
            log.error('Error response: status_code = ' + response.status_code + ' json = ' + response.json()['ok'])

        return response

    # get bot information
    def getMe(self):
        return self.doRequest('getMe')

    # get Updates
    def getUpdates(self, sendData=None):
        return self.doRequest('getUpdates', sendData)


if __name__ == '__main__':
    config = {"telegram_token": "416385445:AAEZI0_oRTg7FC5d4M0fWQqdYBEBvs6UBoI"}

