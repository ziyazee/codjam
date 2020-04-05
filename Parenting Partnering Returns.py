#Parenting Partnering Returns
for test in range(int(input())):
    n=int(input())
    arr=[]
    for interval in range(n):
        arr.append([int(x) for x in input().split()]+[interval])
    if not arr:
      print([]) 
    arr.sort(key=lambda x:x[0])
    arr[0].append("C")
    c=[arr[0][0],arr[0][1]]
    j=[0,0]
    flag=True

    for i in range(1,n):
      if arr[i][0]>=c[1]:
        arr[i].append("C")
        c[0]=arr[i][0]
        c[1]=arr[i][1]
      elif arr[i][0]>=j[1]:
        arr[i].append("J")
        j[0]=arr[i][0]
        j[1]=arr[i][1]
      else:
        flag=False
        break
    if flag:
      arr.sort(key=lambda x:x[2])
      st=""
      for z in range(n):
        st+=arr[z][3]
      print("Case #%s: %s"%(test+1,st))
    else:
      print("Case #%s: %s"%(test+1,"IMPOSSIBLE"))