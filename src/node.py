class Node:
  def __init__(self, nodeID: int, coordinate: tuple[int, int]):
    self.nodeID = nodeID
    self.coord = coordinate
    self.x = coordinate[0]
    self.y = coordinate[1]
    
  def __getitem__(self, key):
    return self.coord
