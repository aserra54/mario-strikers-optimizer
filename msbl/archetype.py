from msbl.stat import Stat, StatBased


class Archetype:

    def __init__(self, name, checker, sorter):
        self.name = name
        self.checker = checker
        self.sorter = sorter

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


class StatSorter:

    def __init__(self, *order):
        self.order = order
    
    def sort(self, equipped_players):
        def key(equipped_player):
            value = 0
            for i, getter in enumerate(self.order):
                mult = int(pow(100, len(self.order) - i))
                value += mult * getter(equipped_player)
            return value
        return sorted(equipped_players, key=key, reverse=True)


_ST = lambda p: p.get(Stat.ST)
_SP = lambda p: p.get(Stat.SP)
_SH = lambda p: p.get(Stat.SH)
_PA = lambda p: p.get(Stat.PA)
_TE = lambda p: p.get(Stat.TE)
SUM = lambda s1, s2: lambda p: s1(p) + s2(p)


archetypes = [
    Archetype('Defender',   StatChecker(st=17, sp=17, pa=9, te=5),  StatSorter(SUM(_ST, _SP), _SP, _ST, SUM(_PA, _TE), _PA, _TE)),
    Archetype('Midfielder', StatChecker(st=17, sp=9, pa=17, te=5),  StatSorter(SUM(_ST, _PA), _ST, _PA, SUM(_SP, _TE), _SP, _TE)),
    Archetype('Playmaker',  StatChecker(st=9, sp=17, pa=17, te=9),  StatSorter(SUM(_SP, _PA), _PA, _SP, SUM(_ST, _TE), _TE, _ST)),
    Archetype('Sniper',     StatChecker(st=10, sp=7, sh=17, te=17), StatSorter(SUM(_SH, _TE), _SH, _TE, SUM(_ST, _SP), _ST, _SP)),
    Archetype('Striker',    StatChecker(st=17, sp=7, sh=17, te=10), StatSorter(SUM(_ST, _SH), _SH, _ST, SUM(_TE, _SP), _TE, _SP)),
]
