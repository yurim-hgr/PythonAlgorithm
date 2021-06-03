
#a = input()
#a, b, c = map(int , input().split())
#n = ord(input())

#n,m = map(int,input().split())
#n = input()
#a=ord(input())


#6098 : [기초-리스트] 성실한 개미(py)
board = []
x = 1
y = 1

# 2차배열 input
for i in range(10):
    temp = list(map(int,input().split()))
    board.append(temp)
    
while True:
    if board[x][y] == 2: #먹이를 발견했을때
        board[x][y] = 9
        break
    elif board[x+1][y] == 1 and board[x][y+1] == 1: #가로막혔을때
        board[x][y] = 9
        break
    board[x][y] = 9
    if board[x][y+1] == 1: # 오른쪽이 벽이면 아래로 1칸
        x += 1
    elif board[x+1][y] == 1: # 아래쪽이 벽이면 오른쪽으로 1칸
        y += 1
    else: y += 1 # 주변에 벽이 없으면 오른쪽으로 1칸

for a in board:
    for b in a:
        print(b,end=' ')
    print()

#for i in range(n+1, -1 , -1) :  #카운트한 값을 공백을 두고 출력
 #print(a[i], end=' ')
    

# n =
# s = 0
# for i in range(1, n+1) :
#   if i%2==0 :
#     s += i

# print(s)
  


    