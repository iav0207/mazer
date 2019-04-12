from render.image import ImageMazeRenderer
from render.text import TextMazeRenderer


def render_as_text(maze, filename=None):
    TextMazeRenderer.render(maze, filename=filename)


def render_as_image(maze, solution=None, filename=None):
    ImageMazeRenderer.render(maze, solution=solution, filename=filename)
