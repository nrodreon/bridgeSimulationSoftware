from math import sqrt


class WoodType:
  # Types name - String, area - (int, int), unspecifedProperty(int)
  def __init__(
    self, 
    name: str,
    elasticity: float,
    tensileStrength: float,
    compressiveStrength: float
  ):
    self.name = name
    self.elasticity = elasticity
    self.tensileStrength = tensileStrength
    self.compressiveStrength = compressiveStrength
  
class Plank:
  # functionally subtype of WoodType
  def __init__(self, woodType: WoodType, width: float, depth: float):
    self.woodType = woodType
    self.width = width
    self.depth = depth
  
  @property
  def area(self):
    return self.width * self.depth

  def __getattr__(self, name):
    return getattr(self.woodType, name)

class SizedPlank:
  # functionally a subtype of Plank
  def __init__(self, plank: Plank, node1, node2):
    self.plank = plank
    self.startNode = node1
    self.endNode = node2
  @property
  def length(self):
    deltaY = self.startNode.y - self.endNode.y
    deltaX = self.startNode.x - self.endNode.x
    length = sqrt(deltaX**2 + deltaY**2)
    return length


  def __getattr__(self, name):
    return getattr(self.plank, name)
