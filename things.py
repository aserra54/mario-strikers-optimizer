#strength speed shooting passing technique

from msbl.equipment import *
from msbl.player import *
from msbl.prototype import *


# player name => prototype name => equipped player
candidates = {}


n = 0
for h in head_pieces:
    for a in arm_pieces:
        for b in body_pieces:
            for l in leg_pieces:
                e = EquipmentSet(h, a, b, l)
                for t in prototypes:
                    for p in players:
                        if t.satisfies(p, e):
                            ep = EquippedPlayer(p, e)
                            if p.name not in candidates:
                                candidates[p.name] = {}
                            if t.name not in candidates[p.name]:
                                candidates[p.name][t.name] = []
                            candidates[p.name][t.name].append(ep)
                            n += 1
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
print(f'{n} candidates total')