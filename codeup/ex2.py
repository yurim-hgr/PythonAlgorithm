#a = input()
#a, b, c = map(int , input().split())
#n = ord(input())

#n,m = map(int,input().split())
#n = input()
#a=ord(input())

#백준 그리디 - 동전 0

n, k = map(int ,input().split())
array = []
for i in range (n) :
  a = int(input())
  array.append(a)

#print(array)
array.sort(reverse=True)

count = 0
for coin in array :
  count = count + k // coin 
  k = k % coin 
print(count)

#for i in range(n+1, -1 , -1) :  #카운트한 값을 공백을 두고 출력
 #print(a[i], end=' ')
    

# n =
# s = 0
# for i in range(1, n+1) :
#   if i%2==0 :
#     s += i

# print(s)
  


    