class Wood:
  # Types name - String, area - (int, int), unspecifedProperty(int)
  def __init__(self, name,elasticity, tensileStrength, compressiveStrength):
    self.name = name
    self.elasticity
    E = elasticity
    sigma_t = tensileStrength
    self.tensileStrength = tensileStrength
    sigma_t = tensileStrength
    self.compressiveStrength = compressiveStrength
    sigma_c = compressiveStrength
    
    def get(self, property):
      return getattr(self, property)
    
class Plank(Wood):
  def __init__(self, woodType, width, depth):
    super().__init__(woodType.name, woodType.elasticity, woodType.tensileStrength, woodType.compressiveStrength)
    self.width = width
    self.depth = depth

  pass
