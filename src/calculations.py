import math
#all functions support subTypes of indicated type
def maxTensileForce(plank: Plank):
  sigmaT = plank.tensileStrength
  area = plank.area
  maxTensileForce = sigmaT*area
  return maxTensileForce


def maxCompressiveForce(plank: Plank):
  sigmaC = plank.compressiveStrength
  area = plank.area
  maxCompressiveForce = sigmaC * area
  return maxCompressiveForce


def criticalBucklingLoad(sizedPlank: SizedPlank):
  k = 0.5
  e = sizedPlank.elasticity
  width = sizedPlank.width
  depth = sizedPlank.depth
  minDim = min(width, depth)
  maxDim = max(width, depth)
  length = sizedPlank.length
  inertia = (minDim**3)*maxDim/12

  criticalLoad = ((math.pi ** 2) * e * inertia )/ ((k*length)**2)
  return criticalLoad


