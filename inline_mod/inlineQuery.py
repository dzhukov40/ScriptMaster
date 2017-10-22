# -*- coding: utf-8 -*-


class InlineQuery:
    def __init__(self,
                 inlineQuery_id,
                 inlineQuery_from,
                 location,
                 query,
                 offset,
                 bot=None,
                 **kwargs):

        # Required
        self.inlineQuery_id = int(inlineQuery_id)
        self.inlineQuery_from = inlineQuery_from
        self.location = location
        self.query = query
        self.offset = offset

        self.bot = bot

    @staticmethod
    def jsonConstructor(data, bot):

        if (data is None) or (bot is None):  # we return None if can not create instance
            return None

        inlineQuery = InlineQuery(inlineQuery_id=data.get('id'),
                                  inlineQuery_from=data.get('from'),
                                  location=data.get('location'),
                                  query=data.get('query'),
                                  offset=data.get('offset'),
                                  bot=bot)

        return inlineQuery

    def __str__(self):
        return ('inlineQuery_id = { ' + str(self.inlineQuery_id) + ' },\n' +
                'inlineQuery_from = ' + str(self.inlineQuery_from) + ' },\n' +
                'location = ' + str(self.location) + ' },\n' +
                'query = ' + str(self.query) + ' },\n' +
                'offset = ' + str(self.offset) + ' },\n' +
                'bot = ' + str(self.bot) + ' }'
                )
