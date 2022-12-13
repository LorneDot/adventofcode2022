

if __name__ == '__main__':

    trees = []

    path = 'trees.txt'

    with open(path,'r') as file:
        for line in file.readlines():
            trees.append([int(tree) for tree in list(line.strip())])

    count_of_visible_trees = ((len(trees) * 2) + (len(trees[0]) * 2)) - 4

    print(count_of_visible_trees)

    max_score = 0

    for y in range(1,len(trees)-1):
        for x in range(1,len(trees[0])-1):
            left = trees[y][:x]
            left_count = 0

            for i in reversed(range(len(left))):
                if left[i] >= trees[y][x]:
                    left_count += 1
                    break
                left_count += 1

            right = trees[y][x+1:]
            right_count = 0

            for i in range(len(right)):
                if right[i] >= trees[y][x]:
                    right_count += 1
                    break
                right_count += 1
            
            up = [trees[i][x] for i in range(0,y)]
            up_count = 0

            for i in reversed(range(len(up))):
                if up[i] >= trees[y][x]:
                    up_count += 1
                    break
                up_count += 1
            
            down = [trees[i][x] for i in range(y+1,len(trees))]
            down_count = 0

            for i in range(len(down)):
                if down[i] >= trees[y][x]:
                    down_count += 1
                    break
                down_count += 1

            max_score = max(max_score,left_count*right_count*down_count*up_count)
    print(max_score)