def pixelget(picture, pictureload):
    width = picture.width
    height = picture.height
    matrix = [[]]
    '''Convoluted method to construct an array. Really should use NumPy.'''
    for y in range(height):
        for x in range(width):
            matrix[-1].append(pictureload[x, y])
        if y != height-1:
            matrix.append([])
    return matrix
