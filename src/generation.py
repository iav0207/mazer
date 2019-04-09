from gen.eller import Eller
from gen.recursive_backtracker import RecursiveBacktrackerGenerator


def generate_eller(size):
    return Eller.generate_maze_of_size(size)


def generate_recursive_backtracker(size):
    return RecursiveBacktrackerGenerator(size).generate()
