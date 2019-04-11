from check.acyclicity import MazeAcyclicityChecker
from check.connectivity import MazeConnectivityChecker


def is_fully_connected(maze):
    return MazeConnectivityChecker(maze).is_fully_connected()


def is_acyclic(maze):
    return MazeAcyclicityChecker(maze).is_acyclic()
