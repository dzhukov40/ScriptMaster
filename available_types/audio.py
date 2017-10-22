# -*- coding: utf-8 -*-


class Audio:
    def __init__(self,
                 file_id,
                 duration,
                 performer=None,
                 title=None,
                 mime_type=None,
                 file_size=None,
                 bot=None,
                 **kwargs):

        # Required
        self.file_id = file_id
        self.duration = duration
        # Optionals
        self.performer = performer
        self.title = title
        self.mime_type = mime_type
        self.file_size = file_size

        self.bot = bot

    @staticmethod
    def jsonConstructor(data, bot):

        if (data is None) or (bot is None):  # we return None if can not create instance
            return None

        audio = Audio(file_id=data.get('file_id'),
                      duration=data.get('duration'),
                      performer=data.get('performer'),
                      title=data.get('title'),
                      mime_type=data.get('mime_type'),
                      file_size=data.get('file_size'),
                      bot=bot)

        return audio

    def __str__(self):
        return ('file_id = { ' + str(self.file_id) + ' },\n' +
                'duration = { ' + str(self.duration) + ' },\n' +
                'performer = { ' + str(self.performer) + ' },\n' +
                'title = { ' + str(self.title) + ' },\n' +
                'mime_type = { ' + str(self.mime_type) + ' },\n' +
                'file_size = { ' + str(self.file_size) + ' },\n' +
                'bot = { ' + str(self.bot) + ' }'
                )
