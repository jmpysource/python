class Odd:
    def __init__ (self,s=[]) :
        self.sequence = s
    def odd(self):
        return self.sequence[::2]
        
odd1 = Odd(['1','ee','wix/',3.9,4])
x=odd1.odd()
print x


def factor_of(factor,range):
     """ returns a list of items in range that are divisable by factor"""
     fact_list=[]
     for i in xrange(range):
             if i%factor != 0 : continue
             fact_list.append(i)
             print i,
     return fact_list 