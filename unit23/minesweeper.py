matrix = []
col, row = map(int, input().split())
for i in range(row):
    temp = list(input())
    matrix.append(temp)


def count_mine(r, c):
    if matrix[r][c] == '*':
        return '*'
    mr = [0, 0, 1, -1, -1, -1, 1, 1]
    mc = [1, -1, 0, 0, -1, 1, -1, 1]
    result = 0
    for i in range(8):
        nr = r + mr[i]
        nc = c + mc[i]
        if nr >= 0 and nr < row and nc >= 0 and nc < col and matrix[nr][nc] == '*':
            result += 1

    return result


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(count_mine(i, j), end='')
    print()
