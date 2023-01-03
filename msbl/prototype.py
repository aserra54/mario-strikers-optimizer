from dataclasses import dataclass


@dataclass
class Prototype:
    name: str
    strength: str
    speed: str
    shooting: str
    passing: str
    technique: str
    primary: str

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
    Prototype(name='Defender', strength='17+', speed='17+', shooting='-', passing='8+', technique='5+', primary=['strength', 'speed']),
    Prototype(name='Finesse', strength='-', speed='14+', shooting='9+', passing='8+', technique='14+', primary=['speed', 'technique']),
    Prototype(name='Halfback', strength='14+', speed='8+', shooting='9+', passing='-', technique='14+', primary=['strength', 'technique']),
    Prototype(name='Midfielder', strength='17+', speed='9+', shooting='-', passing='17+', technique='-', primary=['strength', 'passing']),
    Prototype(name='Playmaker', strength='9+', speed='17+', shooting='-', passing='17+', technique='4+', primary=['speed', 'passing']),
    Prototype(name='Sniper', strength='9+', speed='4+', shooting='17+', passing='-', technique='17+', primary=['shooting', 'technique']),
    Prototype(name='Speedster', strength='4+', speed='17+', shooting='17+', passing='-', technique='9+', primary=['speed', 'shooting']),
    Prototype(name='Striker', strength='17+', speed='7+', shooting='17+', passing='-', technique='6+', primary=['strength', 'shooting']),
    Prototype(name='Sweeper', strength='8+', speed='9+', shooting='-', passing='14+', technique='14+', primary=['passing', 'technique']),
    Prototype(name='Winger', strength='8+', speed='9+', shooting='14+', passing='14+', technique='-', primary=['shooting', 'passing']),
]
