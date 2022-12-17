move_map = {'U':1,'D':-1,'R':1,'L':-1}
x_y_map = {'U':1,'D':1,'R':0,'L':0}

def move_rope(knots,move,tail_positions): 
    for i in range(move[1]):
        knots[0][x_y_map[move[0]]] += move_map[move[0]]
        for x in range(len(knots)-1):
            move_knot(knots[x],knots[x+1])
        tail_positions.add(str(int(knots[9][0])) + ' ' + str(int(knots[9][1])))

def move_knot(previous_knot,current_knot):
    if abs(previous_knot[1] - current_knot[1]) == 2 and abs(previous_knot[0] - current_knot[0]) == 2:
        current_knot[1] += ((previous_knot[1] - current_knot[1])/abs(previous_knot[1] - current_knot[1]))
        current_knot[0] += ((previous_knot[0] - current_knot[0])/abs(previous_knot[0] - current_knot[0]))
        return

    if abs(previous_knot[1] - current_knot[1]) == 2 and abs(previous_knot[0] - current_knot[0]) == 1:
        current_knot[1] += ((previous_knot[1] - current_knot[1])/abs(previous_knot[1] - current_knot[1]))
        current_knot[0] += ((previous_knot[0] - current_knot[0])/abs(previous_knot[0] - current_knot[0]))
        return

    if abs(previous_knot[1] - current_knot[1]) == 1 and abs(previous_knot[0] - current_knot[0]) == 2:
        current_knot[1] += ((previous_knot[1] - current_knot[1])/abs(previous_knot[1] - current_knot[1]))
        current_knot[0] += ((previous_knot[0] - current_knot[0])/abs(previous_knot[0] - current_knot[0]))
        return
    
    if abs(previous_knot[0] - current_knot[0]) == 2:
        current_knot[0] += ((previous_knot[0] - current_knot[0])/abs(previous_knot[0] - current_knot[0]))
        return

    if abs(previous_knot[1] - current_knot[1]) == 2:
        current_knot[1] += ((previous_knot[1] - current_knot[1])/abs(previous_knot[1] - current_knot[1]))
        return

if __name__ == '__main__':

    moves = [[line.strip().split(' ')[0],int(line.strip().split(' ')[1])] for line in open('rope.txt','r').readlines()]
    
    knots = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

    tail_positions = set()

    for move in moves:
        move_rope(knots,move,tail_positions)

    print(len(tail_positions))