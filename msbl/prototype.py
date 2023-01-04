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
    Prototype(name='Defender', strength='17+', speed='21+', shooting='-', passing='9+', technique='-'), # ST+SP
    Prototype(name='Finisher', strength='11+', speed='15+', shooting='12+', passing='7+', technique='15+'), # SP+TE
    Prototype(name='Midfielder', strength='18+', speed='11+', shooting='-', passing='17+', technique='-'), # ST+PA
    Prototype(name='Playmaker', strength='10+', speed='18+', shooting='-', passing='18+', technique='-'), # SP+PA
    Prototype(name='Poacher', strength='16+', speed='7+', shooting='15+', passing='-', technique='16+'), # ST+TE
    Prototype(name='Sniper', strength='10+', speed='10+', shooting='17+', passing='-', technique='19+'), # SH+TE
    Prototype(name='Speedster', strength='8+', speed='17+', shooting='17+', passing='-', technique='10+'), # SP+SH
    Prototype(name='Striker', strength='17+', speed='7+', shooting='20+', passing='-', technique='10+'), # ST+SH
    Prototype(name='Sweeper', strength='10+', speed='11+', shooting='11+', passing='15+', technique='15+'), # PA+TE
    Prototype(name='Winger', strength='10+', speed='11+', shooting='15+', passing='14+', technique='11+'), # SH+PA
]
