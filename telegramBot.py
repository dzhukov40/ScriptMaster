# -*- coding: utf-8 -*-
from time import sleep

import config
import requests
import requests
import log
import enum

# this is HTTP API
# https://tlgrm.ru/docs/bots/api
# https://core.telegram.org/bots/api


offset = 0  # параметр необходим для подтверждения обновления
data = {'offset': 0, 'limit': 5, 'timeout': 0}


class State(enum.Enum):
    START = 1
    STOP = 2


class Bot:
    URL = 'https://api.telegram.org/bot'  # URL на который отправляется запрос
    token = ''
    startStopFlag = State.STOP

    # constructor
    def __init__(self, token):
        self.token = token
        self.startStopFlag = State.STOP
        log.info('CREATE instanse Bot: token = ' + token)

    # do request and get response
    def doRequest(self, method, sendData=None):
        try:
            url = self.URL + self.token + '/' + method
            log.debug('doRequest: url = ' + url + ' data = ')
            response = requests.post(url, sendData)  # собственно сам запрос
            log.debug('response' + response.text)
        except BaseException as e:
            log.error('Error request: method = ' + method + ' data = ' + sendData + e.message)
            return False

        if (not response.status_code == 200) or (not response.json()['ok']):
            log.error('Error response: status_code = ' + str(response.status_code) + ' json = ' + str(response.json()['ok']))

        return response

    # get bot information
    def getMe(self):
        return self.doRequest('getMe')

    # get Updates
    # sendData example
    # { 'offset': 1, 'limit': 0, 'timeout': 0, 'allowed_updates': ['message', 'edited_channel_post']}
    #
    # offset 	Integer 	Optional
    # -- Identifier of the first update to be returned. Must be greater by one than the highest among
    #    the identifiers of previously received updates. By default, updates starting with the earliest
    #    unconfirmed update are returned. An update is considered confirmed as soon as getUpdates is called
    #    with an offset higher than its update_id. The negative offset can be specified to retrieve updates
    #    starting from -offset update from the end of the updates queue. All previous updates will forgotten.
    #
    # limit 	Integer 	Optional
    # -- Limits the number of updates to be retrieved. Values between 1—100 are accepted. Defaults to 100.
    #
    # timeout 	Integer 	Optional
    # -- Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling. Should be positive,
    #    short polling should be used for testing purposes only.
    #
    # allowed_updates 	Array of String 	Optional
    # -- List the types of updates you want your bot to receive. For example,
    #    specify [“message”, “edited_channel_post”, “callback_query”] to only receive updates of these types.
    #    See Update for a complete list of available update types. Specify an empty list to receive all updates
    #    regardless of type (default). If not specified, the previous setting will be used.
    #
    #    Please note that this parameter doesn't affect updates created before the call to the getUpdates,
    #    so unwanted updates may be received for a short period of time.
    #
    #
    #
    def getUpdates(self, sendData=None):
        return self.doRequest('getUpdates', sendData)

    def startListen(self, func):

        self.startStopFlag = State.START
        # получаем сообщения по одному
        update = {'offset': 0, 'limit': 1, 'timeout': 0}

        while True:
            sleep(1)  # pause
            if self.startStopFlag == State.STOP:  # check loop status
                break

            res = self.getUpdates(update)  # try get one new message
            var = res.json()['result']

            if var:  # have new message
                update['offset'] = var[0]['update_id'] + 1  # update (offset)
                log.info('we get message = ' + str(var[0]))
                func(var[0])

    def stopListen(self):
        self.startStopFlag = State.STOP


if __name__ == '__main__':
    config = {"telegram_token": "416385445:AAEZI0_oRTg7FC5d4M0fWQqdYBEBvs6UBoI"}
