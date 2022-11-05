#6-9
a6 = [i**2 if i%2!=0  else i**2*(-1) for i in range(1,11) ]

a7=[]
a7 = [2 if i==0 else i+a7[i-1] for i in range(11)]


for i in range (1, 11):
    a7.append(i+ a7[i-1])


a8=[i if i%2!=0 else i*3 for i in range(1,12)]

a9=[]

print(a7)
