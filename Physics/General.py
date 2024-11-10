from math import sqrt, sin, cos, radians

g = 9.80665
c = 299792458
G = 6.673848e-11
MoonDistance = 384300000
au = 149597870700
SolarMass = 1.9884849805923904e30

def time_to_fall(height: float, a: float = g):
    return sqrt(2 * height / a)


def speed_by_the_end_of_falling(height: float, a: float = g):
    return a * time_to_fall(height, a)


def maximal_reachable_height(v: float, a: float = g):
    return v ** 2 / (2 * a)


def final_position_of_object_thrown_into_the_air(alpha: float, v: float, initial_elevation: float = 0, final_elevation: float = 0, a: float = g):
    max_height = maximal_reachable_height(v * sin(radians(alpha)), a)
    if final_elevation - initial_elevation > max_height:
        return
    to_the_top = (v_x := v * cos(radians(alpha))) * time_to_fall(max_height, a)
    from_the_top = v_x * time_to_fall(max_height - final_elevation + initial_elevation, a)
    return to_the_top + from_the_top, final_elevation


def objects_speeds_after_impact(m1: float, v1: float, m2: float, v2: float):
    return (v1 - v2) * (m1 - m2) / (m1 + m2) + v2, 2 * m1 * (v1 - v2) / (m1 + m2) + v2


def object_speed_at_certain_point_on_its_orbit(mass: float, distance: float):
    return sqrt(G * mass / distance)


def total_speed_in_relativity(v0: float, v1: float):
    return (v0 + v1) / (1 + v0 * v1 / c ** 2)


def contraction_in_relativity(v: float):
    return 1 / sqrt(1 - (v / c) ** 2)
