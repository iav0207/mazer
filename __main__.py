from eller_generator import Eller
from img_renderer import ImageRenderer
from text_renderer import TextMazeRenderer

if __name__ == '__main__':
    size = 100
    maze = Eller.generate_maze_of_size(size)
    TextMazeRenderer.render(maze)
    ImageRenderer.render(maze)
