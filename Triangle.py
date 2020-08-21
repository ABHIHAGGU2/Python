import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
a=int(input())
for i in range(a):
    for j in range(i):
        print("*",end="")
    print()
for i in range(a,0,-1):
    for j in range(i):
        print("*",end="")
    print()
