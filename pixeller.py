"""
Filename: pixeller.py
Author(s): xTrayambak
Description: Prototype game 1

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