from collections import Counter

rows = 'ABCDEFGH'
cols = '12345678'

board = {s:'0' for s in [row+col for row in rows for col in cols]}

def is_goal(state):
    queens = Counter(state.values())
    if queens['Q'] != 8:
        return False    
    return True

def search(start, successors, is_goal): 
    if is_goal(start):
        return start

    queens8 = 0
    explored = set()
    frontier = [start]
    while frontier:
        path = frontier.pop()
        exp = ''.join(list(path.values()))

        if exp not in explored:
            explored.add(exp)
            for state in successors(path):
                frontier.append(state)
        
            if is_goal(path):
                queens8 += 1 
                print(queens8)
                display_board(path)                
                if queens8 == 92:
                    return True             
    
    return False     

def add_squares(state, s):
    start_row = rows.index(s[:1])
    start_col = cols.index(s[1:2])

    for k in state:
        if k != s and state[k] != 2:
            if s[0] == k[0] or s[1] == k[1]:
                state[k] = 'X'
            elif rows.index(k[0]) - cols.index(k[1]) == start_row-start_col:
                state[k] = 'X'
            elif rows.index(k[0]) + cols.index(k[1]) == start_row+start_col:
                state[k] = 'X'            
    return state

def state_sucessors(state):
    #If there are not enough free spaces to place a queen it should return nothing
    values_count = Counter(state.values())
    if values_count['Q'] + values_count['0'] < 8:
        return []

    states = []
    for s in state:
        if state[s] == '0':
            state2 = state.copy()
            state2[s] = 'Q'
            states.append(add_squares(state2, s))

    return states

def display_board(board):
    for r in rows :
        for c in cols :
            print(board[r+c], end=' '), 
        print()
    print()

def solve_queens(puzzle):
    return search(puzzle, state_sucessors, is_goal)

solve_queens(board)