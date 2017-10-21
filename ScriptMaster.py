# -*- coding: utf-8 -*-
import ConfigParser

from telegramBot import Bot
from telegramBot import BotUtility
import log


CONFIG_PATH = "config.ini"

bot = Bot()
config = {}


def readConfig(path):
    global config

    parseConfig = ConfigParser.ConfigParser()
    parseConfig.read(path)
    config['telegram_token'] = parseConfig.get("telegram", "telegram_token")
    log.info('readConfig ' + str(config))


def tort(msg):

    messageChatId = BotUtility.getMessageChatId(msg)

    bot.sendMessage(messageChatId, 'приветики')
    bot.sendPhoto(messageChatId, open('test_data/Photo_1.jpg', 'rb'), caption='тетя')
    bot.sendPhoto(messageChatId, 'http://dummyimage.com/600x400/000/fff.png&text=telegram')
    bot.sendAudio(messageChatId, open('test_data/Song_2.mp3', 'rb'))
    bot.sendAudio(messageChatId, 'https://python-telegram-bot.org/static/testfiles/telegram.mp3')

    # 'https://python-telegram-bot.org/static/testfiles/telegram.jpg'
    # 'https://python-telegram-bot.org/static/testfiles/telegram.gif'
    # 'https://python-telegram-bot.org/static/testfiles/telegram.mp4'
    # 'https://python-telegram-bot.org/static/testfiles/telegram.ogg'
    # 'https://python-telegram-bot.org/static/testfiles/telegram.webp'

    # bot.stopListen()


def main():
    readConfig(CONFIG_PATH)
    log.info('read config ' + CONFIG_PATH)

    global bot
    bot.setToken(config['telegram_token'])

    # print (bot.getMe().text)
    bot.startListen(tort, False)
    print ('основной поток дотопал до конца')

    bot.join_


if __name__ == '__main__':
    main()
