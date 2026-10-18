from . import wood
from . import calculations



# Wood Type Example
# name, 
balsa = Wood("balsa", 4.6*(10**8),2*(10**7),1.2*(10**8) )

# Plank Type Example
# note balsa is using balsa variable from above
# woodTypeObj, length (how much there is), amountLength, width, depth

balsa5mm = Plank(balsa, 5*(10**(-3)), 5*(10**(-3)))
balsa3mm = Plank(balsa, 3*(10**(-3)), 5*(10**(-3)))


