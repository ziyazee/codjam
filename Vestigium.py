#Vestigium
for test in range(int(input())):
    n=int(input())
    arr=[]
    arr=[[int(j) for j in raw_input().split()] for k in range(n)]
    total=(n*(n+1))//2
    rows=0
    cols=0
    trace=0
    for k in range(n):
        hasherR=[0]*(n+1)
        hasherC=[0]*(n+1)
        for m in range(n):
            if (k==m):
                trace+=arr[k][m]
            hasherR[arr[k][m]]+=1
            hasherC[arr[m][k]]+=1
        for row in range(1,n+1):
          if hasherR[row]!=1:
            rows+=1
            break

        
        for col in range(1,n+1):
          if hasherC[col]!=1:
            cols+=1
            break
    print("Case #%s: %s %s %s"%(test+1,trace,rows,cols))