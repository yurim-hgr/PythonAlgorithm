#a = input()
#a, b, c = map(int , input().split())
#n = ord(input())

#n,m = map(int,input().split())
#n = input()
#a=ord(input())

#책(이코테) 그리디 - 더하기 혹은 곱하기 

s = input()
result = 0

for i in range (len(s)) :
  num = int(s[i])
  if num <= 1 or result <= 1:
    result = result + num

  else :
    result = result * num

print(result)

#for i in range(n+1, -1 , -1) :  #카운트한 값을 공백을 두고 출력
 #print(a[i], end=' ')
    

# n =
# s = 0
# for i in range(1, n+1) :
#   if i%2==0 :
#     s += i

# print(s)
  


    