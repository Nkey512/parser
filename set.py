WATER = 1
SOAP = 2
BRUSH = 3


def set(new_state):
    if new_state == 'water':
        return WATER
    if new_state == 'soap':
        return SOAP
    if new_state == 'brush':
        return BRUSH
