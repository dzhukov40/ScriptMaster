# -*- coding: utf-8 -*-
import json

from dah_telegram.available_types.inlineKeyboardButton import InlineKeyboardButton


class InlineKeyboardMarkup:
    def __init__(self,
                 inline_keyboard,
                 bot=None,
                 **kwargs):

        # Required
        self.inline_keyboard = inline_keyboard

        self.bot = bot

    @staticmethod
    def jsonConstructor(data, bot):

        if (data is None) or (bot is None) or (data is []):  # we return None if can not create instance
            return None

        resultList = []

        for entity in data:
            resultList.append(InlineKeyboardMarkup(inline_keyboard=entity.get('inline_keyboard'),
                                                   bot=bot))

        if resultList.count == 1:
            return resultList.pop()
        else:
            return resultList

    def arrayConvert(self):

        # inline_keyboard
        # json.dumps({'inline_keyboard': [[{'text': 'текст1', 'url': 'http://ya.ru'}]]})

        buttonArray = []
        keyboardArray = []

        for keyboard in self.inline_keyboard:
            for button in keyboard:
                if isinstance(button, InlineKeyboardButton):
                    buttonArray.append(button.dictConvert())
            keyboardArray.append(buttonArray)

        result = {'inline_keyboard': keyboardArray}

        return result

    def jsonConvert(self):
        print self.arrayConvert()
        return json.dumps(self.arrayConvert())

    def __str__(self):
        return ('inline_keyboard = { ' + str(self.inline_keyboard) + ' },\n' +
                'bot = { ' + str(self.bot) + ' }'
                )
