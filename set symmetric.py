n=int(input())
roll1=map(int,input().split())
m=int(input())
roll2=map(int,input().split())
s=set(roll1)
s2=s.difference(roll2)
print(len(s2))