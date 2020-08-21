import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
print("tell me the marks of 5 subjects out of 100")
a=input().split(" ")
print(a)
a=[int(i) for i in a]
print(a)
sum=0
for i in a:
    sum=sum+i
perctage=sum/500*100
print("percentage",perctage)