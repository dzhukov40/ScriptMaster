# -*- coding: utf-8 -*-


class ShippingQuery:
    def __init__(self,
                 shippingQuery_id,
                 shippingQuery_from,
                 invoice_payload,
                 shipping_address,
                 bot=None,
                 **kwargs):

        # Required
        self.shippingQuery_id = shippingQuery_id
        self.shippingQuery_from = shippingQuery_from
        self.invoice_payload = invoice_payload
        self.shipping_address = shipping_address

        self.bot = bot

    @staticmethod
    def jsonConstructor(data, bot):

        if (data is None) or (bot is None):  # we return None if can not create instance
            return None

        shippingQuery = ShippingQuery(shippingQuery_id=data.get('id'),
                                      shippingQuery_from=data.get('from'),
                                      invoice_payload=data.get('invoice_payload'),
                                      shipping_address=data.get('shipping_address'),
                                      bot=bot)

        return shippingQuery

    def __str__(self):
        return ('shippingQuery_id = { ' + str(self.shippingQuery_id) + ' },\n' +
                'shippingQuery_from = { ' + str(self.shippingQuery_from) + ' },\n' +
                'invoice_payload = { ' + str(self.invoice_payload) + ' },\n' +
                'shipping_address = { ' + str(self.shipping_address) + ' },\n' +
                'bot = { ' + str(self.bot) + ' }'
                )
