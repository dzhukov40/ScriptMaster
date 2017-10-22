# -*- coding: utf-8 -*-


class ChosenInlineResult:
    def __init__(self,
                 result_id,
                 result_from,
                 location,
                 inline_message_id,
                 query,
                 bot=None,
                 **kwargs):

        # Required
        self.result_id = int(result_id)
        self.result_from = result_from
        self.location = location
        self.inline_message_id = inline_message_id
        self.query = query

        self.bot = bot

    @staticmethod
    def jsonConstructor(data, bot):

        if (data is None) or (bot is None):  # we return None if can not create instance
            return None

        chosenInlineResult = ChosenInlineResult(result_id=data.get('result_id'),
                                                result_from=data.get('from'),
                                                location=data.get('location'),
                                                inline_message_id=data.get('inline_message_id'),
                                                query=data.get('query'),
                                                bot=bot)

        return chosenInlineResult

    def __str__(self):
        return ('result_id = { ' + str(self.result_id) + ' },\n' +
                'result_from = { ' + str(self.result_from) + ' },\n' +
                'location = { ' + str(self.location) + ' },\n' +
                'inline_message_id = { ' + str(self.inline_message_id) + ' },\n' +
                'query = { ' + str(self.query) + ' },\n' +
                'bot = { ' + str(self.bot) + ' }'
                )
