

if __name__ == '__main__':

    trees = []

    path = 'trees.txt'

    with open(path,'r') as file:
        for line in file.readlines():
            trees.append([int(tree) for tree in list(line.strip())])

    count_of_visible_trees = ((len(trees) * 2) + (len(trees[0]) * 2)) - 4

    print(count_of_visible_trees)

    for y in range(1,len(trees)-1):
        for x in range(1,len(trees[0])-1):
            left = max(trees[y][:x])
            if trees[y][x] > left:
                count_of_visible_trees += 1
                continue
            right = max(trees[y][x+1:])
            if trees[y][x] > right:
                count_of_visible_trees += 1
                continue
            up = max([trees[i][x] for i in range(0,y)])
            if trees[y][x] > up:
                count_of_visible_trees += 1
                continue
            down = max([trees[i][x] for i in range(y+1,len(trees))])
            if trees[y][x] > down:
                count_of_visible_trees += 1
                continue

    print(count_of_visible_trees)