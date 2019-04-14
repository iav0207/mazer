from solve.shortest_path import ShortestPathFinder
from solve.wall_follower import WallFollower, Hand


def find_shortest_path(maze):
    return ShortestPathFinder(maze).solution


def solve_following_walls(maze, hand=Hand.LEFT):
    return WallFollower(maze, hand).solution
