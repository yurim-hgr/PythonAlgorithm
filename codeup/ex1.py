

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



  
 
  