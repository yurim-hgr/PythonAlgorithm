#6080  [기초-종합] 주사위 2개 던지기(설명)(py)
n,m = map(int,input().split())
#m = int(input())
for i in range(1, n+1) :
  for j in range(1, m+1) :

    print(i,j)


#6081  [기초-종합] 16진수 구구단 출력하기(py)
#n,m = map(int,input().split())
#n = input()
#a=ord(input())
 
b= int (input(), 16)
#print (b)
for j in range(1, 16) :

    print( '%X'%b ,'*', '%X'%j ,'=' ,'%X'%(b*j) , sep='')
