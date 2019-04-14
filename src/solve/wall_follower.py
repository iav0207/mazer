from enum import Enum

from model import Maze, Vertex, Solution
from solve import path


class Direction(Enum):
    NORTH = lambda v: Vertex(v.x, v.y + 1)
    EAST = lambda v: Vertex(v.x + 1, v.y)
    SOUTH = lambda v: Vertex(v.x, v.y - 1)
    WEST = lambda v: Vertex(v.x - 1, v.y)

    def __call__(self, *args, **kwargs):
        return self(args[0])


directions_clockwise = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]


def turn_left(direction):
    return directions_clockwise[(directions_clockwise.index(direction) - 1) % len(directions_clockwise)]


def turn_right(direction):
    return directions_clockwise[(directions_clockwise.index(direction) + 1) % len(directions_clockwise)]


def turn_back(direction):
    return turn_left(turn_left(direction))


class Hand(Enum):
    LEFT = turn_left
    RIGHT = turn_right

    @staticmethod
    def opposite(hand):
        return Hand.LEFT if hand is Hand.RIGHT else Hand.RIGHT

    def __call__(self, *args, **kwargs):
        return self(args[0])


class WallFollower:
    def __init__(self, maze: Maze, hand: Hand):
        position = path.Node(maze.start)
        direction = Direction.EAST
        turn_prio = [hand, lambda d: d, Hand.opposite(hand), turn_back]

        while position.val != maze.end:
            candidates = [turn(direction) for turn in turn_prio]
            neighbours = maze.get_accessible_neighbours(position.val)
            direction = next(c for c in candidates if c(position.val) in neighbours)
            position = position.create_child(direction(position.val))

        self.solution = Solution.from_vertices(list(position.as_path()))
