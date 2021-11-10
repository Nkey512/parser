import math


def move(curr_x, curr_y, curr_angle, distance):
    angle_rads = curr_angle * (math.pi/180.0)
    new_x = curr_x + int(distance) * math.cos(angle_rads)
    new_y = curr_y + int(distance) * math.sin(angle_rads)
    return new_x, new_y
