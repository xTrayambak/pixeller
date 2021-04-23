"""
Filename: pixeller.py\n
Author(s): xTrayambak\n
Description: Prototype game 1\n

Dependencies: pygame\n

Encoding: UTF-8\n
Spaces: 4
"""

from engine.error import Error
from engine.error import FatalError

try:
    import pygame
except ImportError as e:
    FatalError(e)
except Exception as e:
    Error(e)

