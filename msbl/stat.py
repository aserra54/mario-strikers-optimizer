from dataclasses import dataclass


class Stat:
    ST = 'strength'
    SP = 'speed'
    SH = 'shooting'
    PA = 'passing'
    TE = 'technique'


@dataclass
class StatBased:

    def __init__(self, st=0, sp=0, sh=0, pa=0, te=0):
        self.stats = {Stat.ST: st, Stat.SP: sp, Stat.SH: sh, Stat.PA: pa, Stat.TE: te}

    def get(self, stat):
        return self.stats[stat]
