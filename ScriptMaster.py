# -*- coding: utf-8 -*-
import ConfigParser

import logging.handlers
import json

from dah_telegram import Bot, Update
from dah_telegram.available_types.inlineKeyboardButton import InlineKeyboardButton
from dah_telegram.available_types.inlineKeyboardMarkup import InlineKeyboardMarkup

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

        inlineKeyboardButton1 = InlineKeyboardButton(text='1', url='http://ya.ru')
        inlineKeyboardButton2 = InlineKeyboardButton(text='2', url='http://ya.ru')
        inlineKeyboardButton3 = InlineKeyboardButton(text='3', url='http://ya.ru')
        inlineKeyboardButton4 = InlineKeyboardButton(text='4', url='http://ya.ru')
        arrayButtons1 = [inlineKeyboardButton1, inlineKeyboardButton2]
        arrayButtons2 = [inlineKeyboardButton3, inlineKeyboardButton4]
        inlineKeyboardMarkup1 = InlineKeyboardMarkup(inline_keyboard=[arrayButtons1, arrayButtons2])
        inlineKeyboardMarkup2 = InlineKeyboardMarkup(inline_keyboard=[arrayButtons1, arrayButtons2])

        bot.sendMessage(chatId, chatText, reply_markup=inlineKeyboardMarkup1.jsonConvert())
        bot.sendMessage(chatId, chatText, reply_markup=inlineKeyboardMarkup2.jsonConvert())


        #inlineKeyboardMarkup2.arrayConvert()

        #inlineKeyboardMarkup1 = json.dumps(inlineKeyboardMarkup1)
        #inlineKeyboardMarkup2 = json.dumps(inlineKeyboardMarkup2)

        #bot.sendMessage(chatId, chatText, reply_markup=inlineKeyboardMarkup1)
        #bot.sendMessage(chatId, chatText, reply_markup=inlineKeyboardMarkup2)


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
