# -*- coding: utf-8 -*-


class PreCheckoutQuery:
    def __init__(self,
                 preCheckoutQuery_id,
                 preCheckoutQuery_from,
                 currency,
                 total_amount,
                 invoice_payload,
                 shipping_option_id=None,
                 order_info=None,
                 bot=None,
                 **kwargs):

        # Required
        self.preCheckoutQuery_id = preCheckoutQuery_id
        self.preCheckoutQuery_from = preCheckoutQuery_from
        self.currency = currency
        # Optionals
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.shipping_option_id = shipping_option_id
        self.order_info = order_info

        self.bot = bot

    @staticmethod
    def jsonConstructor(data, bot):

        if (data is None) or (bot is None):  # we return None if can not create instance
            return None

        preCheckoutQuery = PreCheckoutQuery(preCheckoutQuery_id=data.get('id'),
                                            preCheckoutQuery_from=data.get('from'),
                                            currency=data.get('currency'),
                                            total_amount=data.get('total_amount'),
                                            invoice_payload=data.get('invoice_payload'),
                                            shipping_option_id=data.get('shipping_option_id'),
                                            order_info=data.get('order_info'),
                                            bot=bot)

        return preCheckoutQuery

    def __str__(self):
        return ('preCheckoutQuery_id = { ' + str(self.preCheckoutQuery_id) + ' },\n' +
                'preCheckoutQuery_from = { ' + str(self.preCheckoutQuery_from) + ' },\n' +
                'currency = { ' + str(self.currency) + ' },\n' +
                'total_amount = { ' + str(self.total_amount) + ' },\n' +
                'invoice_payload = { ' + str(self.invoice_payload) + ' },\n' +
                'shipping_option_id = { ' + str(self.shipping_option_id) + ' },\n' +
                'order_info = { ' + str(self.order_info) + ' },\n' +
                'bot = { ' + str(self.bot) + ' }'
                )
