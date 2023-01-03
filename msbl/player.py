from collections import namedtuple
from dataclasses import dataclass
from msbl.equipment import EquipmentSet


Player = namedtuple('Player', 'name strength speed shooting passing technique')


@dataclass
class EquippedPlayer:
    player: Player
    set: EquipmentSet

    @property
    def strength(self):
        return self.__safe_stat(self.player.strength + self.set.strength)

    @property
    def speed(self):
        return self.__safe_stat(self.player.speed + self.set.speed)

    @property
    def shooting(self):
        return self.__safe_stat(self.player.shooting + self.set.shooting)

    @property
    def passing(self):
        return self.__safe_stat(self.player.passing + self.set.passing)

    @property
    def technique(self):
        return self.__safe_stat(self.player.technique + self.set.technique)

    def __safe_stat(self, x):
        return max(min(x, 25), 1)


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


def __to_player(player):
    return Player(name=player[0], strength=player[1], speed=player[2], shooting=player[3], passing=player[4],
        technique=player[5])


players = [__to_player(player) for player in __raw_players]
