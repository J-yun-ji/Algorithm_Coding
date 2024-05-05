def solution(board, h, w):
    answer = 0
    count = 0
    color = board[h][w]
    n = len(board)-1
    if h>0 and board[h-1][w] == color:
        count+=1
    if w>0 and board[h][w-1] == color:
        count+=1
    if h<n and board[h+1][w] == color:
        count+=1
    if w<n and board[h][w+1] == color:
        count+=1
    return count