# -*- coding: utf-8 -*-


class PhotoSize:
    def __init__(self,
                 file_id,
                 width,
                 height,
                 file_size=None,
                 bot=None,
                 **kwargs):

        # Required
        self.file_id = file_id
        self.width = width
        self.height = height
        self.file_size = file_size

        self.bot = bot

    @staticmethod
    def jsonConstructor(data, bot):

        if (data is None) or (bot is None) or (data is []):  # we return None if can not create instance
            return None

        resultList = []

        for entity in data:
            resultList.append(PhotoSize(file_id=entity.get('file_id'),
                                        width=entity.get('width'),
                                        height=entity.get('height'),
                                        file_size=entity.get('file_size'),
                                        bot=bot))

        if resultList.count == 1:
            return resultList.pop()
        else:
            return resultList

    def __str__(self):
        return ('file_id = { ' + str(self.file_id) + ' },\n' +
                'width = { ' + str(self.width) + ' },\n' +
                'height = { ' + str(self.height) + ' },\n' +
                'file_size = { ' + str(self.file_size) + ' },\n' +
                'bot = { ' + str(self.bot) + ' }'
                )
