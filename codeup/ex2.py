
#a = input()
#a, b, c = map(int , input().split())
#n = ord(input())

#n,m = map(int,input().split())
#n = input()
#a=ord(input())

#6097 : [기초-리스트] 설탕과자 뽑기(py)
h , w = map(int, input().split())
data= []
for i in range(h+1):
  data.append([])
  for j in range(w+1): 
    data[i].append(0)

n = int(input())
for i in range(n):
  l,d,x,y = input().split()
  l = int(l)
  d = int(d)
  x = int(x)
  y = int(y)
  for j in range(l):
    if d== 0 :      
      data[x][y+j]=1
    else :
      data[x+j][y] = 1
      
for i in range(1,h+1):
  for j in range(1, w+1):
    print(data[i][j], end= ' ')
  print()


#for i in range(n+1, -1 , -1) :  #카운트한 값을 공백을 두고 출력
 #print(a[i], end=' ')
    

# n =
# s = 0
# for i in range(1, n+1) :
#   if i%2==0 :
#     s += i

# print(s)
  


    