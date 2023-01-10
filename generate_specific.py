#strength speed shooting passing technique

from msbl.archetype import *
from msbl.equipment import *
from msbl.player import *
from msbl.stat import *


def generate_equipment_sets():
    sets = []
    for h in head_pieces:
        for a in arm_pieces:
            for b in body_pieces:
                for l in leg_pieces:
                    sets.append(EquipmentSet(h, a, b, l))
    return sets


def generate_candidates(p_name, t_name, equipment_sets):
    for t in archetypes:
        if t.name != t_name:
            continue
        candidates = []
        for p in players:
            if p.name != p_name:
                continue
            for e in equipment_sets:
                ep = EquippedPlayer(p, e)
                if t.satisfies(ep):
                    candidates.append(ep)
        print_top_candidates(t, candidates, 20)


def print_top_candidates(t, candidates, max):

    ordered_candidates = t.sorter.sort(candidates)
    top_candidates = ordered_candidates[:max]

    for ep in top_candidates:
        elems = [
            ep.player.name,
            t.name,
            ep.set.cost,
            ep.set.head.name, ep.set.arms.name, ep.set.body.name, ep.set.legs.name,
            ep.get(Stat.ST), ep.get(Stat.SP), ep.get(Stat.SH), ep.get(Stat.PA), ep.get(Stat.TE),
        ]
        print('\t'.join([str(elem) for elem in elems]))


def main():
    equipment_sets = generate_equipment_sets()
    generate_candidates('Donkey Kong', 'XXX', equipment_sets)


if __name__ == '__main__':
    main()
