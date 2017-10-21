# -*- coding: utf-8 -*-


class User:
    def __init__(self,
                 user_id,
                 is_bot,
                 first_name,
                 last_name=None,
                 username=None,
                 language_code=None,
                 bot=None,
                 **kwargs):

        # Required
        self.user_id = user_id
        self.is_bot = is_bot
        self.first_name = first_name
        # Optionals
        self.last_name = last_name
        self.username = username
        self.language_code = language_code

        self.bot = bot

    @staticmethod
    def jsonConstructor(data, bot):

        if (data is None) or (bot is None):  # we return None if can not create instance
            return None

        user = User(user_id=data.get('user_id'),
                    is_bot=data.get('is_bot'),
                    first_name=data.get('first_name'),
                    last_name=data.get('last_name'),
                    username=data.get('username'),
                    language_code=data.get('language_code'),
                    bot=bot)

        return user

    def __str__(self):
        return ('user_id = ' + str(self.user_id) + ',\n' +
                'is_bot = ' + str(self.is_bot) + ',\n' +
                'first_name = ' + str(self.first_name) + ',\n' +
                'last_name = ' + str(self.last_name) + ',\n' +
                'username = ' + str(self.username) + ',\n' +
                'language_code = ' + str(self.language_code) + ',\n' +
                'bot = ' + str(self.bot)
                )
