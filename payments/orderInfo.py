# -*- coding: utf-8 -*-


class OrderInfo:
    def __init__(self,
                 name,
                 phone_number,
                 email,
                 shipping_address,
                 bot=None,
                 **kwargs):

        # Required
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.shipping_address = shipping_address

        self.bot = bot

    @staticmethod
    def jsonConstructor(data, bot):

        if (data is None) or (bot is None):  # we return None if can not create instance
            return None

        orderInfo = OrderInfo(name=data.get('name'),
                              phone_number=data.get('phone_number'),
                              email=data.get('email'),
                              shipping_address=data.get('shipping_address'),
                              bot=bot)

        return orderInfo

    def __str__(self):
        return ('name = { ' + str(self.name) + ' },\n' +
                'phone_number = { ' + str(self.phone_number) + ' },\n' +
                'email = { ' + str(self.email) + ' },\n' +
                'shipping_address = { ' + str(self.shipping_address) + ' },\n' +
                'bot = { ' + str(self.bot) + ' }'
                )
