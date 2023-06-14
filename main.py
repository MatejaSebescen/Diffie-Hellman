import math

diffie = []
q = 79

for i in range(1,q):
    isRael = True
    lista = []
    for j in range(1,q):
        #print(i,j,math.pow(i,j) % q)
        lista.append(pow(i,j,q))
    for j in range(1,q):
        if not lista.__contains__(j):
            isRael = False
            break
    #print(lista, isRael)
    if isRael:
        diffie.append(i)
print(diffie)

a = 28
c=0
f=1
Xa = 57
#print("binXa", bin(Xa))
for i in range(2, bin(Xa).__len__()):
    c = c*2
    f = (f*f) % q
    if bin(Xa)[i] == '1':
        print("im in")
        c += 1
        f = (f*a) % q
print(f)

c=0
f=1
Yb = 33
#print("binXa", bin(Xa))
for i in range(2, bin(Xa).__len__()):
    c = c*2
    f = (f*f) % q
    if bin(Xa)[i] == '1':
        print("im in")
        c += 1
        f = (f*Yb) % q
print(f)