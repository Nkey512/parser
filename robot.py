import math

# входная программа управления роботом
code = (
    'move 100',
    'turn -90',
    'set soap',
    'start',
    'move 50',
    'stop'
)

# режимы работы устройства очистки
WATER = 1  # полив водой
SOAP = 2  # полив мыльной пеной
BRUSH = 3  # чистка метлой

# текущий режим работы устройства очистки
state = WATER

# текущие позиция и угол (ориентация) робота
x = 0.0
y = 0.0
angle = 0


def move(curr_x, curr_y, curr_angle, distance):
    angle_rads = curr_angle * (math.pi/180.0)
    new_x = curr_x + int(distance) * math.cos(angle_rads)
    new_y = curr_y + int(distance) * math.sin(angle_rads)
    return new_x, new_y


def turn(curr_angle, angle):
    return curr_angle + int(angle)


def set(new_state):
    if new_state == 'water':
        return WATER
    if new_state == 'soap':
        return SOAP
    if new_state == 'brush':
        return BRUSH


# главная программа
for command in code:
    cmd = command.split(' ')

    if cmd[0] == 'move':
        x, y = move(x, y, angle, cmd[1])
        print('POS(', x, ',', y, ')')

    elif cmd[0] == 'turn':
        angle = turn(angle, cmd[1])
        print('ANGLE', angle)

    elif cmd[0] == 'set':
        state = set(cmd[1])
        print('STATE', state)

    elif cmd[0] == 'start':
        print('START WITH', state)

    elif cmd[0] == 'stop':
        print('STOP')
