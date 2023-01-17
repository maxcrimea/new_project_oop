class Hero:

    def __init__(self, name, abyliti):
        self.name = name
        self.abyliti = abyliti


class Hero_Super(Hero):

    def __init__(self, name, abyliti):
        super().__init__(name, abyliti)

    def __str__(self):
        return f'{self.name}\n' \
               f'{self.abyliti}\n'

    def print_name(self):
        return print(f'{self.name} it is super_hero')
