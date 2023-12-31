"""
This module contains the implementation of the `Pattern` class. A pattern is a 
set of living cells. The seed for an instance of a game is the initial life 
pattern.
"""


from pathlib import Path
from typing import Union


try:
    import tomllib
except ImportError:
    import tomli as tomllib


_PATTERNS_FILE = Path(__file__).parent / "patterns.toml"


class Pattern:
    def __init__(self, name: str, alive_cells: set[tuple[int, int]]) -> None:
        self.name = name
        self.alive_cells = alive_cells

    @classmethod
    def from_toml(
            cls,
            name: str,
            file_path: Union[str, Path] = _PATTERNS_FILE):
        """
        This method returns an instance of `Pattern`. The life pattern used to 
        instantiate an object is read from a TOML file listing one or more 
        life patterns. The `name` argument is used to specify what life 
        pattern in the TOML file must be used.

        Args:
            file_path (Union[str, Path]): file path to the TOML file listing 
                the life patterns.
            name (str): name of the life pattern in the TOML file that must be 
                used to instantiate an object.

        Returns:
            Pattern: an instance of `Pattern`.
        """
        if isinstance(file_path, str): file_path = Path(file_path)
        patterns = cls.read_patterns_from_toml(file_path=file_path)
        return cls(
            name, {tuple(cell) for cell in patterns[name]["alive_cells"]}
        )

    @staticmethod
    def read_patterns_from_toml(
            file_path: Union[str, Path] = _PATTERNS_FILE) -> dict:
        """
        This method reads the life patterns from a TOML file and returns a 
        dictionary with the life patterns.

        Args:
            file_path (Union[str, Path]): file path to the TOML file listing 
                the life patterns.

        Returns:
            dict: a dictionary containing all the life patterns.
        """
        if isinstance(file_path, str): file_path = Path(file_path)
        return tomllib.loads(file_path.read_text(encoding="utf-8"))
    

def instantiate_all_patterns(
        file_path: Union[str, Path] = _PATTERNS_FILE) -> list:
    """
    This function returns a list of `Pattern` instances for every pattern 
    found in a particular TOML file.

    Args:
        file_path (Union[str, Path], optional): file path to the TOML file 
            listing the life patterns.

    Returns:
        list: list with `Pattern` instances.
    """
    patterns = Pattern.read_patterns_from_toml(file_path=file_path)
    return [
        Pattern(name, {tuple(cell) for cell in patterns[name]["alive_cells"]})
        for name in patterns.keys()
    ]