# -*- coding: utf-8 -*-


class Chat:
    def __init__(self,
                 chat_id,
                 chat_type,
                 title=None,
                 username=None,
                 first_name=None,
                 last_name=None,
                 group_chat_created=False,
                 photo=None,
                 description=None,
                 invite_link=None,
                 pinned_message=None,
                 sticker_set_name=None,
                 can_set_sticker_set=None,
                 bot=None,
                 **kwargs):

        # Required
        self.chat_id = int(chat_id)
        self.chat_type = chat_type
        # Optionals
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.group_chat_created = group_chat_created
        self.photo = photo
        self.description = description
        self.invite_link = invite_link
        self.pinned_message = pinned_message
        self.sticker_set_name = sticker_set_name
        self.can_set_sticker_set = can_set_sticker_set

        self.bot = bot

    @staticmethod
    def jsonConstructor(data, bot):

        if (data is None) or (bot is None):  # we return None if can not create instance
            return None

        chat = Chat(chat_id=data.get('id'),
                    chat_type=data.get('type'),
                    title=data.get('title'),
                    username=data.get('username'),
                    first_name=data.get('first_name'),
                    last_name=data.get('last_name'),
                    group_chat_created=data.get('group_chat_created'),
                    photo=data.get('photo'),
                    description=data.get('description'),
                    invite_link=data.get('invite_link'),
                    pinned_message=data.get('pinned_message'),
                    sticker_set_name=data.get('sticker_set_name'),
                    can_set_sticker_set=data.get('can_set_sticker_set'),
                    bot=bot)

        return chat

    def __str__(self):
        return ('chat_id = { ' + str(self.chat_id) + ' },\n' +
                'chat_type = { ' + str(self.chat_type) + ' },\n' +
                'title = { ' + str(self.title) + ' },\n' +
                'username = { ' + str(self.username) + ' },\n' +
                'first_name = { ' + str(self.first_name) + ' },\n' +
                'last_name = { ' + str(self.last_name) + ' },\n' +
                'group_chat_created = { ' + str(self.group_chat_created) + ' },\n' +
                'photo = { ' + str(self.photo) + ' },\n' +
                'description = { ' + str(self.description) + ' },\n' +
                'invite_link = { ' + str(self.invite_link) + ' },\n' +
                'pinned_message = { ' + str(self.pinned_message) + ' },\n' +
                'sticker_set_name = { ' + str(self.sticker_set_name) + ' },\n' +
                'can_set_sticker_set = { ' + str(self.can_set_sticker_set) + ' },\n' +
                'bot = { ' + str(self.bot) + ' }'
                )
