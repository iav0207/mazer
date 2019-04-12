from checks import is_fully_connected, is_acyclic
from generation import generate_eller, generate_recursive_backtracker
from rendering import render_as_image, render_as_text
from solving import find_shortest_path


def generate_render_and_check(name, generator):
    size = 100
    maze = generator(size)
    render_as_text(maze, filename=name)
    render_as_image(maze, filename=name)

    assert is_fully_connected(maze)
    assert is_acyclic(maze)

    print(f'{name} maze solution length: {len(find_shortest_path(maze))}')


if __name__ == '__main__':
    generate_render_and_check('Eller', generate_eller)
    generate_render_and_check('RecursiveBacktracker', generate_recursive_backtracker)
