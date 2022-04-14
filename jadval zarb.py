n=int(input("satr ra vared konid ? "))
m=int(input("sotoon ra vared konid ? "))
x = [[ 0 for j in range(m+1)] for i in range(n+1)]
for i in range(n+1):
    for j in range(m+1):
        x[0][0]="x"
        if i==0 or j==0:
            x[0][j]=j
            x[i][0]=i
        else :
            x[i][j]=i*j       
for i in range(n+1):
    for j in range(m+1):   
          print(x[i][j],end="\t")
    print()