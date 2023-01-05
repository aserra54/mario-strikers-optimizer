#strength speed shooting passing technique

from msbl.archetype import *
from msbl.equipment import *
from msbl.player import *
from msbl.stat import *


def generate_candidates():
    # (player, prototype, equipped player)
    candidates = []
    for h in head_pieces:
        for a in arm_pieces:
            for b in body_pieces:
                for l in leg_pieces:
                    e = EquipmentSet(h, a, b, l)
                    for t in archetypes:
                        for p in players:
                            ep = EquippedPlayer(p, e)
                            if t.satisfies(ep):
                                candidates.append((p, t, ep))
                                # print('==========')
                                # print(f'{p.name} ({t.name})')
                                # print('-----')
                                # print(f'  Head: {h.name}')
                                # print(f'  Arms: {a.name}')
                                # print(f'  Body: {b.name}')
                                # print(f'  Legs: {l.name}')
                                # print(f'  Cost: {e.cost}')
                                # print('-----')
                                # print(f'  ST: {ep.strength:2} ({e.strength:+})')
                                # print(f'  SP: {ep.speed:2} ({e.speed:+})')
                                # print(f'  SH: {ep.shooting:2} ({e.shooting:+})')
                                # print(f'  PA: {ep.passing:2} ({e.passing:+})')
                                # print(f'  TE: {ep.technique:2} ({e.technique:+})')
                                # print('==========')
    return candidates


def emit(candidates):
    # print(len(candidates))
    # return
    for p, t, ep in candidates:
        elems = [
            p.name,
            t.name,
            ep.set.cost,
            ep.set.head.name, ep.set.arms.name, ep.set.body.name, ep.set.legs.name,
            ep.get(Stat.ST), ep.get(Stat.SP), ep.get(Stat.SH), ep.get(Stat.PA), ep.get(Stat.TE),
        ]
        print('\t'.join([str(elem) for elem in elems]))


def main():
    candidates = generate_candidates()
    emit(candidates)


if __name__ == '__main__':
    main()
