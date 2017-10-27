# -*- coding: utf-8 -*-
import unittest
from time import sleep

from dah_telegram import Bot, Update
from dah_telegram.available_types.inlineKeyboardButton import InlineKeyboardButton
from dah_telegram.available_types.inlineKeyboardMarkup import InlineKeyboardMarkup

"""
Тестовый случай создаётся путём наследования от unittest.TestCase. 
3 отдельных теста определяются с помощью методов, имя которых начинается на test. 
Это соглашение говорит исполнителю тестов о том, какие методы являются тестами.
"""

TELEGRAM_TOKEN = "416385445:AAEZI0_oRTg7FC5d4M0fWQqdYBEBvs6UBoI"
CHAT_ID = "12"
RETRY_COUNT = 100
RETRY_PAUSE = 1

bot = Bot()
chat_id = 0


def updates(msg):

    global chat_id
    # check type. Must be to indicate type!
    if isinstance(msg, Update):
        chat_id = msg.message.chat.chat_id


class TestTelegramBot(unittest.TestCase):

    # wait coming message for callback
    @classmethod
    def setUpClass(cls):
        global bot
        bot.setToken(TELEGRAM_TOKEN)
        bot.startListen(updates, True)

        if chat_id == 0:
            print "-----------------------------------------------------"
            print "ВАМ НУЖНО ОТПРАВИТЬ СООБЩЕНИЕ БОТУ ДЛЯ ЗАПУСКА ТЕСТОВ"
            print "p.s буду ждать " + str(RETRY_COUNT * RETRY_PAUSE) + " секунд"
            print "-----------------------------------------------------"

        while [RETRY_COUNT]:
            sleep(RETRY_PAUSE)
            if chat_id != 0:
                print "МЫ ПОЛУЧИЛИ [ chat_id = " + str(chat_id) + " ]"
                break

    def test_sendMessage(self):

        if chat_id == 0:
            self.assertTrue(False)
            return
        bot.sendMessage(chat_id, "Привети, это Тесты Детка!")

        inlineKeyboardButton1 = InlineKeyboardButton(text='1', url='http://ya.ru')
        inlineKeyboardButton2 = InlineKeyboardButton(text='2', url='http://ya.ru')
        inlineKeyboardButton3 = InlineKeyboardButton(text='3', url='http://ya.ru')
        inlineKeyboardButton4 = InlineKeyboardButton(text='4', url='http://ya.ru')
        arrayButtons1 = [inlineKeyboardButton1, inlineKeyboardButton2]
        arrayButtons2 = [inlineKeyboardButton3, inlineKeyboardButton4]
        inlineKeyboardMarkup1 = InlineKeyboardMarkup(inline_keyboard=[arrayButtons1, arrayButtons2])
        inlineKeyboardMarkup2 = InlineKeyboardMarkup(inline_keyboard=[arrayButtons1, arrayButtons2])

        bot.sendMessage(chat_id, "проверочка кнопок1", reply_markup=inlineKeyboardMarkup1.jsonConvert())
        bot.sendMessage(chat_id, "проверочка кнопок2", reply_markup=inlineKeyboardMarkup2.jsonConvert())
        self.assertTrue(True)

    def test_sendPhoto(self):

        bot.sendPhoto(chat_id, open('test_data/Photo_1.jpg', 'rb'), caption='тетя')
        bot.sendPhoto(chat_id, 'http://dummyimage.com/600x400/000/fff.png&text=telegram')
        self.assertTrue(True)

    def test_sendAudio(self):

        bot.sendAudio(chat_id, open('test_data/Song_1.mp3', 'rb'))
        bot.sendAudio(chat_id, 'https://python-telegram-bot.org/static/testfiles/telegram.mp3')
        self.assertTrue(True)

    def test_sendDocument(self):

        bot.sendDocument(chat_id, open('test_data/File_1.txt', 'rb'))
        bot.sendDocument(chat_id, 'http://lelang.ru/wp-content/pdf_noindex_medium/Eveline.pdf')
        self.assertTrue(True)

    def test_sendVideo(self):

        bot.sendVideo(chat_id, open('test_data/Video_1.mp4', 'rb'))
        bot.sendVideo(chat_id, 'https://python-telegram-bot.org/static/testfiles/telegram.mp4')
        self.assertTrue(True)

    def test_sendVoice(self):

        bot.sendVoice(chat_id, open('test_data/Voice_1.ogg', 'rb'))
        bot.sendVoice(chat_id, 'https://python-telegram-bot.org/static/testfiles/telegram.ogg')
        self.assertTrue(True)

    def test_sendVideoNote(self):

        bot.sendVideoNote(chat_id, open('test_data/Video_1.mp4', 'rb'))
        bot.sendVideoNote(chat_id, 'https://python-telegram-bot.org/static/testfiles/telegram.mp4')
        self.assertTrue(True)

    def test_sendLocation(self):

        bot.sendLocation(chat_id, 55.807255, 37.621902)
        self.assertTrue(True)

    @classmethod
    def tearDownClass(cls):
        global chat_id
        bot.stopListen()
        chat_id = 0

if __name__ == '__main__':
    unittest.main()
