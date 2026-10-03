from math import cos, acos, pi, inf

EarthRadius = 6371000


def horizon_drop_angle(h: float = 1.8) -> float:
    """
    :param h: Elevation of observer's point of view
    :return: The angle the horizon drops bellow the middle from the observer's point of view
    """

    return acos(EarthRadius / (EarthRadius + h))


def horizon_distance(h: float = 1.8) -> float:
    """
    :param h: Elevation of observer's point of view
    :return: Distance to the horizon from the observer's point of view
    """

    return horizon_drop_angle(h) * EarthRadius


def calculate_hidden(d: float, h: float = 1.8) -> float:
    """
    Calculate the height hidden behind Earth's curvature for an object
    located at a given surface distance.

    The calculation assumes a spherical Earth and that the observed object
    extends vertically from Earth's surface.

    :param d: Surface distance from the observer's subpoint to the object in m
    :param h: Observer height above Earth's surface in m
    :return: Height hidden by Earth's curvature in m
    """

    return max(0, EarthRadius * EarthRadius / ((EarthRadius + h) * cos(d / EarthRadius)) - EarthRadius)
