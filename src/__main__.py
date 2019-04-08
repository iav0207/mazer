from generation import generate_eller
from rendering import render_as_image, render_as_text

if __name__ == '__main__':
    size = 100
    maze = generate_eller(size)
    render_as_text(maze)
    render_as_image(maze)
