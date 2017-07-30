#con cuu

A = [5,7,300,90,24,50,75]

print ("Hello, my name is Cau and these are my sheep sizes")
print (A)
print (" ")
print ("Now my biggest sheep has size 300 let's shear it")
print ("After shearing, here is my flock")
A[A.index (max (A))] = 8
print (A)
print (" ")
for i in range (1,4):
    print ("MONTH", i )
    print ("One month has passed, now here is my flock")
    for a in range (len(A)):
        A[a] = A[a] + 50
    print (A)

    if i!=3 :
        print ("Now my biggest sheep has size 300 let's shear it")
        print ("After shearing, here is my flock")
        A[A.index (max (A))] = 8
        print (A)
        print (" ")
    else :
            break
a = 0
x = 0
for i in range (0,7):
    x = x + A[a]
    a = a + 1

#print (x)

x = x - len(A)*8

print ("My flock has size in total",)

T = x * 2 + len(A)*100
print ("I would get ", x, "* 2$ +",len(A),"*20 = ", T,"$")

