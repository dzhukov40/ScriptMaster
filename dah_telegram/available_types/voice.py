# -*- coding: utf-8 -*-


class Voice:
    def __init__(self,
                 file_id,
                 duration,
                 mime_type=None,
                 file_size=None,
                 bot=None,
                 **kwargs):

        # Required
        self.file_id = file_id
        self.duration = duration
        # Optionals
        self.mime_type = mime_type
        self.file_size = file_size

        self.bot = bot

    @staticmethod
    def jsonConstructor(data, bot):

        if (data is None) or (bot is None) or (data is []):  # we return None if can not create instance
            return None

        resultList = []

        for entity in data:
            resultList.append(Voice(file_id=entity.get('file_id'),
                                    duration=entity.get('duration'),
                                    mime_type=entity.get('mime_type'),
                                    file_size=entity.get('file_size'),
                                    bot=bot))

        if resultList.count == 1:
            return resultList.pop()
        else:
            return resultList

    def __str__(self):
        return ('file_id = { ' + str(self.file_id) + ' },\n' +
                'duration = { ' + str(self.duration) + ' },\n' +
                'mime_type = { ' + str(self.mime_type) + ' },\n' +
                'file_size = { ' + str(self.file_size) + ' },\n' +
                'bot = { ' + str(self.bot) + ' }'
                )
