l1=[10,50,60,555,8000,922,13,1,3]
sum=0
for x in l1:
    sum+=x
print ("sum of l1:",sum)
print("-----------------------")

for x in l1:
    if x%2==0:
        print(x,end=" ")
    else:
        print(x,end=" ")
print("\n---------------------")

print(max(l1))
print(min(l1))

print(len(l1))
