a=[10,20,30,40,50,60,70,80]
b=[20,30,50,80]
a.extend(b)
print(a)
print("------------------------")
c=('apple','ball','cat')
d=[]
d.extend(c)
print(d)

vovel=['a','e','i','u']
vovel.insert(3,'o')
print(vovel)
num=[20,30,40,50,60,70,80]
num.insert(4,999)
print(num)
print("======================")
mixed=[{1,2,3},[4,5,6]]
tup=(7,8,9)
mixed.insert(2,tup)
print(mixed)

print("=======================")
l1=[10,20,30,40,50,60]
l1.remove(60)
print(l1)
l1.remove(30)
print(l1)



