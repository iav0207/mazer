from os import linesep as nl

from vo import Maze


class TextMazeRenderer:
    @staticmethod
    def render(maze: Maze):
        n = 3 * maze.n
        board = [[]] * n
        for i in range(0, n):
            board[i] = [True] * n

        def convert(maze_coord):
            return 1 + 3 * maze_coord

        for edge in maze.get_all_edges():
            xr = {convert(vtx.x) for vtx in edge.v}
            yr = {convert(vtx.y) for vtx in edge.v}
            for x in range(min(xr), max(xr) + 1):
                for y in range(min(yr), max(yr) + 1):
                    board[x][y] = False
        board[0][1] = False
        board[n-1][n-2] = False

        with open('out.txt', 'w') as f:
            f.write(nl.join([''.join(u"\u2588" if cell else ' ' for cell in row) for row in board]))
