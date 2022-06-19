#그리디 1이될때까지 p99
#틀린것 기록 
#1. 입력방식 
#2. n 남은 수를 1씩 빼기

n ,k = map(int ,input().split())
sum = 0
while n >= k:
  sum = sum+1;
  if n % k == 0 :
    n = n//k
  else :
    n= n-1

print(n)

while n> 1:
  n = n-1
  sum +=1
print(sum)
