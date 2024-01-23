def main(x1, y1, x2, y2):
    """
    The program expects two (x,y) points,
    and it returns a straight line between the points.

    In the code I refer to the "dominant direction". This is simply the direction
    in which we should go more steps in order to get from the first point to the second.
    For example if these are the points: (1,1) and (1, 11), then y is the "dominant direction"
    because we need to go 10 steps in the y direction and 0 in the x direction.
    """

    res = [(x1,y1)]

    # Determine the directions in which we should move
    x_direction = 1 if x1-x2 < 0 else -1  # 1 means right, -1 means left
    y_direction = 1 if y1-y2 < 0 else -1  # 1 means up, -1 means down

    # Determine the distances
    distance_x = abs(x1-x2)
    distance_y = abs(y1-y2)

    if distance_x == 0 or distance_y == 0:
        return handle_zero_distance(x1,y1,x2,y2)

    # Calculate the ratio between the distances so it will be >= 1.
    # The ratio is approximately the number of steps we need to go in the
    # dominant direction upon every step we go in the non-dominant direction.
    ratio = (distance_x / distance_y) if distance_x >= distance_y else (distance_y / distance_x)

    # Calculate the remainder of the ratio.
    # This is the number of times we need to go an extra step in the dominant direction.
    remainder = (distance_x % distance_y) if distance_x >= distance_y else (distance_y % distance_x)

    # Now we have all the information we need in order to generate the line.

    # Line generation begin:
    x, y = x1, y1
    while x != x2 and y != y2:
        steps = ratio - 1  # The number of steps to go in the dominant direction

        if remainder > 0:  # Decide whether we should go an extra step in the dominant direction
            steps += 1
            remainder -= 1

        # Move {steps} times in the dominant direction
        while steps >= 0:
            if distance_x / distance_y >= 1:
                # then x is the dominant direction and {remainder} times we need to go {ratio+1} steps in the x direction
                x += x_direction
                res.append((x, y))
                steps -= 1
            else:
                # then y is the dominant direction and {remainder} times we need to go {ratio+1} steps in the y direction
                y += y_direction
                res.append((x, y))
                steps -= 1

        # Move one time in the non-dominant direction
        if distance_x / distance_y >= 1:
            y += y_direction
            res.append((x, y))
        else:
            x += x_direction
            res.append((x, y))

    return res


def handle_zero_distance(x1,y1,x2,y2):
    """
    This function handles the edge case when one or more distances are 0.
    This function assumes at least one of the distances is 0.
    """
    res = [(x1,y1)]

    # Determine the directions in which we should move
    x_direction = 1 if x1 - x2 < 0 else -1  # 1 means right, -1 means left
    y_direction = 1 if y1 - y2 < 0 else -1  # 1 means up, -1 means down

    # Determine the distances
    distance_x = abs(x1 - x2)
    distance_y = abs(y1 - y2)

    if distance_x != 0:  # Go in a straight line on the x-axis
        x = x1
        while x != y2:
            x += x_direction
            res.append((x, y1))

    elif distance_y != 0:  # Go in a straight line on the y-axis
        y = y1
        while y != y2:
            y += y_direction
            res.append((x1, y))

    return res


if __name__ == '__main__':
    print(main(2,9, 15,2 ))


