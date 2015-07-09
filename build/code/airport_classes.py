# -*- coding: utf-8 -*-

class IterRegistry(type):

#    http://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python
    
    def __iter__(cls):
        return iter(cls._registry)
        
class Airport:
    
    __metaclass__ = IterRegistry
    _registry = []

    def __init__(self, x, y, name):
        
        self._registry.append(self)
        
#        longitude (x) and latitude (y), in degrees
        
        self.x = float(x)
        self.y = float(y)
        
        self.name = name
