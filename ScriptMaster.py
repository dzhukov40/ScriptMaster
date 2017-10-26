# -*- coding: utf-8 -*-
import ConfigParser

import logging.handlers

from dah_telegram import Bot, Update

CONFIG_PATH = "config.ini"


bot = Bot()
config = {}


def readConfig(path):
    global config

    parseConfig = ConfigParser.ConfigParser()
    parseConfig.read(path)
    config['telegram_token'] = parseConfig.get("telegram", "telegram_token")


def tort(msg):

    # check type. Must be to indicate type!
    if isinstance(msg, Update):

        chatId = msg.message.chat.chat_id
        chatText = msg.message.text

        msg.message.chat.test()

        print ' msg.chat.chat_id = ' + str(chatId)
        # print ' msg.message.text = ' + str(chatText)

        bot.sendMessage(chatId, chatText)

    # messageChatId = BotUtility.getMessageChatId(msg)

    # bot.sendMessage(messageChatId, 'приветики')
    # bot.sendPhoto(messageChatId, open('test_data/Photo_1.jpg', 'rb'), caption='тетя')
    # bot.sendPhoto(messageChatId, 'http://dummyimage.com/600x400/000/fff.png&text=telegram')
    #
    # bot.sendAudio(messageChatId, open('test_data/Song_2.mp3', 'rb'))
    # bot.sendAudio(messageChatId, 'https://python-telegram-bot.org/static/testfiles/telegram.mp3')
    #
    # bot.sendDocument(messageChatId, open('test_data/File_1.txt', 'rb'))
    # bot.sendDocument(messageChatId, 'http://lelang.ru/wp-content/pdf_noindex_medium/Eveline.pdf')
    #
    # bot.sendVideo(messageChatId, open('test_data/Video_1.mp4', 'rb'))
    # bot.sendAudio(messageChatId, 'https://python-telegram-bot.org/static/testfiles/telegram.mp4')
    #
    # bot.sendVoice(messageChatId, open('test_data/Voice_1.ogg', 'rb'))
    # bot.sendVoice(messageChatId, 'https://python-telegram-bot.org/static/testfiles/telegram.ogg')
    #
    # bot.sendVideoNote(messageChatId, open('test_data/Video_1.mp4', 'rb'))
    # bot.sendVideoNote(messageChatId, 'https://python-telegram-bot.org/static/testfiles/telegram.mp4')

    # bot.sendLocation(messageChatId, 55.807255, 37.621902)

    # 'https://python-telegram-bot.org/static/testfiles/telegram.jpg'
    # 'https://python-telegram-bot.org/static/testfiles/telegram.gif'
    # 'https://python-telegram-bot.org/static/testfiles/telegram.mp4'
    # 'https://python-telegram-bot.org/static/testfiles/telegram.ogg'
    # 'https://python-telegram-bot.org/static/testfiles/telegram.webp'

    # bot.stopListen()


def main():

    readConfig(CONFIG_PATH)

    # TODO: надо вытащить из config.ini параметры логирования
    LOG_FILENAME = "ScriptMaster.log"
    DEBUG_LEVEL = logging.INFO  # ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
    LOG_FORMAT = "%(levelname)-8s [%(asctime)s] [%(thread)d : %(funcName)s] %(message)s"
    ROTATE_HANDLER = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=9000000, backupCount=5)

    logging.basicConfig(filename=LOG_FILENAME, level=DEBUG_LEVEL, format=LOG_FORMAT, handler=ROTATE_HANDLER)

    logging.info('read config ' + CONFIG_PATH)
    logging.info('readConfig ' + str(config))

    global bot
    bot.setToken(config['telegram_token'])

    # print (bot.getMe().text)
    # need registration list of functions !!!
    # and add or delite in work time
    bot.startListen(tort, False)
    print ('основной поток дотопал до конца')

    bot.join_


if __name__ == '__main__':
    main()
