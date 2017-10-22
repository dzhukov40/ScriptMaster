# -*- coding: utf-8 -*-


class Game:
    def __init__(self,
                 title,
                 description=None,
                 photo=None,
                 text=None,
                 text_entities=None,
                 animation=None,
                 bot=None,
                 **kwargs):

        # Required
        self.title = title
        self.description = description
        self.photo = photo
        # Optionals
        self.text = text
        self.text_entities = text_entities
        self.animation = animation

        self.bot = bot

    @staticmethod
    def jsonConstructor(data, bot):

        if (data is None) or (bot is None):  # we return None if can not create instance
            return None

        game = Game(title=data.get('title'),
                    description=data.get('description'),
                    photo=data.get('photo'),
                    text=data.get('text'),
                    text_entities=data.get('text_entities'),
                    animation=data.get('animation'),
                    bot=bot)

        return game

    def __str__(self):
        return ('title = { ' + str(self.title) + ' },\n' +
                'description = { ' + str(self.description) + ' },\n' +
                'photo = { ' + str(self.photo) + ' },\n' +
                'text = { ' + str(self.text) + ' },\n' +
                'text_entities = { ' + str(self.text_entities) + ' },\n' +
                'animation = { ' + str(self.animation) + ' },\n' +
                'bot = { ' + str(self.bot) + ' }'
                )
