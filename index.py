matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

size = len(matrix) 
print(f"size: {size}x{size}")

result = [[0] * size for _ in range(size)] #define and fill with 0

#pos
top = 0
bottom = size - 1
left = 0
right = size - 1
index = 1

print(f"positions: top {top}, bottom {bottom}, left {left}, right {right}, index {index}")

while top <= bottom and left <= right:

    for i in range(left, right + 1): #left to right
        result[top][i] = index #current index
        index += 1 #index + 1
    top += 1 #move top down
    print("right >", result)
    print(f"\npositions: top {top}, bottom {bottom}, left {left}, right {right}, index {index}")


    for i in range(top, bottom + 1): #top to bottom
        result[i][right] = index #current index
        index += 1 #index + 1
    right -= 1 #move right left
    print("down v", result)
    print(f"\npositions: top {top}, bottom {bottom}, left {left}, right {right}, index {index}")
    

    for i in range(right, left - 1, -1): #right to left
        result[bottom][i] = index #current index
        index += 1 #index + 1
    bottom -= 1 #move bottom up
    print("left <", result)
    print(f"\npositions: top {top}, bottom {bottom}, left {left}, right {right}, index {index}")


    for i in range(bottom, top - 1, -1): # bottom to top
        result[i][left] = index # current index
        index += 1 #index + 1
    left += 1 #move left right
    print("top ^", result)
    print(f"\npositions: top {top}, bottom {bottom}, left {left}, right {right}, index {index}")

print("result")
print(result)
