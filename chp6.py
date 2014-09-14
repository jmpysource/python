import os
import math
import random as r
os.chdir("c:/pysource")

e=math.exp(1.0)
def area(radius):
    temp=math.pi*radius**2
    return temp

def abs(x):
    if x<0:
        return -x
    else:
        return x

    
def compare(x,y):
    if x>y:
        return 1
    elif x==y:
        return 0
    else:
        return -1

def dist(x1,y1,x2,y2):
 
    dx=x2-x1
    dy=y2-y1
    #print 'dx is {0} and dy is {1} '.format(dx,dy)
    dsq=dx**2+dy**2
    #print ' dist squared is ',dsq
    dist=math.sqrt(dsq)
    return dist

def is_divisible(num,divisor):
    return num%divisor==0
  
