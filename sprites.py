"""
Filename: pixeller.py
Author(s): xTrayambak
Description: Prototype game 1 - Sprite class

Dependencies: pygame

Encoding: UTF-8
Spaces: 4
"""
from error import Error

try:
    import pygame
except ImportError as e:
    Error(e)
except Exception as e:
    Error(e)

class Sprite():
    """
    The base of a sprite.
    """

    def __init__(self, pos):
        self.pos = pos
        self.sprData = []

        self.pose = 0

    def draw(self):
        """
        Draw sprite onto the screen.
        """
        pass