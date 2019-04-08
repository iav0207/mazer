from collections import deque

from model import Maze


class MazeConnectivityChecker:
    def __init__(self, maze: Maze):
        self.maze = maze
        self.visited = set()
        self.island_sizes = list()

        for v in self.maze.map.keys():
            if v not in self.visited:
                self.traverse_island(v)

    def traverse_island(self, start_vertex):
        visited_at_start = len(self.visited)
        todo = deque([start_vertex])

        def visit(v):
            self.visited.add(v)
            for neighbor in self.maze.get_accessible_neighbours(v):
                if neighbor not in self.visited:
                    todo.append(neighbor)

        while todo:
            visit(todo.pop())

        self.island_sizes.append(len(self.visited) - visited_at_start)

    def is_fully_connected(self):
        return len(self.visited) == self.maze.n ** 2
