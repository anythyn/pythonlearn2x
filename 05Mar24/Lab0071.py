# object--class>> calculator

class Calc():

    def sumi(self,a,b):
        return a+b

    def subi(self,a,b):
        return a-b

    def mult(self,a,b):
        return a*b

    def devi(self,a,b):
        return a/b

q= Calc()
result = q.sumi(10,4)
print(result)

print(q.devi(10,4))


minu=Calc()
print(minu.subi(11,0)) # direct result printing

print(minu.mult(0.9 ,16))