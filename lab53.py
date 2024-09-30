#!/usr/bin/env python3

import itertools as it
from math import factorial

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

gen_motives = it.permutations(notes, 4)
#for motif in gen_motives:
#    print(motif)

hit_candidates = factorial(len(notes))/factorial(len(notes)-4)
print(int(hit_candidates))

gen_motives_v2 = it.product(notes, 4)
for motif in gen_motives_v2:
    print(motif)

hit_candidates_v2 = pow(len(notes), 4)
print(int(hit_candidates_v2))
