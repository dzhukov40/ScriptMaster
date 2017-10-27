# -*- coding: utf-8 -*-


class InlineKeyboardButton:
    def __init__(self,
                 text,
                 url=None,
                 callback_data=None,
                 switch_inline_query=None,
                 switch_inline_query_current_chat=None,
                 callback_game=None,
                 pay=None,
                 bot=None,
                 **kwargs):

        # Required
        self.text = text
        # Optionals
        self.url = url
        self.callback_data = callback_data
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        self.callback_game = callback_game
        self.pay = pay

        self.bot = bot

    @staticmethod
    def jsonConstructor(data, bot):

        if (data is None) or (bot is None) or (data is []):  # we return None if can not create instance
            return None

        resultList = []

        for entity in data:
            resultList.append(InlineKeyboardButton(text=entity.get('text'),
                                                   url=entity.get('url'),
                                                   callback_data=entity.get('callback_data'),
                                                   switch_inline_query=entity.get('switch_inline_query'),
                                                   switch_inline_query_current_chat=entity.get('switch_inline_query_current_chat'),
                                                   callback_game=entity.get('callback_game'),
                                                   pay=entity.get('pay'),
                                                   bot=bot))

        if resultList.count == 1:
            return resultList.pop()
        else:
            return resultList

    def dictConvert(self):

        result = {'text': self.text}

        if self.url is not None:
            result['url'] = self.url

        if self.callback_data is not None:
            result['callback_data'] = self.callback_data

        if self.switch_inline_query_current_chat is not None:
            result['switch_inline_query'] = self.switch_inline_query

        if self.switch_inline_query_current_chat is not None:
            result['switch_inline_query_current_chat'] = self.switch_inline_query_current_chat

        if self.callback_game is not None:
            result['callback_game'] = self.callback_game

        return result

    def __str__(self):
        return ('text = { ' + str(self.text) + ' },\n' +
                'url = { ' + str(self.url) + ' },\n' +
                'callback_data = { ' + str(self.callback_data) + ' },\n' +
                'switch_inline_query = { ' + str(self.switch_inline_query) + ' },\n' +
                'switch_inline_query_current_chat = { ' + str(self.switch_inline_query_current_chat) + ' },\n' +
                'callback_game = { ' + str(self.callback_game) + ' },\n' +
                'pay = { ' + str(self.pay) + ' },\n' +
                'bot = { ' + str(self.bot) + ' }'
                )
