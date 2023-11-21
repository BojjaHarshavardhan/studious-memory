class Movement:
    def move(self, rover):
        pass

class MoveNorth(Movement):
    def move(self, rover):
        if rover.grid.is_valid_position(rover.x, rover.y + 1) and not rover.grid.has_obstacle(rover.x, rover.y + 1):
            rover.y += 1

class MoveSouth(Movement):
    def move(self, rover):
        if rover.grid.is_valid_position(rover.x, rover.y - 1) and not rover.grid.has_obstacle(rover.x, rover.y - 1):
            rover.y -= 1

class MoveEast(Movement):
    def move(self, rover):
        if rover.grid.is_valid_position(rover.x + 1, rover.y) and not rover.grid.has_obstacle(rover.x + 1, rover.y):
            rover.x += 1

class MoveWest(Movement):
    def move(self, rover):
        if rover.grid.is_valid_position(rover.x - 1, rover.y) and not rover.grid.has_obstacle(rover.x - 1, rover.y):
            rover.x -= 1

class Rover:
    def __init__(self, x, y, direction, grid):
        self.x = x
        self.y = y
        self.direction = direction
        self.grid = grid
        self.movements = {
            'N': MoveNorth(),
            'S': MoveSouth(),
            'E': MoveEast(),
            'W': MoveWest()
        }

    def move(self):
        self.movements[self.direction].move(self)

    def turn_left(self):
        turns = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
        self.direction = turns[self.direction]

    def turn_right(self):
        turns = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
        self.direction = turns[self.direction]

    def execute_commands(self, commands):
        for command in commands:
            if command == 'M':
                self.move()
            elif command == 'L':
                self.turn_left()
            elif command == 'R':
                self.turn_right()

            if self.grid.has_obstacle(self.x, self.y):
                print("Obstacle detected. Rover cannot move.")
                break

    def actual_dir(self):
        turns = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
        self.direction = turns[self.direction]

    def status_report(self):
        if not self.grid.has_obstacle(self.x, self.y):
            print(f"Rover is at ({self.x}, {self.y}) facing {self.direction}. No obstacles detected.")
        else:
            print(f"Rover is at ({self.x}, {self.y}) facing {self.direction}.")

# Example Usage
class Grid:
    def __init__(self, size, obstacles):
        self.size = size
        self.obstacles = obstacles

    def is_valid_position(self, x, y):
        return 0 <= x < self.size[0] and 0 <= y < self.size[1]

    def has_obstacle(self, x, y):
        return (x, y) in self.obstacles

grid_size = (10, 10)
starting_position = (0, 0, 'N')
obstacles = [(2, 2), (3, 5)]
commands = ['M','M','R','M','L','M']

grid = Grid(grid_size, obstacles)
rover = Rover(*starting_position, grid)

rover.execute_commands(commands)
rover.actual_dir()
rover.status_report()
