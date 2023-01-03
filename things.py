#strength speed shooting passing technique

from msbl.equipment import *
from msbl.player import *
from msbl.prototype import *


for h in head_pieces:
    for a in arm_pieces:
        for b in body_pieces:
            for l in leg_pieces:
                e = EquipmentSet(h, a, b, l)
                for t in prototypes:
                    for p in players:
                        if t.satisfies(p, e):
                            print('==========')
                            print(f'{p.name} ({t.name})')
                            print('-----')
                            print(f'  Head: {h.name}')
                            print(f'  Arms: {a.name}')
                            print(f'  Body: {b.name}')
                            print(f'  Legs: {l.name}')
                            print(f'  Cost: {e.cost}')
                            print('-----')
                            print(f'  ST: {p.strength + e.strength:2} ({e.strength:+})')
                            print(f'  SP: {p.speed + e.speed:2} ({e.speed:+})')
                            print(f'  SH: {p.shooting + e.shooting:2} ({e.shooting:+})')
                            print(f'  PA: {p.passing + e.passing:2} ({e.passing:+})')
                            print(f'  TE: {p.technique + e.technique:2} ({e.technique:+})')
                            print('==========')
