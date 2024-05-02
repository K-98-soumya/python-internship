n=int(input())
i =1
def table(n ,i):
    if(i<=10):
        print(n, 'x',i,' =',8*i)
        table(n,i+1)
        
    return
table(n,i)
