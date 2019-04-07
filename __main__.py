from eller_generator import Eller
from text_renderer import TextMazeRenderer


if __name__ == '__main__':
    size = 100
    TextMazeRenderer.render(Eller.MazeGenerator(size).generate())
