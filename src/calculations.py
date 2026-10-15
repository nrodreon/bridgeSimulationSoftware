import math

def maxTensileForce(woodPlank):
  sigmaT = woodPlank.get(tensileStrength)
  area = woodPlank.get(width) * woodPlank.get(depth)
  maxTensileForce = sigmaT*area
  return maxTensileForce

def maxCompressiveForce(woodPlank):
  
  sigmaC = woodPlank.get(compressiveStrength)

  area = woodPlank.get(width) * woodPlank.get(depth) #primitive incorrect equation
  
  maxCompressiveForce = sigmaT*area
  return maxCompressiveForce


def criticalBucklingLoad(
    elasticity, length):
  k = 0.5
  e = elasticity
  i = 


