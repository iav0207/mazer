from checks import is_fully_connected, is_acyclic
from generation import generate_eller, generate_recursive_backtracker
from rendering import render_as_image, render_as_text
from solving import find_shortest_path, solve_following_walls


def generate_render_and_check(name, generator):
    size = 100
    maze = generator(size)

    assert is_fully_connected(maze)
    assert is_acyclic(maze)

    def solve_and_print(solution_name, solver):
        solution = solver(maze)
        full_name = f'{name}_{solution_name}'
        print(f'{full_name} maze solution length: {len(solution)}')
        render_as_text(maze, filename=full_name)
        render_as_image(maze, solution=solution, filename=full_name)

    solve_and_print('ShortestPath', find_shortest_path)
    solve_and_print('WallFollower', solve_following_walls)


if __name__ == '__main__':
    generate_render_and_check('Eller', generate_eller)
    generate_render_and_check('RecursiveBacktracker', generate_recursive_backtracker)
