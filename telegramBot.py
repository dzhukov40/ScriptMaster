# -*- coding: utf-8 -*-
import threading
from time import sleep

import config
import requests
import requests
import log
import enum

# this is HTTP API
# https://tlgrm.ru/docs/bots/api
# https://core.telegram.org/bots/api


class State(enum.Enum):
    START = 1
    STOP = 2


# method names
class Method(enum.Enum):
    GET_ME = 'getMe'
    GET_UPDATES = 'getUpdates'
    SEND_MESSAGE = 'sendMessage'
    SEND_PHOTO = 'sendPhoto'
    SEND_AUDIO = 'sendAudio'
    SEND_DOCUMENT = 'sendDocument'


class Bot:
    URL = 'https://api.telegram.org/bot'  # URL на который отправляется запрос
    WORK_URL = ''
    token = ''
    startStopFlag = State.STOP
    TIME_OUT = 10
    TIME_PAUSE = 0.3
    thread_ = threading

    # constructor
    def __init__(self, token=''):
        if token is not '':
            self.setToken(token)
        self.token = token
        self.startStopFlag = State.STOP
        log.info('CREATE instance Bot: token = ' + token)

    # for work need telegram token
    def setToken(self, token):
        self.token = token
        self.WORK_URL = self.URL + self.token + '/'
        log.info('setToken: token = ' + token)
        log.info('set WORK_URL: WORK_URL = ' + self.WORK_URL)

    # do request and get response
    def doRequest(self, method, files=None, data=None):
        response = 666
        try:
            log.debug(
                'doRequest: WORK_URL = ' + self.WORK_URL + method + ', files = ' + str(files) + ', data = ' + str(data))
            response = requests.post(self.WORK_URL + method, files=files, data=data,
                                     timeout=self.TIME_OUT)  # собственно сам запрос
            log.debug('getResponse' + response.text)
        except BaseException as e:
            log.error('Error request: method = ' + method + ', data = ' + str(data) + ', e = ' + str(e))
            return response

        if response.status_code != 200:
            log.error('Error response: status_code = ' + str(response.status_code) + ', response = ' + response.text)

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
    def getUpdates(self, sendData=None):
        return self.doRequest(Method.GET_UPDATES, data=sendData)

    # this method for loop request new message
    def worker(self, func):
        if self.token == '':
            log.error('you must set token')
            return 'you must set token'

        self.startStopFlag = State.START

        # we get message one by one
        update = {'offset': 0, 'limit': 1, 'timeout': 0}

        # loop
        while True:
            sleep(self.TIME_PAUSE)  # pause
            if self.startStopFlag == State.STOP:  # check loop status
                break

            res = self.getUpdates(update)  # try get one new message
            var = res.json()['result']

            if var:  # have new message
                update['offset'] = var[0]['update_id'] + 1  # update (offset)
                log.info('we get message = ' + str(var[0]))
                func(var[0])  # call function

    # this function can work in same or different thread then (fork=True)
    def startListen(self, func, fork=False):
        if fork is True:
            self.thread_ = threading.Thread(target=self.worker, args=[func])  # заметь квадратные скобки!!!
            self.thread_.start()
        else:
            self.worker(func)

    # we wont stop infinity loop
    def stopListen(self):
        self.startStopFlag = State.STOP

    # send text message
    def sendMessage(self,
                    chat_id,
                    text,
                    parse_mode=None,
                    disable_web_page_preview=None,
                    disable_notification=None,
                    reply_to_message_id=None,
                    reply_markup=None):

        message = {'chat_id': chat_id,
                   'text': text,
                   'parse_mode': parse_mode,
                   'disable_web_page_preview': disable_web_page_preview,
                   'disable_notification': disable_notification,
                   'reply_to_message_id': reply_to_message_id,
                   'reply_markup': reply_markup}

        self.doRequest(Method.SEND_MESSAGE, data=message)

    # send photo example [ sendPhoto(3, open('1.jpg', 'rb')) ]
    def sendPhoto(self,
                  chat_id,
                  photo,
                  caption=None,
                  disable_notification=None,
                  reply_to_message_id=None):

        # if isinstance(photo, file):
        data = {'chat_id': chat_id,
                'caption': caption,
                'disable_notification': disable_notification,
                'reply_to_message_id': reply_to_message_id}
        files = {'photo': photo}

        if isinstance(photo, str):
            data = {'chat_id': chat_id, 'photo': photo}
            files = None

        self.doRequest(Method.SEND_PHOTO, files=files, data=data)

    # send audio example [ sendAudio(3, open('song.mp3', 'rb')) ]
    def sendAudio(self,
                  chat_id,
                  audio,
                  caption=None,
                  duration=None,
                  performer=None,
                  title=None,
                  disable_notification=None,
                  reply_to_message_id=None,
                  reply_markup=None):

        # if isinstance(photo, file):
        data = {'chat_id': chat_id,
                'caption': caption,
                'duration': duration,
                'performer': performer,
                'title': title,
                'disable_notification': disable_notification,
                'reply_to_message_id': reply_to_message_id,
                'reply_markup': reply_markup}
        files = {'audio': audio}

        if isinstance(audio, str):
            data = {'chat_id': chat_id, 'audio': audio}
            files = None

        self.doRequest(Method.SEND_AUDIO, files=files, data=data)


# class for help use Bot methods
class BotUtility:
    def __init__(self):
        pass

    # get id chat from msg
    @staticmethod
    def getMessageChatId(msg):
        return msg['message']['chat']['id']


if __name__ == '__main__':
    config = {"telegram_token": "416385445:AAEZI0_oRTg7FC5d4M0fWQqdYBEBvs6UBoI"}
