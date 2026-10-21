class BridgeStructure:
  def __init__(self):
    self.nodes = {}
    self.planks = {} 

  def addNode(self, nodeID: int, x: int, y: int):
    self.nodes[nodeID] = Node(nodeID, (x, y))

  def addPlank(self, plankID, sizedPlank):
    self.planks[plankID] = sizedPlank
