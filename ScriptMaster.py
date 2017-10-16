# -*- coding: utf-8 -*-
import ConfigParser
import json
from time import sleep

import log
import telegramBot

CONFIG_PATH = "config.ini"

config = {}


def readConfig(path):
    global config

    parseConfig = ConfigParser.ConfigParser()
    parseConfig.read(path)
    config['telegram_token'] = parseConfig.get("telegram", "telegram_token")
    log.info('readConfig ' + str(config))


def tort(msg):
    print ('hi msg = ' + str(msg))


def main():
    readConfig(CONFIG_PATH)
    log.info('read config ' + CONFIG_PATH)

    bot = telegramBot.Bot(config['telegram_token'])

    # print (bot.getMe().text)
    bot.startListen(tort)


if __name__ == '__main__':
    main()
