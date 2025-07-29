


def gridChallenge(grid):

    sorted_grid = [''.join(sorted(row)) for row in grid]

    for col in range(len(sorted_grid[0])):
        for row in range(len(sorted_grid[col]) - 1):
            if sorted_grid[row][col] > sorted_grid[row + 1][col]:
                return "NO"
    return "YES"
            
            
if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        print(result)