# -*- coding: utf-8 -*-


class Document:
    def __init__(self,
                 file_id,
                 thumb=None,
                 file_name=None,
                 mime_type=None,
                 file_size=None,
                 bot=None,
                 **kwargs):

        # Required
        self.file_id = file_id
        # Optionals
        self.thumb = thumb
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

        self.bot = bot

    @staticmethod
    def jsonConstructor(data, bot):

        if (data is None) or (bot is None):  # we return None if can not create instance
            return None

        document = Document(file_id=data.get('file_id'),
                            thumb=data.get('thumb'),
                            file_name=data.get('file_name'),
                            mime_type=data.get('mime_type'),
                            file_size=data.get('file_size'),
                            bot=bot)

        return document

    def __str__(self):
        return ('file_id = { ' + str(self.file_id) + ' },\n' +
                'thumb = { ' + str(self.thumb) + ' },\n' +
                'file_name = { ' + str(self.file_name) + ' },\n' +
                'mime_type = { ' + str(self.mime_type) + ' },\n' +
                'mime_type = { ' + str(self.mime_type) + ' },\n' +
                'file_size = { ' + str(self.file_size) + ' },\n' +
                'bot = { ' + str(self.bot) + ' }'
                )
