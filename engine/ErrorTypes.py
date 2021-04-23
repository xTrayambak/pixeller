import files as IO
import error as Errors

class FatalException():
    def __init__(self, msg):
        IO.append(filename='debug.log',
        value=f'[{self}]: {msg} | Game terminated.')
        Errors.FatalError(msg)

class NormalException():
    def __init__(self, msg):
        IO.append(filename='debug.log',
        value=f'[{self}]: {msg}')
        Errors.Error(msg)

class InvalidFileError(FatalException):
    """
    Occurs when an Invalid Filename is provided (eg. NoneType)

    Subclass of class FatalException
    """
    def __init__(self, msg):
        super().__init__(msg)

class RenderingError(NormalException):
    """
    Occurs when a rendering-related error occurs.

    Subclass of class NormalException
    """
    def __init__(self, msg):
        super().__init__(msg)

class SpriteLimitExceededError(FatalException):
    """
    Occurs when the sprite limit of 10000 is reached. At that point, the game will be unplayable as rendering 1 frame will take minutes of time. It's better to just crash.

    Subclass of class FatalException
    """
    def __init__(self, msg):
        super().__init__(msg)