n=int(input("satr ra vared konid ? "))
m=int(input("sotoon ra vared konid ? "))
a = [[ 0 for j in range(m)] for i in range(n)]
for i in range(n):
    if i%2==1:
        for j in range(m):
            if j%2==1:
                a[i][j]="🟨"
            if j%2==0:
                a[i][j]="🟩"
    elif i%2==0:
        for j in range(m):
            if j%2==1:
                a[i][j]="🟩"
            if j%2==0:
                a[i][j]="🟨"               
for i in range(n):
    for j in range(m):     
        print(a[i][j],end=" ")
    print()