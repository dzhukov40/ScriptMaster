# -*- coding: utf-8 -*-


class Location:
    def __init__(self,
                 longitude,
                 latitude,
                 bot=None,
                 **kwargs):

        # Required
        self.longitude = longitude
        self.latitude = latitude

        self.bot = bot

    @staticmethod
    def jsonConstructor(data, bot):

        if (data is None) or (bot is None):  # we return None if can not create instance
            return None

        location = Location(longitude=data.get('longitude'),
                            latitude=data.get('latitude'),
                            bot=bot)

        return location

    def __str__(self):
        return ('longitude = ' + str(self.longitude) + ',\n' +
                'latitude = ' + str(self.latitude) + ',\n' +
                'bot = ' + str(self.bot)
                )
