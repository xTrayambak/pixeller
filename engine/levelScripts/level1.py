import json
from json.decoder import JSONDecoder

try:
    import pygame
except ImportError as e:
    print(f'[Debug]: {e}')
except Exception as e:
    print(f'[Debug]: {e}')

class Settings:
    JSON_FILE_DATA = open('engine/level_configuration/level1.json', 'r')

class JSON_STRUCTURE:
    def __init__(self):
        self.d = json.load(Settings.JSON_FILE_DATA)

        ### HUGE STRUCTURE AHEAD! ###
        self.level_name = self.d['level_name']
        self.level_description = self.d['level_description']
        self.difficulty_stars = self.d['difficulty_stars']
        self.doAliensSpawn = self.d['doAliensSpawn']
        self.theme = self.d['theme']
        self.background = self.d['background']
        self.multiplayer = self.d['multiplayer']
        self.enemyAttackChance = self.d['enemyAttackChance']
        self.enemySpeed = self.d['enemySpeed']
        self.capSpriteLimit = self.d['capSpriteLimit']
        self.bossLevel = self.d['bossLevel']
        self.debug_mode = self.d['debug_mode']
        self.framerate_overriden = self.d['framerate_overriden']
        self.framerate_cap = self.d['framerate_cap']
        self.waves = self.d['waves']
        self.maxEnemySpawnsPerRound = self.d['maxEnemySpawnsPerRound']
        self.spawnDelayTimeMax = self.d['spawnDelayTimeMax']
        self.version = self.d['version']

def start(window, run):
    json_struct = JSON_STRUCTURE()

    bg = pygame.image.load(json_struct.background)
    window.queue.append(bg)

    if json_struct.version != window.VERSION:
        pygame.quit()
        print('[Debug]: Outdated version. JSON data failed to load.\n[Traceback]: JSON file was written for '+json_struct.version+' and it was loaded onto this client of version '+window.VERSION+'. Please load a newer/older client to load this file.')
        inp = input('Press any key to continue...')
        while inp == ' ':
            pass
        window.run = False


    if json_struct.framerate_overriden == True:
        window.cap = json_struct.framerate_cap

    print('game start')