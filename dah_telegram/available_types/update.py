# -*- coding: utf-8 -*-

from dah_telegram.available_types import CallbackQuery
from dah_telegram.inline_mod import InlineQuery, ChosenInlineResult
from dah_telegram.payments import ShippingQuery
from dah_telegram.payments.preCheckoutQuery import PreCheckoutQuery
from message import Message


class Update:
    def __init__(self,
                 update_id,
                 message=None,
                 edited_message=None,
                 channel_post=None,
                 edited_channel_post=None,
                 inline_query=None,
                 chosen_inline_result=None,
                 callback_query=None,
                 shipping_query=None,
                 pre_checkout_query=None,
                 bot=None,
                 **kwargs):

        # Required
        self.update_id = int(update_id)
        # Optionals
        self.message = message
        self.edited_message = edited_message
        self.channel_post = channel_post
        self.edited_channel_post = edited_channel_post
        self.inline_query = inline_query
        self.chosen_inline_result = chosen_inline_result
        self.callback_query = callback_query
        self.shipping_query = shipping_query
        self.pre_checkout_query = pre_checkout_query

        self.bot = bot

    @staticmethod
    def jsonConstructor(data, bot):

        if (data is None) or (bot is None):  # we return None if can not create instance
            return None

        update = Update(update_id=data.get('update_id'),
                        message=Message.jsonConstructor(data.get('message'), bot),
                        edited_message=Message.jsonConstructor(data.get('edited_message'), bot),
                        channel_post=Message.jsonConstructor(data.get('channel_post'), bot),
                        edited_channel_post=Message.jsonConstructor(data.get('edited_channel_post'), bot),
                        inline_query=InlineQuery.jsonConstructor(data.get('inline_query'), bot),
                        chosen_inline_result=ChosenInlineResult.jsonConstructor(data.get('chosen_inline_result'), bot),
                        callback_query=CallbackQuery.jsonConstructor(data.get('callback_query'), bot),
                        shipping_query=ShippingQuery.jsonConstructor(data.get('shipping_query'), bot),
                        pre_checkout_query=PreCheckoutQuery.jsonConstructor(data.get('pre_checkout_query'), bot),
                        bot=bot)

        return update

    def __str__(self):
        return ('update_id = { ' + str(self.update_id) + ' },\n' +
                'message = { ' + str(self.message) + ' },\n' +
                'edited_message = { ' + str(self.edited_message) + ' },\n' +
                'channel_post = { ' + str(self.channel_post) + ' },\n' +
                'edited_channel_post = { ' + str(self.edited_channel_post) + ' },\n' +
                'inline_query = { ' + str(self.inline_query) + ' },\n' +
                'chosen_inline_result = { ' + str(self.chosen_inline_result) + ' },\n' +
                'callback_query = { ' + str(self.callback_query) + ' },\n' +
                'shipping_query = { ' + str(self.shipping_query) + ' },\n' +
                'pre_checkout_query = { ' + str(self.pre_checkout_query) + ' },\n' +
                'bot = { ' + str(self.bot) + ' }'
                )
