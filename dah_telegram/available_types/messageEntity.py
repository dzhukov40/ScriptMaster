# -*- coding: utf-8 -*-


class MessageEntity:
    def __init__(self,
                 messageEntity_type,
                 offset,
                 length,
                 url=None,
                 user=None,
                 bot=None,
                 **kwargs):

        # Required
        self.messageEntity_type = messageEntity_type
        self.offset = offset
        self.length = length
        # Optionals
        self.url = url
        self.user = user

        self.bot = bot

    @staticmethod
    def jsonConstructor(data, bot):
        
        if (data is None) or (bot is None):  # we return None if can not create instance
            return None

        messageEntity = MessageEntity(messageEntity_type=data.get('type'),
                                      offset=data.get('offset'),
                                      length=data.get('length'),
                                      url=data.get('url'),
                                      user=data.get('user'),
                                      bot=bot)

        return messageEntity

    def __str__(self):
        return ('messageEntity_type = { ' + str(self.messageEntity_type) + ' },\n' +
                'offset = { ' + str(self.offset) + ' },\n' +
                'length = { ' + str(self.length) + ' },\n' +
                'url = { ' + str(self.url) + ' },\n' +
                'user = { ' + str(self.user) + ' },\n' +
                'bot = { ' + str(self.bot) + ' }'
                )
