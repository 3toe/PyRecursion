# Write rFib(num). Recursively compute and return numth Fibonacci value. 
# As earlier, treat first two (num = 0, num = 1) Fibonacci vals as 0 and 1.

import math

def rFib(num):
   if num <= 0:
      return 0
   int = math.floor(num)
   if int <= 1:
      return int
   return rFib(int-1)+rFib(int-2)

print(rFib(4))

# Write function rTrib(num) to mimic Fibonacci, adding previous three values instead of two.

def rTrib(num):
   num = math.floor(num)
   if num < 0:
      return 0
   if num in {0,1,2}:   
      return num
   return rTrib(num-1) + rTrib(num-2) + rTrib(num-3)

print(rTrib(5))

# Ackermann function:

def ackermann(m,n):
   if m==0:
      return n+1
   elif m>0 and n==0:
      return ackermann(m-1,1)
   elif m>0 and n>0:
      return ackermann(m-1,ackermann(m,n-1))

print(ackermann(2,2))

# Zibonacci function:

def Zib(n):
   if n == 0 or n == 1:
      return 1
   if n == 2:
      return 2
   if n%2 == 0:
      return Zib(n/2) + Zib(n/2 + 1) + 1
   else:
      return Zib((n-1)/2) + Zib((n-1)/2 - 1) + 1

print(Zib(10))
print(Zib(100))
print(Zib(2467))

def DeZibber(m):
   int = m
   while int>0:
      if Zib(int) == m:
         return int
      int-=1
   return None

print(DeZibber(3186))
print(DeZibber(3183))

