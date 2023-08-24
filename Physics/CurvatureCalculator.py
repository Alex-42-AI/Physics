from math import cos, acos, pi
EarthRadius = 6371000


def horizon_drop_angle(viewer_elevation: float = 1.8):
    return acos(EarthRadius / (EarthRadius + viewer_elevation))


def horizon_distance(viewer_elevation: float = 1.8):
    return horizon_drop_angle(viewer_elevation) * EarthRadius


def calculate_hidden(distance: float, viewer_elevation: float = 1.8):
    horizon = horizon_distance(viewer_elevation)
    if distance <= horizon:
        return 0
    diff_angle = (distance - horizon) / EarthRadius
    if diff_angle >= pi / 2:
        return float('inf')
    total_elevation_at_location = EarthRadius / cos(diff_angle)
    return total_elevation_at_location - EarthRadius


print()
