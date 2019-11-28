b1=[20,60,50,40,80,90,75,65,92,95]
print("even no.s=",[x for x in b1 if x%2==0])
print("odd no.s=",[ y for y in b1 if y%2==1])
print("sum of all no.s =",sum(b1))
print("max no.=",max(b1))
print("min no.s=",min(b1))
print("length=",len(b1))
print("______________________________________")
x=[[0]*5]
print(x)
print("______________________________________")
x=[[0]*5]*2
print(x)
y=[[[0]*3]]
print(y)

print("--------------------------------------")

she_friend=['ravi','raju','krishna','mahesh','vamsi']
my_friend=['krishna','vamsi','ali','mahesh']
common_friend=[]
for x in she_friend:
    if x in my_friend:
        common_friend.append(x)
print(common_friend)
print("=========================================")

common_friend=[x for x in she_friend if x in my_friend]
print(common_friend)
print(type(common_friend))
print("=======================================")
red_colour=['apple','rose','house','flower','sweet','frouit','black','white']
colour=["black",'white','rose','flower','pink','ddd']
a=[x for x in red_colour if x in colour]
print(a)



