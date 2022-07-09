n=int(input())
print('. '*(n-1)+'*'+' .'*(n-1))
for i in range(1,n):
    for j in range(0,n-i-1): print('.',end=' ')
    print('*','. '*(2*i-1), end='')  
    print('*', end='')
    print(' .'*(n-i-1))