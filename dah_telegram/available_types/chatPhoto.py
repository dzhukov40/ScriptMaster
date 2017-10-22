# -*- coding: utf-8 -*-


class ChartPhoto:
    def __init__(self,
                 small_file_id,
                 big_file_id,
                 bot=None,
                 **kwargs):

        # Required
        self.small_file_id = int(small_file_id)
        self.big_file_id = int(big_file_id)

        self.bot = bot

    @staticmethod
    def jsonConstructor(data, bot):

        if (data is None) or (bot is None):  # we return None if can not create instance
            return None

        chartPhoto = ChartPhoto(small_file_id=data.get('small_file_id'),
                                big_file_id=data.get('big_file_id'),
                                bot=bot)

        return chartPhoto

    def __str__(self):
        return ('small_file_id = { ' + str(self.small_file_id) + ' },\n' +
                'big_file_id = { ' + str(self.big_file_id) + ' },\n' +
                'bot = { ' + str(self.bot) + ' }'
                )
