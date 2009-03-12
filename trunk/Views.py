#
#  Views.py
#  TurnShip
#
#  Created by Pete Lord on 22/12/2008.
#  Copyright (c) 2008 __MyCompanyName__. All rights reserved.
#

import pygame, Options, Objects, Graphics

from OpenGL.GLU import *
from OpenGL.GL import *

class GameView(Objects.Object):

    def __init__(self, fullscreen, parent_e):
    
        Objects.Object.__init__(self, 0.0, 0.0, -100.0, 0.0) # x,y,z,r
        
        self.parent_e = parent_e # reference to parent entities object
        
        if fullscreen == 1:
            flags = pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.OPENGL # comment out the last one for epic software
        else:
            flags = pygame.DOUBLEBUF | pygame.OPENGL # comment out the last one for epic software
            
        self.screen = pygame.display.set_mode((Options.SCREEN_WIDTH, Options.SCREEN_HEIGHT), flags)
        self.resize((Options.SCREEN_WIDTH, Options.SCREEN_HEIGHT))
        glEnable(GL_TEXTURE_2D)
        glShadeModel(GL_SMOOTH)
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
        
    def resize(self, (width, height)):
    
        if height==0:
            height=1
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 1.0 * width/height, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
    def draw(self):

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glLoadIdentity() # clear matrix.
        
        glTranslatef(self.x, self.y, self.z) # translate to camera
        glRotatef(self.r.d(), 0.0, 0.0, 1.0) # rotate to camera.        
        # begin rest of draw
        for ship in self.parent_e.ships:
            glPushMatrix() # always push in!
            
            glTranslatef(ship.x, ship.y, ship.z) # where?
            glRotatef(ship.r.d(), 0.0, 0.0, 1.0) # what rotation?
    #        glColor3f(1.0, 1.0, 1.0) not needed, just here for reference.
            glBindTexture(GL_TEXTURE_2D, ship.texture)
            
            glBegin(GL_QUADS)
            glTexCoord2f(0.0, 0.0); glVertex3f(ship.left,  ship.top,        0.0)    # Bottom Left Of The Texture and Quad
            glTexCoord2f(1.0, 0.0); glVertex3f(ship.right, ship.top,        0.0)    # Bottom Right Of The Texture and Quad
            glTexCoord2f(1.0, 1.0); glVertex3f(ship.right, ship.bottom,     0.0)    # Top Right Of The Texture and Quad
            glTexCoord2f(0.0, 1.0); glVertex3f(ship.left,  ship.bottom,     0.0)    # Top Left Of The Texture and Quad
            glEnd()
            
            glPopMatrix() #always pop out at end!
        
        # END DRAW.

    # NO MOVE VIEW? BECAUSE VIEW IS BASED ON AN OBJECT, SO USES THOSE METHODS!
    # however this is modified to constrain the zoom.
    def mod_z(self, amount):
     
        self.z += amount
        
        if self.z > Options.MAX_ZOOM:
            self.z = Options.MAX_ZOOM

        if self.z < Options.MIN_ZOOM:
            self.z = Options.MIN_ZOOM
        
    def pan_to(self, x, y, z, r, time):
        # move view over time to an area. To be done.
        pass
