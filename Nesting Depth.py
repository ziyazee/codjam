#Nesting Depth
for test in range(int(input())):
    n=raw_input()
    tot=0
    string=""
    
    for i in n:
      num=int(i)
      diff=num-tot
      if diff<0:
        string+=")"*abs(diff)+i
      else:
        string+="("*(diff)+i
      tot=tot+diff
    
    print("Case #%s: %s"%(test+1,string+")"*int(string[-1]))) 