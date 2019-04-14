from model import Maze, Solution
from solve import path


def flat_list(lst):
    return [item for sublist in lst for item in sublist]


class ShortestPathFinder:
    def __init__(self, maze: Maze):
        front = [path.Node(maze.start)]
        seen = {maze.start}
        finish = None

        def step_fw(node):
            new_sub_front = []
            for vtx in maze.get_accessible_neighbours(node.val):
                if not node.is_parent_val(vtx) and vtx not in seen:
                    new_node = node.create_child(vtx)
                    seen.add(vtx)
                    new_sub_front.append(new_node)
                    if vtx == maze.end:
                        nonlocal finish
                        finish = new_node
            return new_sub_front

        while not finish:
            front = flat_list([step_fw(n) for n in front])

        self.solution = Solution.from_vertices(list(finish.as_path()))
