import importlib
from ErrorTypes import *

def get_file(filename, mode):
    """
    Returns the file object with the filename of `filename`.\n
    Takes in `filename` as the name of the file and `mode` as the mode of opening the file.\n\n

    One of the engine's core files.
    """

    if filename == '' or None:
        raise InvalidFileError("Filename cannot be empty or NoneType!")

    try:
        f = open(filename, mode)
        return f
    except FileNotFoundError as e:
        print(f"[Debug]: {e}")
        return None

def append(filename, value):
    """
    Appends `value` to the file assigned to the `filename`. Returns errors.InvalidFileError when an invalid file is provided.
    """
    file = open(filename, 'a')
    file.write(value)