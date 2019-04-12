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
You will find the script output under [out](out) directory.

## Project structure

- [model.py](src/model.py) – model classes
- [gen](src/gen) – maze generation algorithms
- [check](src/check) – maze validation
- [solve](src/solve) – solutions package
- [render](src/render) – rendering components
- [main](src/__main__.py) – the example script putting the output to
- [out](out) – the output files directory

## Examples

#### Eller's generation algorithm 100×100
![Eller's generation algorithm](sample_output/Eller.jpg?raw=true "Eller's generation algorithm")

#### Recursive backtracker generation 100×100
![Recursive backtracker generation](sample_output/RecursiveBacktracker.jpg?raw=true "Recursive backtracker maze generation")
