n=int(input())
arr=list(map(int,input().split( )))
p=int(input())
s=set()

k=[]
m=[]
for i in arr:
    s.add(i)

a=0
while(a>=0):
    for i in range(len(arr)-1):
        hj=arr[i]-arr[i+1]
        if(hj<0):
            hj=arr[i+1]-arr[i]
        s.add(hj)
    a=a+1
    if(a==len(arr)):
        break

for i in sorted(s):
    k.append(i)
    
print(k[-p])
