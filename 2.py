#6-9
a6 = [i**2 if i%2!=0  else i**2*(-1) for i in range(1,11) ]


a7 = [2 if i==0 else i+a[i-1] for i in range(0,11)]

a7=[2]
for i in range (1, 11):
    a7.append(i+ a7[i-1])


a8=[i if i%2!=0 else i*3 for i in range(1,12)]

#a9=[1 if i=]

print(a7)
