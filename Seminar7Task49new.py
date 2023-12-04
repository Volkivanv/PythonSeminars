from math import pi


def find_farthest_orbit(orbits):
    print(max([orbit for orbit in orbits if orbit[0] != orbit[1]], key=lambda orb: pi * orb[0] * orb[1]))


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

find_farthest_orbit(orbits)

lst = []