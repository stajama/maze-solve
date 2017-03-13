def pixelget(picture, pictureload):
    width = picture.width
    height = picture.height
    matrix = [[]]
    for y in range(height):
        for x in range(width):
            matrix[-1].append(pictureload[x,y])
        if not y == height-1:
            matrix.append([])
    return matrix

