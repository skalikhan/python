t1=(10,20,30,41,50,69,70,80)
t2=()
for x in t1:
    if x %2==0:
        print ("even numbers:",x)
    else:
        print("odd numbers:",x)
            
print(t2)

print("---------------------------------")

t2=(10,20,30,40,50)
print(max(t2))
print(min(t2))
print(sum(t2))
sum=0
for x in t2:
    sum+=x
print(sum)
