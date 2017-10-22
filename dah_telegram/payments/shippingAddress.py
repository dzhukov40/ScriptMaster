# -*- coding: utf-8 -*-


class ShippingAddress:
    def __init__(self,
                 country_code,
                 state,
                 city,
                 street_line1,
                 street_line2,
                 post_code,
                 bot=None,
                 **kwargs):

        # Required
        self.country_code = country_code
        self.state = state
        self.city = city
        self.street_line1 = street_line1
        self.street_line2 = street_line2
        self.post_code = post_code

        self.bot = bot

    @staticmethod
    def jsonConstructor(data, bot):

        if (data is None) or (bot is None):  # we return None if can not create instance
            return None

        shippingAddress = ShippingAddress(country_code=data.get('country_code'),
                                          state=data.get('state'),
                                          city=data.get('city'),
                                          street_line1=data.get('street_line1'),
                                          street_line2=data.get('street_line2'),
                                          post_code=data.get('post_code'),
                                          bot=bot)

        return shippingAddress

    def __str__(self):
        return ('country_code = { ' + str(self.country_code) + ' },\n' +
                'state = { ' + str(self.state) + ' },\n' +
                'city = { ' + str(self.city) + ' },\n' +
                'street_line1 = { ' + str(self.street_line1) + ' },\n' +
                'street_line2 = { ' + str(self.street_line2) + ' },\n' +
                'post_code = { ' + str(self.post_code) + ' },\n' +
                'bot = { ' + str(self.bot) + ' }'
                )
