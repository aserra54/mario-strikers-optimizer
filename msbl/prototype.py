from dataclasses import dataclass


@dataclass
class Prototype:
    name: str
    strength: str
    speed: str
    shooting: str
    passing: str
    technique: str

    def satisfies(self, player, equipment_set):
        return (
            self.__stat_satisfy(self.strength, player.strength + equipment_set.strength) and
            self.__stat_satisfy(self.speed, player.speed + equipment_set.speed) and
            self.__stat_satisfy(self.shooting, player.shooting + equipment_set.shooting) and
            self.__stat_satisfy(self.passing, player.passing + equipment_set.passing) and
            self.__stat_satisfy(self.technique, player.technique + equipment_set.technique)
        )

    def __stat_satisfy(self, stat, total):
        if stat == '-':
            return True
        elif stat.endswith('+'):
            minimum = int(stat[:-1])
            return total >= minimum
        raise ValueError(f'Cannot parse: {stat}')


prototypes = [
    Prototype(name='Striker', strength='17+', speed='7+', shooting='17+', passing='-', technique='7+'),
    Prototype(name='Defender', strength='17+', speed='17+', shooting='-', passing='7+', technique='-'),
]
