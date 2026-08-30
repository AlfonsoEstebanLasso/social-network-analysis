"""Provided by course materials.

Simple discrete-time epidemic propagation function distributed with the
UOC Social Network Analysis course assignment (PEC2). Included here only
so that communities_and_epidemics.ipynb can run; it is NOT my own code.
"""

import random

def propagate(network, seed, probability, steps):
    infected = [seed]
    pocket = [seed]
    time = 0
    while time < steps:
        time += 1
        # propagate
        new_pocket = []
        for seed in pocket:
            for node in network.neighbors(seed):
                if node not in infected and random.random() < probability:
                    infected.append(node)
                    new_pocket.append(node)
        pocket = new_pocket[:]
    return len(infected)
