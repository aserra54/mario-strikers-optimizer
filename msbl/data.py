from collections import namedtuple
from dataclasses import dataclass


Player = namedtuple('Player', 'name strength speed shooting passing technique')
Equipment = namedtuple('Equipment', 'name cost strength speed shooting passing technique')


@dataclass
class EquipmentSet:
    head: Equipment
    arms: Equipment
    body: Equipment
    legs: Equipment

    @property
    def strength(self):
        return self.head.strength + self.arms.strength + self.body.strength + self.legs.strength

    @property
    def speed(self):
        return self.head.speed + self.arms.speed + self.body.speed + self.legs.speed

    @property
    def shooting(self):
        return self.head.shooting + self.arms.shooting + self.body.shooting + self.legs.shooting

    @property
    def passing(self):
        return self.head.passing + self.arms.passing + self.body.passing + self.legs.passing

    @property
    def technique(self):
        return self.head.technique + self.arms.technique + self.body.technique + self.legs.technique

    @property
    def cost(self):
        return self.head.cost + self.arms.cost + self.body.cost + self.legs.cost


__raw_players = [
    ('Mario', 11, 12, 14, 10, 16),
    ('Luigi', 11, 11, 10, 14, 17),
    ('Bowser', 17, 9, 17, 11, 9),
    ('Peach', 9, 17, 9, 13, 15),
    ('Rosalina', 14, 9, 17, 10, 13),
    ('Toad', 9, 17, 11, 15, 11),
    ('Yoshi', 10, 10, 17, 17, 9),
    ('Donkey Kong', 16, 9, 13, 16, 9),
    ('Wario', 17, 9, 15, 13, 9),
    ('Waluigi', 15, 16, 9, 9, 14),
    ('Daisy', 13, 9, 10, 13, 18),
    ('Shy Guy', 13, 12, 13, 13, 12),
    ('Pauline', 20, 16, 9, 9, 9),
    ('Diddy Kong', 9, 16, 9, 16, 13),
    ('Bowser Jr', 13, 13, 11, 17, 9),
    ('Birdo', 9, 10, 18, 9, 17),
]

__raw_equipment = {
    'head': [
        ('Nothing', 0, 0, 0, 0, 0, 0),
        ('Muscle', 100, 2, 0, 0, 0, -2),
        ('Turbo', 100, 0, 2, 0, 0, -2),
        ('Cannon', 100, 0, 0, 2, 0, -2),
        ('Chain', 100, 0, -2, 0, 2, 0),
        ('Trick', 100, 0, 0, 0, -2, 2),
        ('Bushido', 300, -1, -1, -1, 4, -1),
        ('Knight', 300, 2, -2, 1, 1, -2),
        ('Barrel', 300, -2, 1, 2, 1, -2),
    ],
    'arms': [
        ('Nothing', 0, 0, 0, 0, 0, 0),
        ('Muscle', 100, 2, 0, 0, -2, 0),
        ('Turbo', 100, -2, 2, 0, 0, 0),
        ('Cannon', 100, 0, -2, 2, 0, 0),
        ('Chain', 100, 0, 0, -2, 2, 0),
        ('Trick', 100, 0, -2, 0, 0, 2),
        ('Bushido', 300, -1, -1, -1, -1, 4),
        ('Knight', 300, 2, 1, 1, -2, -2),
        ('Barrel', 300, -2, 1, 2, 1, -2),
    ],
    'body': [
        ('Nothing', 0, 0, 0, 0, 0, 0),
        ('Muscle', 100, 2, 0, -2, 0, 0),
        ('Turbo', 100, 0, 2, 0, -2, 0),
        ('Cannon', 100, -2, 0, 2, 0, 0),
        ('Chain', 100, 0, 0, 0, 2, -2),
        ('Trick', 100, -2, 0, 0, 0, 2),
        ('Bushido', 300, 4, -1, -1, -1, -1),
        ('Knight', 300, 2, -2, 1, -2, 1),
        ('Barrel', 300, -1, -1, 2, 2, -2),
    ],
    'legs': [
        ('Nothing', 0, 0, 0, 0, 0, 0),
        ('Muscle', 100, 2, -2, 0, 0, 0),
        ('Turbo', 100, 0, 2, -2, 0, 0),
        ('Cannon', 100, 0, 0, 2, -2, 0),
        ('Chain', 100, -2, 0, 0, 2, 0),
        ('Trick', 100, 0, 0, -2, 0, 2),
        ('Bushido', 300, -1, 4, -1, -1, -1),
        ('Knight', 300, 2, -2, 2, -1, -1),
        ('Barrel', 300, 1, -2, 2, 1, -2),
    ]
}


def __to_player(player):
    return Player(name=player[0], strength=player[1], speed=player[2], shooting=player[3], passing=player[4],
        technique=player[5])


def __to_equipment(item):
    return Equipment(name=item[0], cost=item[1], strength=item[2], speed=item[3], shooting=item[4], passing=item[5],
        technique=item[6])


players = [__to_player(player) for player in __raw_players]
head_pieces = [__to_equipment(piece) for piece in __raw_equipment['head']]
arm_pieces = [__to_equipment(piece) for piece in __raw_equipment['arms']]
body_pieces = [__to_equipment(piece) for piece in __raw_equipment['body']]
leg_pieces = [__to_equipment(piece) for piece in __raw_equipment['legs']]
