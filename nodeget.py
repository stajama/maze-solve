

def NSEWget(xycoord):
        return [(xycoord[0]-1,xycoord[1]), (xycoord[0]+1,xycoord[1]), (xycoord[0],xycoord[1]+1), (xycoord[0],xycoord[1]-1)]

def isgoodcoord(coordinate, matr, been):
    if not coordinate[0] < 0 and not coordinate[0] > len(matr)-1 and not coordinate[1] < 0 and not coordinate[1] >= len(matr[0]) and matr[coordinate[0]][coordinate[1]] == 1 and not coordinate in been:
        return True
    return False

'''In the Pound implementation, nodes need only be connected 
latitudinally or longitudinally. By capturing the direction and 
distance between nodes, we can count steps between them.'''
'''Went with this idea assuming it would cost less and be more 
efficient than a mechanical solution. Can not test this 
hypothesis until code is working fully'''
def connectnode(start, matr, direction, nodedic):
    startcoord = nodedic[start]['coordinate']
    directdic = {'N': (-1,0), 'S':(1,0), 'E':(0,1), 'W':(0,-1)}
    direction = directdic[direction]
    starters = startcoord
    while True:
        starters = (starters[0]+direction[0]),(starters[1]+direction[1])
        #print(starters)
        if isgoodcoord(starters,matr,[]) == False:
            return nodedic
        for key in nodedic:
            #print(key, start, starters, startcoord)
            if key == start:
                continue
            if nodedic[key]['coordinate'] == starters:
                #print(nodedic[key]['connections'])
                nodedic[key]['connections'][start] = (startcoord, abs((startcoord[0]-starters[0])+(startcoord[1]-starters[1])))
                nodedic[start]['connections'][key] = (starters, abs((startcoord[0]-starters[0]) + (startcoord[1]-starters[1])))
                return nodedic





def getnode(picture,pictureload):
    width = picture.width
    height = picture.height
    matrix = [[]]
    for y in range(height):
        for x in range(width):
            matrix[-1].append(pictureload[x,y])
        if not y == height-1:
            matrix.append([])
    #print("matrix\n",matrix[0],matrix[1],matrix[2],matrix[3],matrix[4],matrix[5],matrix[6],matrix[7],matrix[8],matrix[9])
    nodedic = {'S':{'coordinate':(0,matrix[0].index(1)), 'connections':{}}, 'E':{'coordinate':(height-1,matrix[-1].index(1)), 'connections':{}}}

    alpha = 'ABCDFGHIJKLMNOPQRTUVWXYZabcedfghijklmnopqrstuvwxyz0123456789'
    '''this bit is hamstrung by any maze bigger than the total number 
    of icons available in the above list. Need to find a larger 
    sample of potential one-character node names or find a 
    different storage solution.''' 
    #print(matrix)
    for x in range(1,height-1):
        for y in range(width):
            #print('try', (x,y))
            if matrix[x][y] == 1:
                isnode = NSEWget((x,y)) 
                #if (x,y) == (1,6):
                #    print('for 1/6', isnode)
                for item in range(len(isnode)):
                    if isgoodcoord(isnode[item],matrix,[]) == True:
                        isnode[item] = 1
                    else:
                        isnode[item] = 0
                if sum(isnode[:2]) >= 1 and sum(isnode[2:]) >= 1:
                    nodename = alpha[0]
                    alpha = alpha[1:]
                    #print('tick')
                    nodedic[nodename] = {"coordinate":(x,y), 'connections':{},}
    for key in nodedic:
        for direction in "NSEW":
            nodedic = connectnode(key, matrix, direction, nodedic) 
        #print(nodedic)      
    return nodedic



'''My implementation idea was to only capture nodes that act as 
branching junctions. This reduces the size of the hashtable 
necessary to represent the maze abstractly in memory. The major 
downfall of this implementation is the difficulty of reconstructing 
directions from a map so far abstracted from the original. Was 
considering another targeted flood-fill to just find the paths 
between nodes, but a more efficient solution must exist.'''
def getnodeMos(picture, pictureload):
    width = picture.width
    height = picture.height
    matrix = [[]]
    for y in range(height):
        for x in range(width):
            matrix[-1].append(pictureload[x,y])
        if not y == height-1:
            matrix.append([])
    #print("matrix\n",matrix[0],matrix[1],matrix[2],matrix[3],matrix[4],matrix[5],matrix[6],matrix[7],matrix[8],matrix[9])
    nodedic = {'S':{'coordinate':(0,matrix[0].index(1)), 'connections':{}}, 'E':{'coordinate':(height-1,matrix[-1].index(1)), 'connections':{}}}

    alpha = 'ABCDFGHIJKLMNOPQRTUVWXYZabcedfghijklmnopqrstuvwxyz0123456789'
    for x in range(1,height-1):
        for y in range(width):
        
            if matrix[x][y] == 1:
                #print('try', (x,y))
                isnode = [des for des in NSEWget((x,y)) if isgoodcoord(des,matrix,[]) == True]
                if len(isnode) >= 3:
                    #print('tick')
                    nodedic[alpha[0]] = {"coordinate":(x,y), 'connections':{},}
                    alpha = alpha[1:]
    return nodedic


