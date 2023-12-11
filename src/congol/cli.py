"""
This module implements the function required to parse the command line 
arguments specified by the user.
"""


import argparse
from congol import pattern, views, __version__


def get_command_line_args() -> argparse.Namespace:
    """
    This function parses the command line arguments specified by the user and 
    returns a namespace containg these arguments

    Returns:
        argparse.Namespace: the namespace with the command line arguments 
            specified by the user. 
    """
    parser = argparse.ArgumentParser(
        prog="ConGoL",
        description="a Python implementation of Conway's Game of Life"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s v{__version__}"
    )
    parser.add_argument(
        "-p",
        "--pattern",
        default="Blinker",
        choices=[k for k, v in pattern.Pattern.read_patterns_from_toml().items()],
        help="choose a seed to start the game (default: %(default)s)",
    )
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="show all available patterns",
    )
    parser.add_argument(
        "-v",
        "--view",
        choices=views.__all__,
        default="CursesView",
        help="display the life grid in a specific view (default: %(default)s)",
    )
    parser.add_argument(
        "-g",
        "--gen",
        type=int,
        default=10,
        help="the number of generations to display (default: %(default)s)",
    )
    parser.add_argument(
        "-f",
        "--fps",
        type=int,
        default=7,
        help="frames per second (default: %(default)s)",
    )

    return parser.parse_args()