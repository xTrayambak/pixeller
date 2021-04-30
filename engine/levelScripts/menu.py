import threading
import time
import random

try:
    import pygame
except ImportError as e:
    print(f'[Debug]: {e}')
except Exception as e:
    print(f'[Debug]: {e}')

def splashThread(obj, getRandColor, f_splash, aa):
    while True:
        res = obj.render(f_splash, aa, getRandColor())
        time.sleep(0.5)


def start(win):
    # we can start off by adding a title
    win.queue.update({(0, 0): pygame.font.SysFont(
        name="engine/engine_assets/font/batman_forever/batmfa__.ttf", 
        size=50,
    )})