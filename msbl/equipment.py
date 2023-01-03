from collections import namedtuple
from dataclasses import dataclass


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


def __to_equipment(item):
    return Equipment(name=item[0], cost=item[1], strength=item[2], speed=item[3], shooting=item[4], passing=item[5],
        technique=item[6])


head_pieces = [__to_equipment(piece) for piece in __raw_equipment['head']]
arm_pieces = [__to_equipment(piece) for piece in __raw_equipment['arms']]
body_pieces = [__to_equipment(piece) for piece in __raw_equipment['body']]
leg_pieces = [__to_equipment(piece) for piece in __raw_equipment['legs']]
