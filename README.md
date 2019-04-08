# Maze generation

Inspired by [this article](https://habr.com/ru/post/445378/) and [Daedalus project](http://www.astrolog.org/labyrnth/daedalus.htm).

## Requirements

All modules required to run the app are listed in [requirements.txt](/requirements.txt).

## How to run

If running for the first time, run
```bash
pip3 install -r requirements.txt
```
Then you can just
```bash
python3 src
```
or
```bash
python3 src/__main__.py
```

## Project structure

- [model.py](src/model.py) – model classes
- [gen](src/gen) – the package of maze generation algorithms
- [render](src/render) - the package for maze rendering
- [main](src/__main__.py) – the example script putting the output to
- [out](out/) – the output files directory

## Examples

#### Eller's generation algorithm 100×100
![Eller's generation algorithm](sample_output/maze.jpg?raw=true "Eller's generation algorithm")
