# -*- coding: utf-8 -*-
import ConfigParser
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


def main():
    readConfig(CONFIG_PATH)
    log.info('read config ' + CONFIG_PATH)

    bot = telegramBot.Bot(config['telegram_token'])

    # print (bot.getMe().text)
    print (bot.getUpdates().text)


if __name__ == '__main__':
    main()
