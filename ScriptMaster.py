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
    pass
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
    log.info('read config ' + CONFIG_PATH)

    global bot
    bot.setToken(config['telegram_token'])

    # print (bot.getMe().text)
    bot.startListen(tort, False)
    print ('основной поток дотопал до конца')

    bot.join_


if __name__ == '__main__':
    main()
