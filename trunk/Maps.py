#
#  Maps.py
#  TurnShip
#
#  Created by Pete Lord on 30/12/2008.
#  Copyright (c) 2008 __MyCompanyName__. All rights reserved.
#
import pygame, os, Options, CollisionGrids
        
class Map():

    def __init__(self, entities, mapfile):
        self.entities = entities # link to entities above it & therefore view.
        
        self.width = mapfile.WIDTH
        self.height = mapfile.HEIGHT 
        self.data = mapfile.DATA
        
        self.collision_data = []
        x = y = 0 # init values
        # scale across the width of the map in 100's, making gridmajors.
        # these fill themselves with grid minors. woo!
        # so maps MUST CURRENTLY BE in 100's.
        while x < self.width - 100:
            while y < self.height - 100:
                self.collision_data.append(CollisionGrids.GridMajor(self, (x, x + 100), (y, y + 100)))
                y += 100
            x += 100