import math

def maxTensileForce(woodPlank):
  sigmaT = woodPlank.get(tensileStrength)
  area = woodPlank.get(width) * woodPlank.get(depth)
  maxTensileForce = sigmaT*area
  return maxTensileForce

def maxCompressiveForce(woodPlank):
  
  sigmaC = woodPlank.get(compressiveStrength)

  area = woodPlank.get(width) * woodPlank.get(depth) #primitive incorrect equation
  
  maxCompressiveForce = sigmaC*area
  return maxCompressiveForce


def criticalBucklingLoad(elasticity, length, width, depth):
  k = 0.5
  e = elasticity
  x = (width, depth)
  minDim = min(x)
  maxDim = max(x)
  inertia = (minDim**3)*maxDim/12
  criticalLoad = ((math.pi ** 2) * elasticity * inertia )/ ((k*length)**2)
  return criticalLoad


