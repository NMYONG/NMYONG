# 전치 행렬 transposed matrix


# i : 행의 좌표, len(arr)
# j : 열의 좌표, lens(arr[0])
arr = [[1,2,3], [4,5,6], [7,8,9]] # 3*3 행렬

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]