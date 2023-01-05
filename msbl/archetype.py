from dataclasses import dataclass


class Archetype:

    def __init__(self, name, checker):
        self.name = name
        self.checker = checker

    def satisfies(self, equipped_player):
        return self.checker.satisfies(equipped_player)


@dataclass
class StatChecker:
    st: int = 0
    sp: int = 0
    sh: int = 0
    pa: int = 0
    te: int = 0

    def satisfies(self, equipped_player):
        if equipped_player.strength < self.st:
            return False
        if equipped_player.speed < self.sp:
            return False
        if equipped_player.shooting < self.sh:
            return False
        if equipped_player.passing < self.pa:
            return False
        if equipped_player.technique < self.te:
            return False
        return True


archetypes = [
    Archetype('Striker', StatChecker(st=17, sp=7, sh=17, te=10)),
]
