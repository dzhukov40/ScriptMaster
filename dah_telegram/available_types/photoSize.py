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

        if (data is None) or (bot is None):  # we return None if can not create instance
            return None

        photoSize = PhotoSize(file_id=data.get('file_id'),
                              width=data.get('width'),
                              height=data.get('height'),
                              file_size=data.get('file_size'),
                              bot=bot)

        return photoSize

    def __str__(self):
        return ('file_id = { ' + str(self.file_id) + ' },\n' +
                'width = { ' + str(self.width) + ' },\n' +
                'height = { ' + str(self.height) + ' },\n' +
                'file_size = { ' + str(self.file_size) + ' },\n' +
                'bot = { ' + str(self.bot) + ' }'
                )
