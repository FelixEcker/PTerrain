# -*- coding: utf-8 -*-

#######################################
# PTerrain Parser 1.0 by Felix Eckert #
# Copyright (c) 2020 Felix Eckert     #
# This Project is lincesed under the  #
# 3 Clause BSD License                #
#######################################


terrainDataKeys = []

# usrTerrainDataKeys: A List with the Name of all Data Keys Within the pterrain file
def setup(usrTerrainDataKeys):
    global terrainDataKeys
    terrainDataKeys = usrTerrainDataKeys
    terrainDataKeys.append("size")


# path: The Path to the pterrain file, which needs to be parsed
# This function returns a List of 2 Other Lists, the first one beeing the Data retrieved by the
# terrainDataKeys, the second one is the Actual TerrainMap
def parseTerrainFile(path):
    global terrainDataKeys
    print("Parsing " + path)

    f = open(path, "r").read()
    pterrainSplit = f.split(";")
    cleanedPTerrainSplit = []
    for i in pterrainSplit:
        if not i == pterrainSplit[0]:
            cleanedPTerrainSplit.append(i)

    terrainMap = []
    terrainMapLocation = 0
    terrainStartKey = ""

    terrainData = []

    c = 0
    for i in cleanedPTerrainSplit:
        if "TERRAIN START" in i:
            terrainMapLocation = c
            terrainStartKey = i
            break

        for j in terrainDataKeys:
            if j in i:
                j = i.replace(j, '')
                j = j.replace(' ', '')
                terrainData.append(j)

        c += 1

    for i in range(terrainMapLocation, len(cleanedPTerrainSplit)):
        terrainMap.append(cleanedPTerrainSplit[i])

    terrainMap[0] = terrainMap[0].replace("TERRAIN START", '')
    terrainMap[0] = terrainMap[0].replace("\n", '')

    return [terrainData, terrainMap]


