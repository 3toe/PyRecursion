# Write a recursive function that given a number returns the sum of integers from 1 to that number. 
# Example: rSigma(5) = 15 (1+2+3+4+5); rSigma(2.5) = 3 (1+2); rSigma(-1) = 0.

import math

def rSigma(num):
   int = math.floor(num)
   if int < 1:
      return 0
   return int + rSigma(int-1)

print(rSigma(8.3))

# Given num, return the product of ints from 1 up to num. If less than zero, treat as zero. 
# If not an integer, truncate. Experts tell us 0! is 1. rFact(3) = 6 (1*2*3). Also, rFact(6.5) = 720 (1*2*3*4*5*6).

def rFac(num):
   int = math.floor(num)
   if int < 1:
      return 1
   return int * rFac(int-1)

print(rFac(7.3))

