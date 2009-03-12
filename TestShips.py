#
#  Ships.py
#  Untitled
#
#  Created by Pete Lord on 10/03/2009.
#  Copyright (c) 2009 Coventry University. All rights reserved.
#

import Options, Misc, math, Objects, Angles, os.path

class TestShip(Objects.Object):
    
    def __init__(self, parent_e, x, y, z, r):
        Objects.Object.__init__(self, x, y, z, r)
        
        self.internal_name = "TestShip"
        self.display_name = "Testicle"
        self.parent_e = parent_e # reference to entities.
        
        self.texture_file = os.path.join('Data', self.internal_name)
        
        self.texture = self.parent_e.graphics.load(self) # request texture from graphics class.
        self.left =  -3.2
        self.right =  3.2
        self.top =   -3.2
        self.bottom = 3.2
        print self.internal_name, self.texture, self.left, self.right, self.top, self.bottom