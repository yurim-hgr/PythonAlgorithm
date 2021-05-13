#a = input()
#a, b, c = map(int , input().split())
#n = ord(input())

#n,m = map(int,input().split())
#n = input()
#a=ord(input())

#6093 : [기초-리스트] 이상한 출석 번호 부르기2(py)
n = int(input())      #개수를 입력받아 n에 정수로 저장
a = input().split()  #공백을 기준으로 잘라 a에 순서대로 저장

for i in range(n-1 , -1 , -1) :  #0부터 n-1까지...
  a[i] = int(a[i])       #a에 순서대로 저장되어있는 각 값을 정수로 변환해 다시 저장
  print(a[i], end=' ')
    

#for i in range(n+1, -1 , -1) :  #카운트한 값을 공백을 두고 출력
 #print(a[i], end=' ')
    

# n =
# s = 0
# for i in range(1, n+1) :
#   if i%2==0 :
#     s += i

# print(s)
  


    