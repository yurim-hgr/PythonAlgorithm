
#6081  [기초-종합] 16진수 구구단 출력하기(py)

 
b= int (input(), 16)
#print (b)
for j in range(1, 16) :

    print( '%X'%b ,'*', '%X'%j ,'=' ,'%X'%(b*j) , sep='')
    