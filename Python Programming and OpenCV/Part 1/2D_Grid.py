def process_instructions(instructions, grid_size):
    # From grid size tuple, we separate the number of rows and columns
    rows = grid_size[0]
    columns = grid_size[1]

    # We initiate a Dictionary to store the direction values of the rover as (x, y) tuples
    directions = {
        # North means moving up 1 step in the y-axis, so we add 1 to y and keep x the same
        'N': (0, 1),
        # East means moving right 1 step in the x-axis, so we add 1 to x and keep y the same
        'E': (1, 0),
        # Opposite of North
        'S': (0, -1),
        # Opposite of East
        'W': (-1, 0)
    }

    # The rover's initial position is assumed to be at coordinates (0, 0) Facing North.
    x, y = 0, 0
    direction = 'N'

    turns = {'N': 0, 'E': 1, 'S': 2, 'W': 3}

    def Turn(direction, turnDirection):
        # Taking the value of the current direction from the turns dictionary
        directionValue = turns[direction]

        # If the turn direction is 'L', subtract 1 from the direction value
        # If the turn direction is 'R', add 1 to the direction value
        turnOperations = {'L': -1, 'R': 1}

        # When the direction value is greater than 3, we need to reset it to 0
        # So we take the module value of 4 % 4 = 0, And the direction value is reset to 0
        newDirectionValue = (directionValue +
                             turnOperations[turnDirection]) % 4

        newDirection = next(
            key for key, value in turns.items() if value == newDirectionValue)

        return newDirection

    for i in instructions:
        if i == 'F':
            # From the Directions dictionary & the current directtion, we get (x, y) from [0] & [1] respectively
            moveX = directions[direction][0]
            moveY = directions[direction][1]

            # We add the move_in_x & move_in_y to the current x & y coordinates
            newX = x + moveX
            newY = y + moveY

            # If the new x is greater than 0 and less than rows, it's valid as x moves in rows
            # If the new y is greater than 0 and less than columns, it's valid as y moves in columns
            if 0 <= newX < rows and 0 <= newY < columns:
                x = newX
                y = newY

        elif i == 'L' or i == 'R':
            direction = Turn(direction, i)

    return x, y, direction


if __name__ == "__main__":

    instructions = "FFLFFRFL"
    grid_size = (5, 5)
    print(process_instructions(instructions, grid_size))

    # Example Output: (0, 3, 'W')
