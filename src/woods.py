import . wood

balsa = Wood("balsa", 4.6*(10**8), 2*(10**7), 1.2*(10**8))
balsa3mm = Plank(balsa, 3*(10**(-3)), 5*(10**(-3)))
balsa5mm = Plank(balsa, 5*(10**(-3)), 5*(10**(-3)))
