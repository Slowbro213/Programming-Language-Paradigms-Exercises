def Image_Smooth(image):
    rows, cols = len(image), len(image[0])
    smoothed_image = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            smoothed_image[i][j] = smoothen(image, i, j)

    return smoothed_image


def smoothen(image, x, y):
    rows, cols = len(image), len(image[0])
    sum, count = 0, 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            nx, ny = x + i, y + j
            if 0 <= nx < rows and 0 <= ny < cols:
                sum += image[nx][ny]
                count += 1

    return int(sum / count)

image = [[100,200,100],[200,50,200],[100,200,100]]
print(Image_Smooth(image))

image = [[1,2],[3,4]]
print(Image_Smooth(image))