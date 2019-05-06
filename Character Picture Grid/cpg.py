grid = [['.', '.', '.', '.', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['.', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.']] 

for i in range(len(grid[0])): #dla każdego nowgo rzędu użyj ilości kolumn(6)
    for j in range(len(grid)): #iteracja przez numery wiersza (9)
        print(grid[j][i], end = '')
        j = j + 1
    print('')    