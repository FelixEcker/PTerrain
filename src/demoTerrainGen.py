# -*- coding: utf-8 -*-

#######################################
# PTerrain Demo 1.0 by Felix Eckert   #
# Copyright (c) 2020 Felix Eckert     #
# This Project is lincesed under the  #
# 3 Clause BSD License                #
#######################################

import random
import re

def generate():
    size = 32
    sizeSq = size * size
    tiles = ["~", "#"]
    waterCount = 0
    landCount = 0
    map = ""

    for i in range(sizeSq):
        tile = random.randint(0, 1)

        # Increment the aprropriate Counters for the Tile
        if tile == 0:  # Water Counters
            waterCount += 1
        else:  # Land Counters
            landCount += 1

        # Change up the Tile if the tile counter matches the random number
        if waterCount == random.randint(2, size / 2):
            waterCount = 0  # Reset the Water Counter
            tile = 1  # Set the Tile to land

        if landCount == random.randint(4, size - 4):
            landCount = 0  # Reset the Land Counter
            tile = 0  # Set the Tile to Water

        map += tiles[tile]

    return re.sub("(.{" + str(size) + "})", "\\1\n", ''.join(map), 0, re.DOTALL)

print(generate())