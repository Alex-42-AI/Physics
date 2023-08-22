from math import sqrt, sin, cos, radians

g = 9.80665
c = 299792458
G = 6.673848e-11
au = 149597870700
SunMass = 1.9884849805923904e+30
MoonDistance = 384300000

def time_to_fall(height: float, a: float = g):
    return sqrt(height / a)


def speed_by_the_end_of_falling(height: float, a: float = g):
    return a * time_to_fall(height, a)


def maximal_reachable_height(v: float, a: float = g):
    return v ** 2 / (2 * a)


def final_position_of_object_thrown_into_the_air(alpha: float, v: float, a: float = g):
    return 2 * v * cos(radians(alpha)) * time_to_fall(maximal_reachable_height(v * sin(radians(alpha)), a), a)


def objects_speeds_after_impact(m1: float, v11: float, m2: float, v21: float):
    return (v11 - v21) * (m1 - m2) / (m1 + m2) + v21, 2 * m1 * (v11 - v21) / (m1 + m2) + v21


def object_speed_at_certain_point_on_its_orbit(mass: float, distance: float):
    return sqrt(G * mass / distance)


def total_speed_in_relativity(v0: float, v1: float):
    return (v0 + v1) / (1 + v0 * v1 / c ** 2)


def contraction_in_relativity(v: float):
    return 1 / sqrt(1 - (v / c) ** 2)


print()
