# comment
##comment out
### heading




### Setup

import numpy as np
import matplotlib.pyplot as plt


# lcaa = lift coefficients (and) angles array
# lcaa[x][0] is the angle associated with lcaa[x][1] coefficient
lcaa = np.loadtxt('liftcoeff.txt', ndmin = 2)
# lcaa[x][0] yields angles of attack
# lcaa[x][1] yields lift coefficients
##print(lcaa)




### i) (Sort lcaa Array by Angle)

for a in range(0, len(lcaa) - 1):
   for b in range(a + 1, len(lcaa)):
      if (lcaa[a][0] > lcaa[b][0]):
         temp = lcaa[a][0]
         lcaa[a][0] = lcaa[b][0]
         lcaa[b][0] = temp
         temp = lcaa[a][1]
         lcaa[a][1] = lcaa[b][1]
         lcaa[b][1] = temp
##print(lcaa)




### ii) (Linear Polynomial to Find Force at 11°)
         
Clp = 0.0
# Clp = Coefficient from linear polynomial approximation

for a in range(1, 9):
   if (lcaa[a][0] > 11):
      Clp = lcaa[a - 1][1] + lcaa[a][1] * (11 - lcaa[a - 1][0])




### iii) (Third Order Polynomial to Improve Accuracy of Force Approximation Calculation)

xa = np.zeros((len(lcaa), len(lcaa)))
# xa = Coefficient substitution 2D array

fa = np.zeros(len(lcaa))
# fa = Function value array

# for loop to set the array values of arrays f and x
for i in range(0, len(lcaa)):
   fa[i] = lcaa[i][1]
   for j in range(0, len(lcaa)):
      xa[i][j] = lcaa[i][0]**j

aa = np.linalg.inv(xa) @ fa
# aa = Coefficient array

Ctop = 0.0
# Ctop = Coefficient from third order polynomial approximation

# function to calculate approximant
def y(x):
   total = 0.0
   for z in range(len[aa]):
      total += aa[z]*x**z
   return total

# Calculate Ctop
Ctop = y(11)




### iv) (Calculating Error Between Approximations)

e = 100 * (math.abs(Clp - Ctop) / Ctop)
# e = error




### v) (Formatted Printing of Results)
def format():
   print("The calculated approximation of force at an angle of attack of 11° using linear approximation is " + str(Clp) + "N.")
   print("The calculated approximation of force at an angle of attack of 11° using third order polynomial approximation is " + str(Ctop) + "N.")
   print("The calculated error between the approximations is " + str(e) + "%.")
