from math import cos, acos, pi
Earth_radius = 6371000


def horizon_drop_angle(viewer_elevation: float = 1.8):
    return acos(Earth_radius / (Earth_radius + viewer_elevation))


def horizon_distance(viewer_elevation: float = 1.8):
    return horizon_drop_angle(viewer_elevation) * Earth_radius


def calculate_hidden(distance: float, viewer_elevation: float = 1.8):
    horizon = horizon_distance(viewer_elevation)
    if distance <= horizon:
        return 0
    diff_angle = (distance - horizon) / Earth_radius
    if diff_angle >= pi / 2:
        return float('inf')
    total_elevation_at_location = Earth_radius / cos(diff_angle)
    return total_elevation_at_location - Earth_radius


print()
