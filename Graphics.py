#
#  Graphics.py
#  Peteship
#
#  Created by Pete Lord on 06/03/2009.
#  Copyright (c) 2009 Coventry University. All rights reserved.
#
import os, pygame

from OpenGL.GL import *
from OpenGL.GLU import *


class GraphicsHandler():

    def __init__(self):
    
        self.ships = []
        # VVV to be replaced with recursive stuff to load all images. VVV
        self.ships.append([pygame.image.load(os.path.join('Data', 'icon.png'))])    
        
        self.textures = {"NO":0}
        i = 1
        
        for list in self.ships:
            for surface in list:
                temp = pygame.image.tostring(surface, "RGBA", 1)
                glBindTexture(GL_TEXTURE_2D, i)
            #                glTexImage2D( GL_TEXTURE_2D, 0, GL_RGBA, surface.get_width(), surface.get_height(), 0,\
            #                              GL_RGBA, GL_UNSIGNED_BYTE, textureData )
                gluBuild2DMipmaps(GL_TEXTURE_2D, 3, surface.get_width(), \
                    surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, self.textures[i])
                glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            #                glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
                glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
                i += 1
                
    def bind(self, texture):
        glBindTexture(GL_TEXTURE_2D, texture)