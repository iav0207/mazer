from generator.facade import generate_eller
from render.facade import render_as_image, render_as_text

if __name__ == '__main__':
    size = 100
    maze = generate_eller(size)
    render_as_text(maze)
    render_as_image(maze)
