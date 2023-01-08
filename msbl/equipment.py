from dataclasses import dataclass
from msbl.stat import Stat, StatBased


class Equipment(StatBased):

    def __init__(self, name, cost, st, sp, sh, pa, te):
        super().__init__(st, sp, sh, pa, te)
        self.name = name
        self.cost = cost


class EquipmentSet(StatBased):

    def __init__(self, head, arms, body, legs):
        pieces = [head, arms, body, legs]
        super().__init__(
            sum([piece.get(Stat.ST) for piece in pieces]),
            sum([piece.get(Stat.SP) for piece in pieces]),
            sum([piece.get(Stat.SH) for piece in pieces]),
            sum([piece.get(Stat.PA) for piece in pieces]),
            sum([piece.get(Stat.TE) for piece in pieces]),
        )
        self.head = head
        self.arms = arms
        self.body = body
        self.legs = legs

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
        ('Shellfish', 300, -2, 2, -1, -1, 2),
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
        ('Barrel', 300, -2, -2, 2, 1, 1),
        ('Shellfish', 300, 1, 2, -2, -2, 1),
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
        ('Shellfish', 300, -2, 2, 1, -2, 1),
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
        ('Shellfish', 300, -2, 2, -2, 1, 1),
    ]
}


head_pieces = [Equipment(*piece) for piece in __raw_equipment['head']]
arm_pieces = [Equipment(*piece) for piece in __raw_equipment['arms']]
body_pieces = [Equipment(*piece) for piece in __raw_equipment['body']]
leg_pieces = [Equipment(*piece) for piece in __raw_equipment['legs']]
