import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
b=int(input())
a=65
for i in range(b):
    for j in range(i+1):
        print(chr(a),end="")
    a=a+1
    print()
    