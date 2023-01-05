from dataclasses import dataclass
from msbl.equipment import EquipmentSet
from msbl.stat import Stat, StatBased


class Player(StatBased):

    def __init__(self, name, st, sp, sh, pa, te):
        super().__init__(st, sp, sh, pa, te)
        self.name = name


class EquippedPlayer(StatBased):

    def __init__(self, player, set):
        safe = lambda x: max(min(x, 25), 1)
        super().__init__(
            safe(player.get(Stat.ST) + set.get(Stat.ST)),
            safe(player.get(Stat.SP) + set.get(Stat.SP)),
            safe(player.get(Stat.SH) + set.get(Stat.SH)),
            safe(player.get(Stat.PA) + set.get(Stat.PA)),
            safe(player.get(Stat.TE) + set.get(Stat.TE)),
        )
        self.player = player
        self.set = set


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


players = [Player(*player) for player in __raw_players]
