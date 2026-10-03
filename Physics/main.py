from math import sqrt, sin, cos, radians, pi

g = 9.80665
c = 299792458
G = 6.6743e-11
au = 149597870700
MoonDistance = 384300000
SolarMass = 1.9884849805923904e30


def speed_by_the_end_of_falling(height: float, a: float = g) -> float:
    """
    :param height: Vertical distance fallen from the initial position in m
    :param a: Constant downward acceleration in m/s^2
    :return: Time required for an object initially at rest to fall the given distance in s
    """

    return sqrt(2 * a * height)


def time_to_fall(height: float, a: float = g) -> float:
    """
    :param height: Initial object elevation in m
    :param a: Acceleration, g by default in m/s^2
    :return: How long an object will take to fall from a given height in s
    """

    return speed_by_the_end_of_falling(height, a) / a


def kinetic_energy(m: float, v: float) -> float:
    """
    :param m: Object mass in kg
    :param v: Object speed in m/s
    :return: Object kinetic energy in J
    """

    return m * v * v / 2


def potential_energy(m: float, h: float, a: float = g) -> float:
    """
    :param m: Object mass in kg
    :param h: Object elevation in m
    :param a: Celestial body gravitational acceleration in m/s^2
    :return: Object potential energy on given celestial body at a given elevation in J
    """

    return m * a * h


def maximal_reachable_height(v: float, a: float = g) -> float:
    """
    :param v: Object initial vertical speed in m/s
    :param a: Celectial body acceleration in m/s^2
    :return: The maximal elevation of the object from the starting position in m
    """

    return v * v / (2 * a)


def final_position_of_object_thrown_into_the_air(alpha: float, v: float, start_elevation: float = 0,
                                                 end_elevation: float = 0, a: float = g) -> None | tuple[float, float]:
    """
    Calculate where an ideal projectile reaches a specified elevation.

    The projectile is assumed to experience constant downward acceleration
    and no air resistance. The launch point is treated as x = 0.

    :param alpha: Launch angle above the horizontal, in degrees
    :param v: Initial speed, in m/s
    :param start_elevation: Initial vertical position
    :param end_elevation: Target vertical position
    :param a: Constant downward acceleration, g by default
    :return: (horizontal displacement, end_elevation), or None if the target elevation cannot be reached
    """

    max_height = maximal_reachable_height(v * sin(alpha := radians(alpha)), a)

    if end_elevation - start_elevation > max_height:
        return

    to_the_top = (v_x := v * cos(alpha)) * time_to_fall(max_height, a)
    from_the_top = v_x * time_to_fall(max_height - end_elevation + start_elevation, a)

    return to_the_top + from_the_top, end_elevation


def objects_speeds_after_impact(m1: float, v1: float, m2: float, v2: float) -> tuple[float, float]:
    """
    Calculate the velocities after a one-dimensional perfectly elastic collision.

    The objects move along the same line. Velocities are signed, so their
    directions are represented by their signs.

    :param m1: Mass of object 1 in kg
    :param v1: Initial velocity of object 1 in m/s
    :param m2: Mass of object 2 in kg
    :param v2: Initial velocity of object 2 in m/s
    :return: Final velocities of objects 1 and 2 in m/s
    """

    return (v1 - v2) * (m1 - m2) / (m1 + m2) + v2, 2 * m1 * (v1 - v2) / (m1 + m2) + v2


def object_speed_at_certain_point_on_its_orbit(m: float, r: float, a: float = 0) -> float:
    """
    An object orbits a massive celestial body. Its speed varies based on its distance from it
    :param m: Mass of the celestial body
    :param r: Object distance from the celestial body
    :param a: Eliptical semi-major axis of the object's orbit
    :return: Object speed at given distance from the celestial body
    """

    if not a:
        a = r

    return sqrt(G * m * (2 / r - 1 / a))


def total_speed_in_relativity(v0: float, v1: float) -> float:
    """
    :param v0: Speed of object 1 relative to a stationary observer
    :param v1: Speed of object 2 relative to object 1
    :return: The total speed of object 2 relative to the stationary observer
    """

    return (v0 + v1) / (1 + v0 * v1 / c ** 2)


def lorentz_factor(v: float) -> float:
    """
    :param v: Object speed relative to an observer in m/s
    :return: Lorentz factor
    """

    return 1 / sqrt(1 - (v / c) ** 2)


def schwarzschild_radius(m: float) -> float:
    """
    :param m: Body mass in kg
    :return: The schwarzschild radius of the body in m
    """

    return 2 * G * m / c ** 2


def distance_from_singularity(m: float, r: float, t: float = 0) -> float:
    """
    Calculate the Schwarzschild radial coordinate of an object in radial
    free fall from rest, using the object's proper time.

    The black hole is assumed to be non-rotating and uncharged. The object
    is released from rest at the initial Schwarzschild radial coordinate r.

    :param m: Black hole mass in kg
    :param r: Initial Schwarzschild radial coordinate in m
    :param t: Proper time elapsed since release in s
    :return: Current Schwarzschild radial coordinate in m
    """

    if t >= (sing_t := time_to_fall_into_singularity(m, r)):
        return 0

    eta = factor = pi * t / sing_t

    for _ in range(20):
        eta -= (eta + sin(eta) - factor) / (1 + cos(eta))

    return r * (1 + cos(eta)) / 2


def time_to_fall_into_singularity(m: float, r: float) -> float:
    """
    Calculate the proper time experienced by an object released from rest at Schwarzschild
    radius r before reaching the singularity of a non-rotating, uncharged black hole.

    :param m: Black hole mass in kg
    :param r: Initial Schwarzschild radial coordinate in m
    :return: Proper time until reaching the singularity, in s
    """

    return pi * sqrt(r ** 3 / (8 * G * m))
