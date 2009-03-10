#
#  Ships.py
#  Untitled
#
#  Created by Pete Lord on 10/03/2009.
#  Copyright (c) 2009 Coventry University. All rights reserved.
#

import Options, Misc, math, Objects, Angles

class TestShip(Objects.Object):
    
    def __init__(self, parent_e, x, y, z, r):
        Objects.Object.__init__(self, x, y, z, r)
        
        self.internal_name = "TestShip"
        self.display_name = "Testicle"
        self.parent_e = parent_e # reference to entities.
        temp = self.parent_e.graphics.load(self) # get texture from graphics class.
        self.texture = temp[0]
        self.left = -temp[1] * 0.5
        self.right =  + self.left
        self.top =  -temp[2] * 0.5
        self.bottom = + self.top