from eller_generator import EllerGenerator
from text_renderer import TextMazeRenderer


if __name__ == '__main__':
    size = 100
    TextMazeRenderer.render(EllerGenerator(size).generate())
