def naiverec(matrix, coord = None, done = None, ending = None, returnlist = None):
    if done == None:
        done = []
    if returnlist == None:
        returnlist = []
    if coord == None:
        coord = (0,matrix[0].index(1))
        ending = (len(matrix)-1,matrix[-1].index(1))
    #print(coord)
    #print(done)
    if coord in done:
        #print("in done")
        return False
    else:
        done.append(coord)
    if coord == ending:
        return coord
    if coord[0] >= len(matrix[0]) or coord[0] < 0 or coord[1] >= len(matrix) or coord[0] < 0:
        return False
    if matrix[coord[0]][coord[1]] == 0:
        #print("not path")
        return False
    for checkcord in [(coord[0],coord[1]-1),(coord[0],coord[1]+1),(coord[0]+1,coord[1]),(coord[0]-1,coord[1])]:
        nextcheck = naiverec(matrix,checkcord,done,ending,returnlist)
        if not nextcheck == False:
            returnlist+=[checkcord]
            return returnlist
    return False

