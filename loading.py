class Practice:
    def __init__(self,a,b):
        self.e=a
        self.l=b
    def fun(self):
        c=self.e+self.l
        print(c)
class Dem(Practice):
    pass
ob=Dem(5,2)
ob.fun()