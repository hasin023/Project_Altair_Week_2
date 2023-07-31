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
        # South means the opposite of North, so we subtract 1 from y
        'S': (0, -1),
        # West means the opposite of East, so we subtract 1 from x
        'W': (-1, 0)
    }

    # The rover's initial position is assumed to be at coordinates (0, 0), Facing North.
    x, y = 0, 0
    direction = 'N'

    # Helper function to turn the rover
    def turn_rover(current_direction, turn_direction):
        # TODO - Turn to Rover



    for i in instructions:
        if i == 'F':
            # From the Directions dictionary & the current directtion, we get (x, y) from [0] & [1] respectively
            move_in_x = directions[direction][0]
            move_in_y = directions[direction][1]

            # We add the move_in_x & move_in_y to the current x & y coordinates
            current_x = x + move_in_x
            current_y = y + move_in_y


            # If the current x is greater than 0 and less than rows, it's valid as x moves in rows
            # If the current y is greater than 0 and less than columns, it's valid as y moves in columns
            if 0 <= current_x < rows and 0 <= current_y < columns:
                x= current_x
                y = current_y

        elif i in {'L', 'R'}:
            #TODO - Turn the rover

    return x, y, direction


instructions = "FFLFFRFL"
grid_size = (5, 5)
final_position = process_instructions(instructions, grid_size)
print(final_position)

# Example Output: (0, 3, 'W')
