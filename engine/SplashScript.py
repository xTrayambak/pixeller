"""
Filename: SplashScript.py\n
Description: Handles splash data.\n

Author(s): xTrayambak\n
Encoding: UTF-8\n
Spaces: 4 (no tab indentation, using tabs will raise errors)\n
"""

try:
    import files
    import audio
    import random
except Exception as e:
    print(f"[Debug]: {e}")

class Configuration: 
    SPLASHES = open('engine\engine_assets\splashes.txt').readlines()



def RandomSplash():
    """
    Returns a random splash text.
    """
    return random.choice(Configuration.SPLASHES)

print(RandomSplash())