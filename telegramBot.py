# -*- coding: utf-8 -*-
import functools
import threading
from time import sleep

import config
import requests
import log
import enum

# this is HTTP API
# https://tlgrm.ru/docs/bots/api
# https://core.telegram.org/bots/api
from base import TelegramObject
from message import Message


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
    SEND_VIDEO = 'sendVideo'
    SEND_VOICE = 'sendVoice'
    SEND_VIDEO_NOTE = 'sendVideoNote'
    SEND_LOCATION = 'sendLocation'
    SEND_VENUE = 'sendVenue'
    SEND_CONTACT = 'sendContact'
    SEND_CHAT_ACTION = 'sendChatAction'


# send decorator
def message(func):
    @functools.wraps(func)
    def decorator(self, *args, **kwargs):

        # call decorated function (*) self this is class pointer
        url, data = func(self, *args, **kwargs)

        # get not required args
        if kwargs.get('disable_notification'):
            data['disable_notification'] = kwargs.get('disable_notification')

        if kwargs.get('reply_to_message_id'):
            data['reply_to_message_id'] = kwargs.get('reply_to_message_id')

        if kwargs.get('reply_markup'):
            data['reply_markup'] = kwargs.get('reply_markup')

        timeout = self.TIME_OUT_DEFAULT
        if kwargs.get('timeout'):
            timeout = kwargs.get('timeout')

        files = data.get('files')
        if files is not None:
            del data['files']


        log.debug('DO REQUESTS: url = ' + url + ', data = ' + str(data))
        result = requests.post(url, files=files, data=data, timeout=timeout)
        log.debug('GET RESPONSE: result = ' + result.text)

        if result is True:
            return result

        # return Message.de_json(result, self)
        return result

    return decorator


class Bot(TelegramObject):
    URL = 'https://api.telegram.org/bot'  # URL на который отправляется запрос
    WORK_URL = ''
    base_url = ''
    token = ''
    startStopFlag = State.STOP
    TIME_OUT_DEFAULT = 10
    # TIME_PAUSE = 0.3
    TIME_PAUSE = 2
    thread_ = threading.Thread

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
        self.base_url = self.URL + self.token
        log.info('setToken: token = ' + token)
        log.info('set WORK_URL: base_url = ' + self.base_url)

    # do request and get response
    def doRequest(self, method, files=None, data=None):
        response = 666
        try:
            log.debug(
                'doRequest: base_url = ' + self.base_url + method + ', files = ' + str(files) + ', data = ' + str(data))
            response = requests.post(self.base_url + '/' + method, files=files, data=data,
                                     timeout=self.TIME_OUT_DEFAULT)  # собственно сам запрос
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

    # check new message and if they exist, get them
    @message
    def getUpdates(self, data=None):

        url = '{0}/{1}'.format(self.base_url, Method.GET_UPDATES)

        return url, data

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
                log.info('WE GET MSG: ' + str(var[0]))
                func(var[0])  # call function

    # we can use for jon thread
    def join_(self):
        self.thread_.join()
        log.info('join thread')

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

    @message
    def sendMessage(self,
                    chat_id,
                    text,
                    parse_mode=None,
                    disable_web_page_preview=None,
                    **kwargs):

        url = '{0}/{1}'.format(self.base_url, Method.SEND_MESSAGE)
        data = {'chat_id': chat_id, 'text': text}

        if parse_mode is not None:
            data['parse_mode'] = parse_mode

        if disable_web_page_preview is not None:
            data['disable_web_page_preview'] = disable_web_page_preview

        return url, data

    # to send photo (*) do not see limits
    # photo: 1 - [ open('...', 'rb')) ], 2 - [ 'https://...') ], 3 - [ ... ]
    @message
    def sendPhoto(self, chat_id, photo, caption=None, **kwargs):

        url = '{0}/{1}'.format(self.base_url, Method.SEND_PHOTO)
        data = {'chat_id': chat_id}

        if isinstance(photo, file):  # 1 variant
            data['files'] = {'photo': photo}

        if isinstance(photo, str):  # 2 variant
            data['photo'] = photo

        # 3 variant (*) TODO: need have specific class
        # if isinstance(photo, class):

        if caption is not None:
            data['caption'] = caption

        return url, data

    # send audio (*) must be in the .mp3 format and not up to 50 MB
    # photo: 1 - [ open('...', 'rb')) ], 2 - [ 'https://...') ], 3 - [ ... ]
    @message
    def sendAudio(self, chat_id, audio, caption=None, duration=None, performer=None, title=None, **kwargs):

        url = '{0}/{1}'.format(self.base_url, Method.SEND_AUDIO)
        data = {'chat_id': chat_id}

        if isinstance(audio, file):  # 1 variant
            data['files'] = {'audio': audio}

        if isinstance(audio, str): # 2 variant
            data['audio'] = audio

        # 3 variant (*) TODO: need have specific class
        # if isinstance(audio, class):

        # maybe should have global params. For create methods global control
        if caption is not None:
            data['caption'] = caption
        if duration is not None:
            data['duration'] = duration
        if performer is not None:
            data['performer'] = performer
        if title is not None:
            data['title'] = title

        return url, data

    # send document (*) any file and any size
    # photo: 1 - [ open('...', 'rb')) ], 2 - [ 'https://...') ], 3 - [ ... ]
    def sendDocument(self,
                     chat_id,
                     document,
                     caption=None,
                     disable_notification=None,
                     reply_to_message_id=None,
                     reply_markup=None):

        # Required params
        data = {'chat_id': chat_id}
        files = {'document': document}

        # 1 variant (*) it is default case
        # if isinstance(audio, file):

        # 2 variant
        if isinstance(document, str):
            data['document'] = document
            files = None

        # 3 variant (*) TODO: need have specific class
        # if isinstance(audio, class):

        # maybe should have global params. For create methods global control
        if caption is not None:
            data['caption'] = caption
        if disable_notification is not None:
            data['disable_notification'] = disable_notification
        if reply_to_message_id is not None:
            data['reply_to_message_id'] = reply_to_message_id
        if reply_markup is not None:
            data['reply_markup'] = reply_markup

        # send data
        self.doRequest(Method.SEND_DOCUMENT, files=files, data=data)

    # send video (*) must be in the .mp4 format and not up to 50 MB
    # photo: 1 - [ open('...', 'rb')) ], 2 - [ 'https://...') ], 3 - [ ... ]
    def sendVideo(self,
                  chat_id,
                  video,
                  duration=None,
                  width=None,
                  height=None,
                  caption=None,
                  disable_notification=None,
                  reply_to_message_id=None,
                  reply_markup=None):

        # Required params
        data = {'chat_id': chat_id}
        files = {'video': video}

        # 1 variant (*) it is default case
        # if isinstance(video, file):

        # 2 variant
        if isinstance(video, str):
            data['document'] = video
            files = None

        # 3 variant (*) TODO: need have specific class
        # if isinstance(audio, class):

        # maybe should have global params. For create methods global control
        if duration is not None:
            data['duration'] = duration
        if width is not None:
            data['width'] = width
        if height is not None:
            data['height'] = height
        if caption is not None:
            data['caption'] = caption
        if disable_notification is not None:
            data['disable_notification'] = disable_notification
        if reply_to_message_id is not None:
            data['reply_to_message_id'] = reply_to_message_id
        if reply_markup is not None:
            data['reply_markup'] = reply_markup

        # send data
        self.doRequest(Method.SEND_VIDEO, files=files, data=data)

    # send voice (*) must be in the .ogg format and not up to 50 MB
    # photo: 1 - [ open('...', 'rb')) ], 2 - [ 'https://...') ], 3 - [ ... ]
    def sendVoice(self,
                  chat_id,
                  voice,
                  caption=None,
                  duration=None,
                  disable_notification=None,
                  reply_to_message_id=None,
                  reply_markup=None):

        # Required params
        data = {'chat_id': chat_id}
        files = {'voice': voice}

        # 1 variant (*) it is default case
        # if isinstance(voice, file):

        # 2 variant
        if isinstance(voice, str):
            data['voice'] = voice
            files = None

        # 3 variant (*) TODO: need have specific class
        # if isinstance(voice, class):

        # maybe should have global params. For create methods global control
        if caption is not None:
            data['caption'] = caption
        if duration is not None:
            data['duration'] = duration
        if disable_notification is not None:
            data['disable_notification'] = disable_notification
        if reply_to_message_id is not None:
            data['reply_to_message_id'] = reply_to_message_id
        if reply_markup is not None:
            data['reply_markup'] = reply_markup

        # send data
        self.doRequest(Method.SEND_VOICE, files=files, data=data)

    # send videoNote (*) must be in the .mp4 format and 1 minute long
    # photo: 1 - [ open('...', 'rb')) ], 2 - [ 'https://...') ], 3 - [ ... ]
    def sendVideoNote(self,
                      chat_id,
                      video_note,
                      duration=None,
                      length=None,
                      disable_notification=None,
                      reply_to_message_id=None,
                      reply_markup=None):

        # Required params
        data = {'chat_id': chat_id}
        files = {'video_note': video_note}

        # 1 variant (*) it is default case
        # if isinstance(video_note, file):

        # 2 variant
        if isinstance(video_note, str):
            data['video_note'] = video_note
            files = None

        # 3 variant (*) TODO: need have specific class
        # if isinstance(video_note, class):

        # maybe should have global params. For create methods global control
        if duration is not None:
            data['duration'] = duration
        if length is not None:
            data['length'] = length
        if disable_notification is not None:
            data['disable_notification'] = disable_notification
        if reply_to_message_id is not None:
            data['reply_to_message_id'] = reply_to_message_id
        if reply_markup is not None:
            data['reply_markup'] = reply_markup

        # send data
        self.doRequest(Method.SEND_VOICE, files=files, data=data)

    # send location (*)
    def sendLocation(self,
                     chat_id,
                     latitude,
                     longitude,
                     live_period=None,
                     disable_notification=None,
                     reply_to_message_id=None,
                     reply_markup=None):

        # Required params
        data = {'chat_id': chat_id, 'latitude': latitude, 'longitude': longitude}

        # maybe should have global params. For create methods global control
        if live_period is not None:
            data['live_period'] = live_period
        if disable_notification is not None:
            data['disable_notification'] = disable_notification
        if reply_to_message_id is not None:
            data['reply_to_message_id'] = reply_to_message_id
        if reply_markup is not None:
            data['reply_markup'] = reply_markup

        # send data
        self.doRequest(Method.SEND_LOCATION, data=data)


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
