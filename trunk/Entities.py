#
#  Entities.py
#  TurnShip
#
#  Created by Pete Lord on 22/12/2008.
#  Copyright (c) 2008 __MyCompanyName__. All rights reserved.
#
import pygame, os, time, Options, Views, Maps, Graphics, TestShips
   
class EntityHandler():

    def __init__(self, fullscreen, map, player, number_of_players):
        self.player = player
        self.selected = None # selected ship.
        
        self.view = Views.GameView(fullscreen, self)
        
        self.graphics = Graphics.GraphicsHandler()
        
        self.map = Maps.Map(self, map)
        
        self.ships = [TestShips.TestShip(self, 1.0, 1.0, 0.0, 0.0)]
        
    def select(self):
        pass
    
    def deselect(self):
        pass
        
# testing stuff.
        
# end testing.

# main stuff.
        
    def draw(self):
        self.view.draw()
        
    def poll(self):
        for effect in self.effects:
            effect.poll()
            if effect.lifeTime == 0:
                self.effects.remove(effect)