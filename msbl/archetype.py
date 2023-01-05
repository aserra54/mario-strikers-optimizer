from msbl.stat import Stat, StatBased


class Archetype:

    def __init__(self, name, checker):
        self.name = name
        self.checker = checker

    def satisfies(self, equipped_player):
        return self.checker.satisfies(equipped_player)


class StatChecker(StatBased):

    def __init__(self, st=0, sp=0, sh=0, pa=0, te=0):
        super().__init__(st, sp, sh, pa, te)

    def satisfies(self, equipped_player):
        for stat in [Stat.ST, Stat.SP, Stat.SH, Stat.PA, Stat.TE]:
            if equipped_player.get(stat) < self.get(stat):
                return False
        return True


archetypes = [
    Archetype('Striker', StatChecker(st=17, sp=7, sh=17, te=10)),
]
