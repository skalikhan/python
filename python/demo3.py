l1=[10,1,3,9,7,20,30,40,50]
l2=[]
l3=[]
for x in l1:
    if x%2==0:
        l2.append(x)
    else:
        l3.append(x)
            
print(l2)
print(l3)
print("----------------------------")

man=[10,20,30,40,50,60,70,80,90]
women=[10,20,60,80,30,50,70,90]
common=[]
for x in man:
    if x in women:
        common.append(x)
print(common)
print("=====================")

for x in man:
    if x not in women:
        common.append(x)
print(common)

        
