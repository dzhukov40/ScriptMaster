# -*- coding: utf-8 -*-


class Sticker:
    def __init__(self,
                 file_id,
                 width,
                 height,
                 thumb=None,
                 emoji=None,
                 set_name=None,
                 mask_position=None,
                 file_size=None,
                 bot=None,
                 **kwargs):

        # Required
        self.file_id = file_id
        self.width = width
        self.height = height
        # Optionals
        self.thumb = thumb
        self.emoji = emoji
        self.set_name = set_name
        self.mask_position = mask_position
        self.file_size = file_size

        self.bot = bot

    @staticmethod
    def jsonConstructor(data, bot):

        if (data is None) or (bot is None):  # we return None if can not create instance
            return None

        sticker = Sticker(file_id=data.get('file_id'),
                          width=data.get('width'),
                          height=data.get('height'),
                          last_name=data.get('last_name'),
                          thumb=data.get('thumb'),
                          emoji=data.get('emoji'),
                          set_name=data.get('set_name'),
                          mask_position=data.get('mask_position'),
                          file_size=data.get('file_size'),
                          bot=bot)

        return sticker

    def __str__(self):
        return ('file_id = { ' + str(self.file_id) + ' },\n' +
                'width = { ' + str(self.width) + ' },\n' +
                'height = { ' + str(self.height) + ' },\n' +
                'thumb = { ' + str(self.thumb) + ' },\n' +
                'emoji = { ' + str(self.emoji) + ' },\n' +
                'set_name = { ' + str(self.set_name) + ' },\n' +
                'mask_position = { ' + str(self.mask_position) + ' },\n' +
                'file_size = { ' + str(self.file_size) + ' },\n' +
                'bot = { ' + str(self.bot) + ' }'
                )
