class var:
    
    def __init__(self, value, delta = 0):
        self.delta = delta
        self.value = value
    
    def getdelta(self):
        return self.delta
    
    def getvalue(self):
        return self.value
        
    def __add__(self, other):
        l = pow(self.getdelta(), 2) + pow(other.getdelta(), 2)
        return variable(self.getvalue() + other.getvalue(), pow(l, 0.5))

    def __sub__(self, other):
        l = pow(self.getdelta(), 2) + pow(other.getdelta(), 2)
        return variable(self.getvalue() -  other.getvalue(), pow(l, 0.5))
        
    def __mul__(self, other):
        l = ((pow(self.getdelta() * other.getvalue(), 2)) + (pow(other.getdelta() * self.getvalue(), 2)))
        return variable(self.getvalue() * other.getvalue(), pow(l, 0.5))
    
    def __div__(self, other):
        a = -1 * pow(other.getvalue(),-2) * self.getvalue()
        b = 1 / other.getvalue()
        l = (pow(self.getdelta() * b, 2) + pow(other.getdelta() * a, 2))
        return variable(self.getvalue() / other.getvalue(), pow(l, 0.5))
        
    def __pow__(self, const):
        l = const * pow(self.getvalue(), const - 1) * self.getdelta()
        return variable(pow(self.getvalue(), const), l)
    
    def __str__(self):
        return str(k.getvalue()) + " , " + str(k.getdelta()) 

        

# Variables (value, delta)
m = var(3, 0.1)
v = var(4, 0.2)

k = var(0.5) * m * (v ** 2)

print(k)
