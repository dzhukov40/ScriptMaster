# -*- coding: utf-8 -*-


class Video:
    def __init__(self,
                 file_id,
                 width,
                 height,
                 duration,
                 thumb,
                 mime_type,
                 file_size,
                 bot=None,
                 **kwargs):

        # Required
        self.file_id = file_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumb = thumb
        self.mime_type = mime_type
        self.file_size = file_size

        self.bot = bot

    @staticmethod
    def jsonConstructor(data, bot):

        if (data is None) or (bot is None):  # we return None if can not create instance
            return None

        video = Video(file_id=data.get('file_id'),
                      width=data.get('width'),
                      height=data.get('height'),
                      duration=data.get('duration'),
                      thumb=data.get('thumb'),
                      mime_type=data.get('mime_type'),
                      file_size=data.get('file_size'),
                      bot=bot)

        return video

    def __str__(self):
        return ('file_id = { ' + str(self.file_id) + ' },\n' +
                'width = { ' + str(self.width) + ' },\n' +
                'height = { ' + str(self.height) + ' },\n' +
                'duration = { ' + str(self.duration) + ' },\n' +
                'thumb = { ' + str(self.thumb) + ' },\n' +
                'mime_type = { ' + str(self.mime_type) + ' },\n' +
                'file_size = { ' + str(self.file_size) + ' },\n' +
                'bot = { ' + str(self.bot) + ' }'
                )
