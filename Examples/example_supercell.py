"""
Dans_Diffraction Examples
Calculate list of reflections
"""

import sys,os
import numpy as np
import matplotlib.pyplot as plt # Plotting
cf = os.path.dirname(__file__)
sys.path.insert(0,os.path.join(cf,'..'))
import Dans_Diffraction as dif


f = cf+'/../Dans_Diffraction/Structures/Na0.8CoO2_P63mmc.cif'

xtl = dif.Crystal(f)

#P = [[2,-1,0],[1,3,0],[0,0,1]] # 1/7th Supercell
#P = [[-1,3,0],[4,3,0],[0,0,1]] # Square Supercell
P = [[3,0,0],[4,5,0],[0,0,1]] # Stripe Supercell
#P = [[1,3,0],[3,-1,0],[0,0,1]]
#P = [[2,0,0],[0,2,0],[0,0,1]] # Double supercell
#sup = xtl.generate_superstructure(P)

# Set discrete occupancies for average structure
xtl.Atoms.occupancy[2]=0
xtl.Atoms.occupancy[3]=1
xtl.generate_structure()

# Generate the superstructure, repeating the parent/average structure to fill the supercell
sup = xtl.generate_superstructure(P)

# Set the Na ion occupancies
# Stripe Cell
# Na1 6,7 16,17 26,27 36,37 46,47 56,57 66,67 76,77 86,87 96,97 106,107 116,117 126,127 136,137 146,147
# Na2 8,9 18,19 28,29 38,39 48,49 58,59 68,69 78,79 88,89 98,99 108,109 118,119 128,129 138,139 148,149
sup.Structure.occupancy[[6 ,16,26,77,87,107]] = 1 # Na1
sup.Structure.occupancy[[8 ,18,38,28,48,58, 139, 119, 149, 109, 89,79]] = 0 # Na2

# Generate hk0 plane, with overlapping hexagonal superlattice domains
#plt.ion()
print('Running simulation:')
sup.Plot.simulate_hk0(L=0) # (0,0,L) of the parent cell
plt.clim([0, 100])
#plt.ioff()
plt.show()

# Plot the structure in 2D layers
#sup.Plot.plot_layers(show_labels=True)