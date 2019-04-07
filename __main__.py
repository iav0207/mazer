from eller_generator import Eller
from text_renderer import TextMazeRenderer


if __name__ == '__main__':
    size = 100
    TextMazeRenderer.render(Eller.generate_maze_of_size(size))
