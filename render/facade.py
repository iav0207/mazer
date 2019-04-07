from render.image import ImageMazeRenderer
from render.text import TextMazeRenderer


def render_as_text(maze):
    TextMazeRenderer.render(maze)


def render_as_image(maze):
    ImageMazeRenderer.render(maze)
