
import random


class Product:
    '''
    - `name` (string with no default)
    - `price` (integer with default value 10)
    - `weight` (integer with default value 20)
    - `flammability` (float with default value 0.5)
    - `identifier` (integer, automatically genererated as a random (uniform)number
       anywhere from 1000000 to 9999999, includisve)(inclusive).
    '''

    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):

        self.identifier = identifier
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability

    def stealability(self):
        '''
        stealability(self) - calculates the price divided by the weight, and then
        returns a message: if the ratio is less than 0.5 return "Not so stealable...",
        if it is greater or equal to 0.5 but less than 1.0 return "Kinda stealable.",
        and otherwise return "Very stealable!"
        '''
        ratio = self.price/self.weight

        if ratio < 0.5:
            return 'Not so stealable...'
        elif ratio >= 0.5 and ratio < 1.0:
            return 'Kinda Stealable'
        else:
            return 'Very stealable'

    def explode(self):
        '''`explode(self)` - calculates the flammability times the weight,
         and then returns a message
        '''

        explosion = self.flammability * self.weight

        if explosion < 10:
            return '...fizzle.'
        elif explosion >= 10 and explosion < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 identifier=random.randint(1000000, 10000000)):
        super().__init__(name, price, weight, flammability, identifier)

    def explode(self):
        return "..it's a glove."

    def punch(self):
        if self.weight < 5:
            return 'That tickles.'
        elif self.weight >= 5 & self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
