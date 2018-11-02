
# z = x + y 
def add(x, y):
    l = pow(x.getdelta(), 2) + pow(y.getdelta(), 2)
    return variable(x.getvalue() + y.getvalue(), pow(l, 0.5))
    
# z = x - y
def sub(x, y):
    l = pow(x.getdelta(), 2) + pow(y.getdelta(), 2)
    return variable(x.getvalue() -  y.getvalue(), pow(l, 0.5))

# z = x * y
def mul(x, y):
    l = ((pow(x.getdelta()* y.getvalue(), 2)) + (pow(y.getdelta() * x.getvalue(), 2)))
    return variable(x.getvalue() * y.getvalue(), pow(l, 0.5))

# z = x / y
def div(x, y):
    a = -1 * pow(y.getvalue(),-2) * x.getvalue()
    b = 1 / y.getvalue()
    
    l = (pow(x.getdelta() * b, 2) + pow(y.getdelta() * a, 2))
    return variable(x.getvalue() / y.getvalue(), pow(l, 0.5))
    
    return variable(x.getvalue() / y.getvalue(), pow(l, 0.5))


def power_c(x, c):
    l = c * pow(x.getvalue(), c - 1) * x.getdelta()
    return variable(pow(x.getvalue(), c), l)

class variable:
    
    def __init__(self, value, delta):
        self.delta = delta
        self.value = value
    
    def getdelta(self):
        return self.delta
    
    def getvalue(self):
        return self.value

# Variables (value, delta)
m = variable(3, 0.1)
v = variable(4, 0.2)

# 1/2 mv^2

c = mul(m, variable(0.5, 0))
d = power_c(v, 2)
t = mul(c, d)

print(t.getvalue())
print(t.getdelta())
