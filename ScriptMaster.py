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
