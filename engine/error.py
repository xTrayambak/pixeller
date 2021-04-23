"""
Filename: error.py\n
Author(s): xTrayambak\n
Description: Prototype game 1 - Error handling system\n

Dependencies: none\n

Encoding: UTF-8\n
Spaces: 4
"""

def Error(error):
    """
    Function name: Error()\n
    Takes argument(s): `error`\n

    Description: Loops forever and prints error to console. Will pause everything on the main thread, but everything will be back to normal once a key is pressed.
    """

    print(f"[Debug]: {error}")
    close = input('Press any key to continue...')
    while close != '':
        pass

try:
    import sys
except Exception as e:
    Error(e) # then we conclude this Python installation is either A) corrupted due to the user being a smoothbrain or B) some technical mumbo jumbo went wrong, hopefully, this is impossible

def FatalError(error):
    """
    Function name: FatalError()\n
    Takes argument(s): `error`\n

    Description: Loops forever and prints error to console. Shows this as a fatal error, though. Game will be forced to quit, though.
    """

    print(f"[Fatal Error Debug]: {error}")
    close = input('Press any key to exit. Game will not run till errors are dealt with.')
    while close != '':
        pass
    sys.exit()