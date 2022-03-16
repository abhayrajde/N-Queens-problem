#!/usr/bin/env python
# coding: utf-8

# # N Queens Problem
# 

# In[51]:


# First we will create a board of any dimension (i.e 4X4, 8X8 etc)
global n
n =8
def create_board(n):
    board = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        board.append(temp)
    return(board)

board = create_board(n)


# In[52]:


def validate(board, pos):
    # CHECK SAME ROW - BUT WE HAD TOOK CARE OF THAT
    for i in range(len(board[0])):
        if(board[pos[0]][i] != 0 and i != pos[1]):
            return(False)
    
    # CHECK SAME COLUMN
    for i in range(len(board)):
        if(board[i][pos[1]] != 0 and i != pos[0]):
            return(False)
    
    # INITIALIZING I AND J WILL BE DONE SEPERATELY FOR ALL THE WHILE LOOPS DOWN
    i = pos[0] - 1
    j = pos[1] - 1
     
    # CHECK LEFT-UP
    while(i>=0 and j>=0):
        if(board[i][j] != 0):
            return(False)
        i -= 1
        j -= 1
        
    i = pos[0] + 1
    j = pos[1] - 1
    # CHECK LEFT-DOWN
    while(i<=n-1 and j>=0):
        if(board[i][j] != 0):
            return(False)
        i += 1
        j -= 1
        
    i = pos[0] - 1
    j = pos[1] + 1
    # CHECK RIGHT-UP
    while(i>=0 and j<=n-1):
        if(board[i][j] != 0):
            return(False)
        i -= 1
        j += 1
    
    i = pos[0] + 1
    j = pos[1] + 1
    # CHECK RIGHT-DOWN
    while(i<=n-1 and j<=n-1):
        if(board[i][j] != 0):
            return(False)
        i += 1
        j += 1
    
    return(True)


# In[53]:


def solve(board, col):
    if(col == n):
        return(True)
    
    for i in range(n):
        position = (i, col)
        
        if(validate(board,position)):
            board[position[0]][position[1]] = 1
            
            if(solve(board,col+1)):
                return(True)
            
            board[position[0]][position[1]] = 0
    return(False)


# In[54]:


# DRIVERS CODE
solve(board,0)
for i in range(n):
    print(board[i])
# print(board)


# In[10]:




