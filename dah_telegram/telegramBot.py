# -*- coding: utf-8 -*-
import functools
import json
import threading
import logging
from time import sleep

import enum
import requests

from dah_telegram import Update


# this is HTTP API
# https://tlgrm.ru/docs/bots/api
# https://core.telegram.org/bots/api

# logging.getLogger(__name__).addHandler(logging.NullHandler())
logger = logging.getLogger(__name__)


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


# забыл, зачем создавал))) это вообще вроде возможные значения квакогото параметра
class ChatAction(enum.Enum):
    UPLOAD_PHOTO = 'upload_photo'
    UPLOAD_VIDEO = 'upload_video'
    UPLOAD_AUDIO = 'upload_audio'
    UPLOAD_DOCUMENT = 'upload_document'
    FIND_LOCATION = 'find_location'
    RECORD_VIDEO_NOTE = 'record_video_note'
    UPLOAD_VIDEO_NOTE = 'upload_video_note'


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

        logger.info('DO REQUESTS: url = ' + url + ', data = ' + str(data))
        response = requests.post(url, files=files, data=data, timeout=timeout)
        logger.info('GET RESPONSE: result = ' + response.text)

        if (response.status_code != 200) and (not response.json()['ok']):
            logger.error('Error response: status_code = ' + str(response.status_code) + ', response = ' + response.text)

        return response.json()['result']

    return decorator


# TODO: maybe we must use extending (*) create base class
class Bot:
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
        logger.info('CREATE instance Bot: token = ' + token)

    # for work need telegram token
    def setToken(self, token):
        self.token = token
        self.base_url = self.URL + self.token
        logger.info('setToken: token = ' + token)
        logger.info('set WORK_URL: base_url = ' + self.base_url)

    # get bot information
    @message
    def getMe(self):

        url = '{0}/{1}'.format(self.base_url, Method.GET_ME)

        return url

    # метод работает как остальные
    @message
    def getCleanUpdates(self, data=None):

        url = '{0}/{1}'.format(self.base_url, Method.GET_UPDATES)

        return url, data

    # check new message and if they exist, get them
    # [!] return list objects Update
    def getUpdates(self, data=None):

        update = self.getCleanUpdates(data)

        if not update:
            return None

        resultList = []

        for entity in update:
            resultList.append(Update.jsonConstructor(entity, self))

        return resultList

    # this method for loop request new message
    def worker(self, func):
        if self.token == '':
            logger.error('you must set token')
            return 'you must set token'

        self.startStopFlag = State.START

        # we get message one by one
        data = {'offset': 0, 'limit': 1, 'timeout': 0}

        # loop
        while True:
            sleep(self.TIME_PAUSE)  # pause
            if self.startStopFlag == State.STOP:  # check loop status
                break

            # try get one new message, only one on the list
            update = self.getUpdates(data)

            # TODO: must use UpdateType

            # print '---\n' + str(update) + '\n---'


            # var = res.json()['result']
            #
            if (update is not None) and (update is not []):  # have new message
                data['offset'] = update[0].update_id + 1  # update (offset)
                func(update[0])  # call function




    # we can use for jon thread
    def join_(self):
        self.thread_.join()
        logger.info('join thread')

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
    def sendMessage(self, chat_id, text, parse_mode=None, disable_web_page_preview=None, **kwargs):

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

    # send audio (*) must be in the .mp3 format and up to 50 MB
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

        if caption is not None:
            data['caption'] = caption
        if duration is not None:
            data['duration'] = duration
        if performer is not None:
            data['performer'] = performer
        if title is not None:
            data['title'] = title

        return url, data

    # send document (*) any file type and up to 50 MB
    # document: 1 - [ open('...', 'rb')) ], 2 - [ 'https://...') ], 3 - [ ... ]
    @message
    def sendDocument(self, chat_id, document, caption=None, **kwargs):

        url = '{0}/{1}'.format(self.base_url, Method.SEND_DOCUMENT)
        data = {'chat_id': chat_id}

        if isinstance(document, file):  # 1 variant
            data['files'] = {'document': document}

        if isinstance(document, str):  # 2 variant
            data['document'] = document

        # 3 variant (*) TODO: need have specific class
        # if isinstance(document, class):

        if caption is not None:
            data['caption'] = caption

        return url, data

    # send video (*) must be in the .mp4 format and up to 50 MB
    # video: 1 - [ open('...', 'rb')) ], 2 - [ 'https://...') ], 3 - [ ... ]
    @message
    def sendVideo(self, chat_id, video, duration=None, width=None, height=None, caption=None, **kwargs):

        url = '{0}/{1}'.format(self.base_url, Method.SEND_VIDEO)
        data = {'chat_id': chat_id}

        if isinstance(video, file):  # 1 variant
            data['files'] = {'video': video}

        if isinstance(video, str):  # 2 variant
            data['video'] = video

        # 3 variant (*) TODO: need have specific class
        # if isinstance(video, class):

        if duration is not None:
            data['duration'] = duration

        if width is not None:
            data['width'] = width

        if height is not None:
            data['height'] = height

        if caption is not None:
            data['caption'] = caption

        return url, data

    # send voice (*) must be in the .ogg format and up to 50 MB
    # voice: 1 - [ open('...', 'rb')) ], 2 - [ 'https://...') ], 3 - [ ... ]
    @message
    def sendVoice(self, chat_id, voice, caption=None, duration=None, **kwargs):

        url = '{0}/{1}'.format(self.base_url, Method.SEND_VOICE)
        data = {'chat_id': chat_id}

        if isinstance(voice, file):  # 1 variant
            data['files'] = {'voice': voice}

        if isinstance(voice, str):  # 2 variant
            data['voice'] = voice

        # 3 variant (*) TODO: need have specific class
        # if isinstance(voice, class):

        if caption is not None:
            data['caption'] = caption

        if duration is not None:
            data['duration'] = duration

        return url, data

    # send videoNote (*) must be in the .mp4 format and 1 minute long
    # videoNote: 1 - [ open('...', 'rb')) ], 2 - [ 'https://...') ], 3 - [ ... ]
    @message
    def sendVideoNote(self, chat_id,  video_note, duration=None, length=None, **kwargs):

        url = '{0}/{1}'.format(self.base_url, Method.SEND_VIDEO_NOTE)
        data = {'chat_id': chat_id}

        if isinstance(video_note, file):  # 1 variant
            data['files'] = {'video_note': video_note}

        if isinstance(video_note, str):  # 2 variant
            data['video_note'] = video_note

        # 3 variant (*) TODO: need have specific class
        # if isinstance(video_note, class):

        if duration is not None:
            data['duration'] = duration

        if length is not None:
            data['length'] = length

        return url, data

    @message
    def sendLocation(self, chat_id, latitude, longitude, live_period=None, **kwargs):

        url = '{0}/{1}'.format(self.base_url, Method.SEND_LOCATION)
        data = {'chat_id': chat_id, 'latitude': latitude, 'longitude': longitude}

        if live_period is not None:
            data['live_period'] = live_period

        return url, data

    @message
    def sendVenue(self, chat_id, latitude, longitude, title, address, foursquare_id, **kwargs):

        url = '{0}/{1}'.format(self.base_url, Method.SEND_VENUE)
        data = {'chat_id': chat_id, 'latitude': latitude, 'longitude': longitude}

        if title is not None:
            data['title'] = title

        if address is not None:
            data['address'] = address

        if foursquare_id is not None:
            data['foursquare_id'] = foursquare_id

        return url, data

    @message
    def sendContact(self, chat_id, phone_number, first_name, last_name, **kwargs):

        url = '{0}/{1}'.format(self.base_url, Method.SEND_CONTACT)
        data = {'chat_id': chat_id, 'phone_number': phone_number, 'first_name': first_name, 'last_name': last_name}

        return url, data

    # action must be type [ ChatAction ]
    @message
    def sendChatAction(self, chat_id, action, **kwargs):

        url = '{0}/{1}'.format(self.base_url, Method.SEND_CHAT_ACTION)
        data = {'chat_id': chat_id, 'action': action}

        return url, data


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
