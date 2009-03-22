#
#  CollisionGrids.py
#  Untitled
#
#  Created by Pete Lord on 13/03/2009.
#  Copyright (c) 2009 Coventry University. All rights reserved.
#

class GridMinor():
    def __init__(self, parent, moveable, cost, x, y):
        self.moveable = moveable
        self.cost = cost
        self.x = x
        self.y = y
        
    def output(self):
        print self.x, self.y
        
class GridMajor():
    def __init__(self, parent, x, y):
        # x & y should be tuples of start and end.
        self.data = []
        
        self.x_start = x[0]
        self.x_end =   x[1]
        self.y_start = y[0]
        self.y_end =   y[1]
        
        for x in range(self.x_end - self.x_start):
        
            self.data.append([])
            
            for y in range(self.y_end - self.y_start):
            
                self.data[-1].append(GridMinor(self, False, 0, self.x_start + x, self.y_start + y))
                self.data[-1][-1].output()
        