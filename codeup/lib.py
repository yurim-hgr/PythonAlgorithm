#2차원배열 라이브러리
#1
data= []
for i in range(11):
  data.append([])
  for j in range(11):
    data[i].append(0)

for i in range(10):
  a=  input().split()
  for j in range(10):
    data[i+1][j+1]= int(a[j])

for i in range(1, 11):
  for j in range(1, 11):
    print(data[i][j], end= ' ')
  print()

#2
board = []

for i in range(10):
    temp = list(map(int,input().split()))
    board.append(temp)

for a in board:
    for b in a:
        print(b,end=' ')
    print()