# -*- coding: utf-8 -*-


class CallbackQuery:
    def __init__(self,
                 callbackQuery_id,
                 callbackQuery_from,
                 message=None,
                 inline_message_id=None,
                 chat_instance=None,
                 data=None,
                 game_short_name=None,
                 bot=None,
                 **kwargs):

        # Required
        self.callbackQuery_id = callbackQuery_id
        self.callbackQuery_from = callbackQuery_from
        # Optionals
        self.message = message
        self.inline_message_id = inline_message_id
        self.chat_instance = chat_instance
        self.data = data
        self.game_short_name = game_short_name

        self.bot = bot

    @staticmethod
    def jsonConstructor(data, bot):

        if (data is None) or (bot is None):  # we return None if can not create instance
            return None

        callbackQuery = CallbackQuery(callbackQuery_id=data.get('id'),
                                      callbackQuery_from=data.get('from'),
                                      message=data.get('message'),
                                      inline_message_id=data.get('inline_message_id'),
                                      chat_instance=data.get('chat_instance'),
                                      data=data.get('data'),
                                      game_short_name=data.get('game_short_name'),
                                      bot=bot)

        return callbackQuery

    def __str__(self):
        return ('callbackQuery_id = { ' + str(self.callbackQuery_id) + ' },\n' +
                'callbackQuery_from = { ' + str(self.callbackQuery_from) + ' },\n' +
                'message = { ' + str(self.message) + ' },\n' +
                'inline_message_id = { ' + str(self.inline_message_id) + ' },\n' +
                'chat_instance = { ' + str(self.chat_instance) + ' },\n' +
                'data = { ' + str(self.data) + ' },\n' +
                'game_short_name = { ' + str(self.game_short_name) + ' },\n' +
                'bot = { ' + str(self.bot) + ' }'
                )
