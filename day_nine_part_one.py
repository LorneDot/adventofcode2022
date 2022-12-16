move_map = {'U':1,'D':-1,'R':1,'L':-1}
x_y_map = {'U':1,'D':1,'R':0,'L':0}

def move_rope(head_position,tail_position,move,tail_positions): 
    for i in range(move[1]):
        head_position[x_y_map[move[0]]] += move_map[move[0]]
        print("head "+ str(head_position))
        if abs(head_position[0] - tail_position[0]) > 1:
            tail_position[0] += ((head_position[0] - tail_position[0])/abs(head_position[0] - tail_position[0]))
            tail_positions.append(str(str(int(tail_position[0]))) + " " + str(int(tail_position[1])))
            continue
        if abs(head_position[1] - tail_position[1]) > 1:
            tail_position[1] += ((head_position[1] - tail_position[1])/abs(head_position[1] - tail_position[1]))
            tail_positions.append(str(str(int(tail_position[0]))) + " " + str(int(tail_position[1])))
            continue
        
        print("tail "+ str(str(int(tail_position[0]))) + " " + str(int(tail_position[1])))

if __name__ == '__main__':

    moves = [[line.strip().split(' ')[0],int(line.strip().split(' ')[1])] for line in open('rope.txt','r').readlines()]
    
    head_position = [0,0]
    tail_position = [0,0]
    tail_positions = []

    for move in moves:
        move_rope(
            head_position,
            tail_position,
            move,
            tail_positions
            )

    print(len(set(tail_positions)))