board={"7":' ',"8":' ',"9":' ',
       "4":' ',"5":' ',"6":' ',
       "1":' ',"2":' ',"3":' '}
def TicTacToe(strc):
    print(strc['7']+'|'+ strc['8']+'|'+strc['9'])
    print('-+-+-')
    print(strc['4']+'|'+ strc['5']+'|'+strc['6'])
    print('-+-+-')
    print(strc['1']+'|'+ strc['2']+'|'+strc['3'])
turn='X'
for i in range(9):
    TicTacToe(board)
    print("Enter your move:"+turn)
    move=input()
    if move=='' or move==' ':
        print("TRY ENTERING A VALUE")
        break
    board[str(move)]=turn
    if turn=='X':
        turn='O'
    else:
        turn="X"
    if board[str(move)]=='' or board[str(move)]==' ':
        print("TRY ENTERING A VALUE")
        continue
    



    
