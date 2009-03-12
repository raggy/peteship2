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
        self.dictionary = {"NO": 0}
        
    def load(self, ship):
        
        try:
        
            return self.dictionary[ship.texture_file]
            
        except KeyError:
        
            self.current_texture += 1 # go from 0 to 1, then increment
            
            self.dictionary[ship.texture_file] = self.current_texture
            
            surface = pygame.image.load(os.path.join(ship.texture_file, 'icon.png'))
            
            temp = pygame.image.tostring(surface, "RGBA", 1)
            
            glBindTexture(GL_TEXTURE_2D, self.current_texture)
            
        #                glTexImage2D( GL_TEXTURE_2D, 0, GL_RGBA, surface.get_width(), surface.get_height(), 0,\
        #                              GL_RGBA, GL_UNSIGNED_BYTE, textureData )
        
            gluBuild2DMipmaps(GL_TEXTURE_2D, 3, surface.get_width(), \
                surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, temp)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            
        #                glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
            
            return self.current_texture # tell the ship which integer it needs to use to get rendered, baby

    def unload(self):
        # is this needed? YES!
         glDeleteTextures(range(self.current_texture))