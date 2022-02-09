from itertools import product

x1 = 56
x2 = 76
y1 = -162
y2 = -134

target_area = list(product(range(x1, x2 + 1), range(y1, y2 + 1)))


# print(target_area)


def check_x_position(x):
    if x > 0:
        return x - 1
    elif x < 0:
        return x + 1
    else:
        return 0


def outside_of_target_area(x, y):
    # It fell before the trench
    if x < x1 and y < y1:
        return True
    # It overshot
    if x > x2:
        return True
    # It is falling forever
    if x == 0 and y < y1:
        return True
    else:
        return False


starters = []  # All starting velocities which land in the target area


def check_if_lands_in_trench(initial_velocity):
    next_position = initial_velocity
    while not outside_of_target_area(next_position[0], next_position[1]):
        next_position = (next_position[0] + check_x_position(next_position[0]),
                         next_position[1] + next_position[1] - 1)
        if next_position in target_area:
            starters.append(initial_velocity)


# Starting at 0 makes projectile falling forever, starting 1 means it gets stuck in infinite loop
# Starting higher than x boundary, makes projectile overshoot from the start
for x in range(2, 1000):
    # Brute forcing shooting up or down starting from the lowest point just before target
    for y in range(-1000, 1000):
        if y != 1:
            initial_velocity = (x, y)
            check_if_lands_in_trench(initial_velocity)

# Check all starter velocities and record the highest reached y value (but in the negatives)
y_values = [100]


def loop_through_starters():
    global starter, next_position, initial_y
    for starter in starters:
        next_position = starter
        initial_y = starter[1]
        while not outside_of_target_area(next_position[0], next_position[1]):
            if initial_y > next_position[1]:
                y_values.append(next_position[1])
            next_position = (next_position[0] + check_x_position(next_position[0]),
                             next_position[1] + next_position[1] - 1)


loop_through_starters()
print(str(min(y_values)))  # The most negative point which corresponds to the highest height at one step

# Now we need to sum up the height increments from starting velocity to the highest point (thanks to the hints on reddit)
sum = 0
for y in range(0, abs(min(y_values)) + 1):
    sum = sum + y

print(str(sum))
