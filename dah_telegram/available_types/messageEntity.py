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

        if (data is None) or (bot is None) or (data is []):  # we return None if can not create instance
            return None

        resultList = []

        for entity in data:
            resultList.append(MessageEntity(messageEntity_type=entity.get('type'),
                                            offset=entity.get('offset'),
                                            length=entity.get('length'),
                                            url=entity.get('url'),
                                            user=entity.get('user'),
                                            bot=bot))

        if resultList.count == 1:
            return resultList.pop()
        else:
            return resultList

    def __str__(self):
        return ('messageEntity_type = { ' + str(self.messageEntity_type) + ' },\n' +
                'offset = { ' + str(self.offset) + ' },\n' +
                'length = { ' + str(self.length) + ' },\n' +
                'url = { ' + str(self.url) + ' },\n' +
                'user = { ' + str(self.user) + ' },\n' +
                'bot = { ' + str(self.bot) + ' }'
                )
