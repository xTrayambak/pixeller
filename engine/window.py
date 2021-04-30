from error import FatalError, Error
import sys

try:
    import pygame
except ImportError as e:
    FatalError(e)
except Exception as e:
    Error(e)

pygame.init()

class WindowConfig:
    WIDTH, HEIGHT = 1280, 720 # is it me or that window kinda.. THI- okay, I'll stop.
    framerate = 120 # fps cap
    VERSION = "1.0PROTO" # this should not be changed in runtime, if it does, well, something went really, REALLY wrong and the interpreter forgot the meaning of constants. RIP Python 3.8 Interpreter
    anti_aliasing = True # in case you've socially isolated yourself from the world including cutting your internet for the past 30 years, here is what this variable refers to in rendering: https://en.wikipedia.org/wiki/Anti-aliasing thank me later! :D

class Window():
    def __init__(self):
        self.state = "menu"
        self.display = pygame.display.set_mode((WindowConfig.WIDTH, WindowConfig.HEIGHT), vsync=1)
        self.clock = pygame.time.Clock()
        self.cap = WindowConfig.framerate
        self.VERSION = WindowConfig.VERSION
        self.run = True
        
        # UI RENDERING QUEUES
        self.queue = {}

        pygame.display.set_caption(f'Pixeller | {int(self.clock.get_fps())} FPS')

    def set_caption(self, caption):
        pygame.display.set_caption(caption)

    def get_fps_color(self):
        """
        Get color of the FPS bar based on the framerate.
        """

        if int(self.clock.get_fps()) > 39:
            return "green"
        elif int(self.clock.get_fps()) < 39:
            return "yellow"
        elif int(self.clock.get_fps()) < 23:
            return "red"
        else:
            return "green"

def main(debug):
    # initialize pygame's modules
    pygame.init()

    # construct our Window class
    win = Window()

    # `win`'s run bool
    run = win.run

    # add objects, as you please, i recommend doing that in seperate files, though.
    win.queue.update({(0, 0, win.clock.get_fps, win.get_fps_color): pygame.font.SysFont(
        name="engine/engine_assets/font/batman_forever/batmfa__.ttf", 
        size=50,
    )})



    #print('capped to '+str(int(win.cap)))

    # main game loop
    while run:
        win.display.fill((255, 255, 255))
        win.set_caption(f'Pixeller | {WindowConfig.VERSION} | {int(win.clock.get_fps())} FPS')

        for pos in win.queue:
            obj = win.queue[pos]

            res = obj

            x, y, text, color = pos

            # text render workaround, I know this looks very weird, but do NOT change it unless you want 70 different things to break
            # god bless this dumb rendering queue...
            if isinstance(obj, pygame.font.Font):
                t = None
                c = "white"
                try:
                    t = text()
                    if debug == True:
                        print(f"Conversion success! ('{t}')")
                except Exception as e:
                    t = text
                    print('err '+str(e))

                try:
                    c = color()
                except:
                    c = color

                # we do NOT want floats, those suck ngl.
                if isinstance(t, float):
                    t = int(t)

                res = obj.render(str(t), WindowConfig.anti_aliasing, c)


            win.display.blit(res, (x, y))
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.flip()
        # cap game to the `win.cap` value, set to 120 as default
        win.clock.tick(win.cap)

    print('[Debug]: Game loop closed. Now quitting...')
    pygame.quit()

if __name__ == "__main__":
    main(True)