import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print("Greatest number is ",a)
elif b>a and b>c:
    print("Greatest number is",b )
else :
    print("The greatest number is ",c)