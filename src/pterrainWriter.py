# -*- coding: utf-8 -*-

#######################################
# PTerrain Writer 1.0 by Felix Eckert #
# Copyright (c) 2020 Felix Eckert     #
# This Project is lincesed under the  #
# 3 Clause BSD License                #
#######################################

def writeTerrainFile(filename, terrain, data, size):
    # Create String to be written
    out = ""

    c = 0
    for i in data[0]:
         out += "{0} {1} ; ".format(i, data[1][c])
         c += 1

    out += "SIZE {} ;\n\n".format(size)

    out += "TERRAIN START\n"
    out += terrain

    # Write variable out to TimeStamped file
    f = open(filename, "x", encoding="utf-8")
    f.write(out)
    f.close()