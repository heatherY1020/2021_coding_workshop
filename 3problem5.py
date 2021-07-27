a,b,c,d,e=map(int,input().rstrip().split())
arr=[a,b,c,d,e]

x=arr[0]+arr[1]+arr[2]+arr[3]+arr[4]
print(x-max(arr), x-min(arr))
