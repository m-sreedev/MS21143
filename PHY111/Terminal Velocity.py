import math

k = 6*3.14*(7.37697085523173/100)*(3.43/1000)
mg = 9.8/1000
eta = mg/k
print(eta)

l1 = 13.6
l2 = 6.7
t1 = 1.84
t2 = 0.91

dl = 0.1
dt = 0.01

e1 = ((t2*dl)/(2*t1*t2))**2
e2 = ((t1*dl)/(2*t1*t2))**2
e3 = ((l1*dt)/(2*t1*t1))**2
e4 = ((l2*dt)/(2*t2*t2))**2

dvsq = e1 + e2 + e3 + e4

dv = math.sqrt(dvsq)

print(dv)

r = 3.43/1000
v = 7.37697/100

dr = 0.01/1000
ratiosq= (dr/r)**2 + (dv/v)**2

ratio = math.sqrt(ratiosq)

deleta = ratio * eta

print(deleta)