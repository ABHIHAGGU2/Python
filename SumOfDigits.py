import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
a=int(input())
b=0
while a>0:
    b=b+a%10
    a=a//10
print(b)