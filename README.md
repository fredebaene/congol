# ConGoL

This project is a Python implementation of Conway's Game of Life.

## The Game

This project is a Python implementation of Conway's Game of Life. The game 
shows the evolution of the life of cells in a grid. A collection of living 
cells forms a pattern. The cells evolve as follows:

- living cells die if they have less than 2 or more than 3 living neighbors
- living cells keep on living if they have 2 or 3 living neighbors
- dead cells become alive if they have exactly 3 living neighbors.

## Installation

To install the application, create a virtual environment with Python 3.10 or 
higher, and then install the application from GitHub:

```
pip install git+https://github.com/fredebaene/congol.git
```

## Usage

Use the following command to get help on the command line arguments:

```
congol -h
```

To run the evolution of the cells in the **Bunnies** pattern for 30 
generations:

```
congol -p Bunnies -g 30
```

To get the version:

```
congol --version
```