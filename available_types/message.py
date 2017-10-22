# -*- coding: utf-8 -*-
from chat import Chat
from user import User


class Message:
    def __init__(self,
                 message_id,
                 from_user,
                 date,
                 chat,
                 forward_from=None,
                 forward_from_chat=None,
                 forward_from_message_id=None,
                 forward_date=None,
                 reply_to_message=None,
                 edit_date=None,

                 author_signature=None,
                 text=None,
                 entities=None,
                 caption_entities=None,
                 audio=None,
                 document=None,
                 game=None,
                 photo=None,
                 sticker=None,
                 video=None,

                 video_note=None,
                 caption=None,
                 contact=None,
                 location=None,
                 venue=None,
                 new_chat_members=None,
                 left_chat_member=None,
                 new_chat_title=None,
                 new_chat_photo=None,
                 delete_chat_photo=False,

                 group_chat_created=False,
                 supergroup_chat_created=False,
                 channel_chat_created=False,
                 migrate_to_chat_id=None,
                 migrate_from_chat_id=None,
                 pinned_message=None,
                 invoice=None,
                 successful_payment=None,
                 bot=None,
                 **kwargs):

        # Required
        self.message_id = int(message_id)
        self.from_user = from_user
        self.date = date
        self.chat = chat
        # Optionals
        self.forward_from = forward_from
        self.forward_from_chat = forward_from_chat
        self.forward_from_message_id = forward_from_message_id
        self.forward_date = forward_date
        self.reply_to_message = reply_to_message
        self.edit_date = edit_date

        self.author_signature = author_signature
        self.text = text
        self.entities = entities or list()
        self.caption_entities = caption_entities or list()
        self.audio = audio
        self.document = document
        self.game = game
        self.photo = photo or list()
        self.sticker = sticker
        self.video = video

        self.video_note = video_note
        self.caption = caption
        self.contact = contact
        self.location = location
        self.venue = venue
        self.new_chat_members = new_chat_members or list()
        self.left_chat_member = left_chat_member
        self.new_chat_title = new_chat_title
        self.new_chat_photo = new_chat_photo or list()
        self.delete_chat_photo = bool(delete_chat_photo)

        self.group_chat_created = bool(group_chat_created)
        self.supergroup_chat_created = bool(supergroup_chat_created)
        self.channel_chat_created = bool(channel_chat_created)
        self.migrate_to_chat_id = migrate_to_chat_id
        self.migrate_from_chat_id = migrate_from_chat_id
        self.pinned_message = pinned_message
        self.invoice = invoice
        self.successful_payment = successful_payment

        self.bot = bot

    @staticmethod
    def jsonConstructor(data, bot):

        if (data is None) or (bot is None):  # we return None if can not create instance
            return None

        message = Message(message_id=data.get('message_id'),
                          from_user=User.jsonConstructor(data.get('from'), bot),
                          date=data.get('date'),
                          chat=Chat.jsonConstructor(data.get('chat'), bot),
                          forward_from=User.jsonConstructor(data.get('forward_from'), bot),
                          forward_from_chat=Chat.jsonConstructor(data.get('forward_from_chat'), bot),
                          forward_from_message_id=data.get('forward_from_message_id'),
                          forward_date=data.get('forward_date'),
                          reply_to_message=Message.jsonConstructor(data.get('reply_to_message'), bot),
                          edit_date=data.get('edit_date'),

                          author_signature=data.get('author_signature'),
                          text=data.get('text'),
                          entities=data.get('entities'),
                          caption_entities=data.get('caption_entities'),
                          audio=data.get('audio'),
                          document=data.get('document'),
                          game=data.get('game'),
                          photo=data.get('photo'),
                          sticker=data.get('sticker'),
                          video=data.get('video'),

                          video_note=data.get('video_note'),
                          caption=data.get('caption'),
                          contact=data.get('contact'),
                          location=data.get('location'),
                          venue=data.get('venue'),
                          new_chat_members=data.get('new_chat_members'),
                          left_chat_member=data.get('left_chat_member'),
                          new_chat_title=data.get('new_chat_title'),
                          new_chat_photo=data.get('new_chat_photo'),
                          delete_chat_photo=data.get('delete_chat_photo'),

                          group_chat_created=data.get('group_chat_created'),
                          supergroup_chat_created=data.get('supergroup_chat_created'),
                          channel_chat_created=data.get('channel_chat_created'),
                          migrate_to_chat_id=data.get('migrate_to_chat_id'),
                          migrate_from_chat_id=data.get('migrate_from_chat_id'),
                          pinned_message=data.get('pinned_message'),
                          invoice=data.get('invoice'),
                          successful_payment=data.get('successful_payment'),

                          bot=bot)
        print message

        return message

    def __str__(self):
        return ('message_id = { ' + str(self.message_id) + ' },\n' +
                'from_user = { ' + str(self.from_user) + ' },\n' +
                'date = { ' + str(self.date) + ' },\n' +
                'chat = { ' + str(self.chat) + ' },\n' +
                'forward_from = { ' + str(self.forward_from) + ' },\n' +
                'forward_from_chat = { ' + str(self.forward_from_chat) + ' },\n' +
                'forward_from_message_id = { ' + str(self.forward_from_message_id) + ' },\n' +
                'forward_date = { ' + str(self.forward_date) + ' },\n' +
                'reply_to_message = { ' + str(self.reply_to_message) + ' },\n' +
                'edit_date = { ' + str(self.edit_date) + ' },\n' +

                'author_signature = { ' + str(self.author_signature) + ',\n' +
                'text = { ' + str(self.text) + ' },\n' +
                'entities = { ' + str(self.entities) + ' },\n' +
                'caption_entities = { ' + str(self.caption_entities) + ' },\n' +
                'audio = { ' + str(self.audio) + ' },\n' +
                'document = { ' + str(self.document) + ' },\n' +
                'game = { ' + str(self.game) + ' },\n' +
                'photo = { ' + str(self.photo) + ' },\n' +
                'sticker = { ' + str(self.sticker) + ' },\n' +
                'video = { ' + str(self.video) + ' },\n' +

                'video_note = { ' + str(self.video_note) + ' },\n' +
                'caption = { ' + str(self.caption) + ' },\n' +
                'contact = { ' + str(self.contact) + ' },\n' +
                'location = { ' + str(self.location) + ' },\n' +
                'venue = { ' + str(self.venue) + ' },\n' +
                'new_chat_members = { ' + str(self.new_chat_members) + ' },\n' +
                'left_chat_member = { ' + str(self.left_chat_member) + ' },\n' +
                'new_chat_title = { ' + str(self.new_chat_title) + ' },\n' +
                'new_chat_photo = { ' + str(self.new_chat_photo) + ' },\n' +
                'delete_chat_photo = { ' + str(self.delete_chat_photo) + ' },\n' +

                'group_chat_created = { ' + str(self.group_chat_created) + ' },\n' +
                'supergroup_chat_created = { ' + str(self.supergroup_chat_created) + ' },\n' +
                'channel_chat_created = { ' + str(self.channel_chat_created) + ' },\n' +
                'migrate_to_chat_id = { ' + str(self.migrate_to_chat_id) + ' },\n' +
                'migrate_from_chat_id = { ' + str(self.migrate_from_chat_id) + ' },\n' +
                'pinned_message = { ' + str(self.pinned_message) + ' },\n' +
                'invoice = { ' + str(self.invoice) + ' },\n' +
                'successful_payment = { ' + str(self.successful_payment) + ' },\n' +
                'bot = { ' + str(self.bot) + ' }'
                )
