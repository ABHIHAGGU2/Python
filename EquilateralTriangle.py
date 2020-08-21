import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
n=int(input())
for i in range(n,0,-1):
    for j in range(i):
        print(" ",end="")
    for k in range((n-i+1)*2-1):
        print("*",end="")
    print()
    
