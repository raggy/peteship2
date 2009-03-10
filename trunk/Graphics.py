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
        self.current_texture = 0 # 0 used by opengl, but we always increment on load.
        
    def load(self, ship):
        print "dicks"
        self.current_texture += 1 # go from 0 to 1, then increment
        print self.current_texture
        surface = pygame.image.load(os.path.join('Data', ship.internal_name, 'icon.png'))
                
        temp = pygame.image.tostring(surface, "RGBA", 1)
        print "1"
        glBindTexture(GL_TEXTURE_2D, self.current_texture)
        print "2"
    #                glTexImage2D( GL_TEXTURE_2D, 0, GL_RGBA, surface.get_width(), surface.get_height(), 0,\
    #                              GL_RGBA, GL_UNSIGNED_BYTE, textureData )
        gluBuild2DMipmaps(GL_TEXTURE_2D, 3, surface.get_width(), \
            surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, self.current_texture)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    #                glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        return (self.current_texture, surface.width(), surface.height()) # tell the ship which integer it needs to use to get rendered, baby

    def unload(self, ship):
        # is this needed?
        pass
                
    def bind(self, texture):
        glBindTexture(GL_TEXTURE_2D, texture)