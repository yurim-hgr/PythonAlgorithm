

#6094 : [기초-리스트] 이상한 출석 번호 부르기3(py)
n = int(input())      #개수를 입력받아 n에 정수로 저장
a = list(map(int ,input().split()))  #공백을 기준으로 잘라 a에 int 로 변환하고 리스트에 저장 
result = a[0]
for i in a:
  if result > i :
     result = i
print (result)
#a= sorted(a)
#print(a[0])

#a.sort()
#print(a[0])

#print(min(a))

#6093 : [기초-리스트] 이상한 출석 번호 부르기2(py)
n = int(input())      #개수를 입력받아 n에 정수로 저장
a = input().split()  #공백을 기준으로 잘라 a에 순서대로 저장

for i in range(n-1 , -1 , -1) :  #0부터 n-1까지...
  a[i] = int(a[i])       #a에 순서대로 저장되어있는 각 값을 정수로 변환해 다시 저장
  print(a[i], end=' ')
    

#6092 : [기초-리스트] 이상한 출석 번호 부르기1(설명)(py)
n = int(input())      #개수를 입력받아 n에 정수로 저장
a = input().split()  #공백을 기준으로 잘라 a에 순서대로 저장

for i in range(n) :  #0부터 n-1까지...
  a[i] = int(a[i])       #a에 순서대로 저장되어있는 각 값을 정수로 변환해 다시 저장

d = []                     #d라는 이름의 빈 리스트 [ ] 변수를 만듦. 대괄호 기호 [  ] 를 사용한다.
for i in range(24) :  #[0, 0, 0, ... , 0, 0, 0] 과 같이 24개의 정수 값 0을 추가해 넣음
  d.append(0)        #각 값은 d[0], d[1], d[2], ... , d[22], d[23] 으로 값을 읽고 저장할 수 있음.

for i in range(n) :    #번호를 부를 때마다, 그 번호에 대한 카운트 1씩 증가
  d[a[i]] += 1

for i in range(1, 24) :  #카운트한 값을 공백을 두고 출력
  print(d[i], end=' ')

#6091 : [기초-종합] 함께 문제 푸는 날(설명)(py)
a, b, c = map(int , input().split())
d = 1
while d%a!=0 or d%b!=0 or d%c!=0 :
  d += 1
print(d)

#6090 : [기초-종합] 수 나열하기3(py)

a, m, d, n = map(int , input().split())

for i in range(n-1):    
    a = a*m+d
print(a)
  

#6089 : [기초-종합] 수 나열하기2(py)

a, d, n = map(int , input().split())
print(a * d**(n-1))
  
  
#6088 : [기초-종합] 수 나열하기1(py)

a, d, n = map(int , input().split())
print(a + d * (n-1))
  

#6087 : [기초-종합] 3의 배수는 통과(설명)(py)

n = int(input())
s = 0
i = 1
for i in range(1, n+1) :
  
  if(i%3 ==0):
     continue
  else :
      print(i)
      
#210513
#6086 [기초-종합] 거기까지! 이제 그만~(설명)(py) 

n = int(input())
s = 0
i = 1
while True:
   s = s+i
   i = i+1
   if(s>=n):
     break
print(s)
    
  

#6085 : [기초-종합] 그림 파일 저장용량 계산하기(py)

w,h, b= input().split()
w = int(w)
h = int(h)
b = int(b)
a = w*h*b/8/1024/1024
 
print('%.2f'%a , 'MB' , end = ' ')
    
   
#6084 : [기초-종합] 소리 파일 저장용량 계산하기(py)

h,b, c, s= input().split()
h = int(h)
b = int(b)
c = int(c)
s = int(s)
 
print(round(h*b*c*s/8/1024/1024,1) , 'MB' , end = ' ')
    

#6083 : [기초-종합] 빛 섞어 색 만들기(설명)(py)
n,m, p= input().split()
n = int(n)
m = int(m)
p = int(p)
for i in range(0, n) :
  for j in range(0, m) :
    for z in range(0, p) :

      print(i,j,z)
print(n*m*p)


#6082 : [기초-종합] 3 6 9 게임의 왕이 되자(설명)(py)
a = int(input())
for i in range(1, a+1) : 
  if(i%10==3):
    print ('X' , end=' ')
  elif(i%10==6):
    print ('X' , end=' ')
  elif(i%10==9):
    print ('X' , end=' ')
  else :
    print (i , end=' ')

#20210512
#6081  [기초-종합] 16진수 구구단 출력하기(py)
b= int (input(), 16)
for j in range(1, 16) :

    print( '%X'%b ,'*', '%X'%j ,'=' ,'%X'%(b*j) , sep='')

#20210511
#6080  [기초-종합] 주사위 2개 던지기(설명)(py)
n,m = map(int,input().split())
for i in range(1, n+1) :
  for j in range(1, m+1) :

    print(i,j)



  
 
  