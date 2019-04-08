from PIL import Image, ImageDraw

from model import Maze, Edge, Vertex
from render.path import build_output_path


class ImageMazeRenderer:
    line_width = 2

    @staticmethod
    def render(maze: Maze):

        lw = ImageMazeRenderer.line_width
        dlw = 2 * lw

        def convert(maze_coord):
            return dlw * maze_coord + dlw

        img_size = convert(maze.n) + lw
        image = Image.new('RGB', (img_size, img_size), color='black')
        drawer = ImageDraw.Draw(image)

        def as_box(e: Edge):
            xr = {convert(vtx.x) for vtx in e.v}
            yr = {convert(vtx.y) for vtx in e.v}
            return min(xr), min(yr), max(xr) + 1, max(yr) + 1

        def draw(*edges):
            for e in edges:
                drawer.rectangle(as_box(e), fill='white')

        entrance = Edge(Vertex(-1, 0), Vertex(0, 0))
        the_exit = Edge(Vertex(maze.n - 1, maze.n - 1), Vertex(maze.n, maze.n - 1))

        draw(*maze.get_all_edges())
        draw(entrance, the_exit)

        image.save(build_output_path('jpg'), 'JPEG')

