# -*- coding: utf-8 -*-


class MaskPosition:
    def __init__(self,
                 point,
                 x_shift,
                 y_shift,
                 scale=None,
                 bot=None,
                 **kwargs):

        # Required
        self.point = point
        self.x_shift = x_shift
        self.y_shift = y_shift
        self.scale = scale

        self.bot = bot

    @staticmethod
    def jsonConstructor(data, bot):

        if (data is None) or (bot is None):  # we return None if can not create instance
            return None

        maskPosition = MaskPosition(point=data.get('point'),
                                    x_shift=data.get('x_shift'),
                                    y_shift=data.get('y_shift'),
                                    scale=data.get('scale'),
                                    bot=bot)

        return maskPosition

    def __str__(self):
        return ('point = { ' + str(self.point) + ' },\n' +
                'x_shift = { ' + str(self.x_shift) + ' },\n' +
                'y_shift = { ' + str(self.y_shift) + ' },\n' +
                'scale = { ' + str(self.scale) + ' },\n' +
                'bot = { ' + str(self.bot) + ' }'
                )
