import random
from collections import ChainMap
import time

'''In the Pound implementation, nodes need only be connected
latitudinally or longitudinally. By capturing the direction and
distance between nodes, we can count steps between them.'''
'''Went with this idea assuming it would cost less and be more
efficient than a mechanical solution. Can not test this
hypothesis until code is working fully'''


def NSEWget(xycoord):

    return [(xycoord[0] - 1, xycoord[1]), (xycoord[0] + 1, xycoord[1]),
            (xycoord[0], xycoord[1] + 1), (xycoord[0], xycoord[1] - 1)]


def isgoodcoord(coordinate, matr, been):

    if not coordinate[0] < 0 and not coordinate[0] > len(matr) - 1 and not \
           coordinate[1] < 0 and not coordinate[1] >= len(matr[0]) and \
           matr[coordinate[0]][coordinate[1]] == 1 and coordinate not in been:
        return True
    return False


def connectnode(start, matr, direction, nodedic, keylist, coordlist):

    startcoord = nodedic[start]['coordinate']
    directdic = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}
    direction = directdic[direction]
    starters = nodedic[start]['coordinate']

    while True:
        # print('connecting node', start)
        starters = (starters[0] + direction[0]),  (starters[1] + direction[1])
        # print(starters)
        if not isgoodcoord(starters, matr, []):
            return nodedic
        if starters in coordlist:
            key = keylist[coordlist.index(starters)]
            nodedic[key]['connections'][start] = (startcoord,
                        abs((startcoord[0] - starters[0]) + (startcoord[1] -
                        starters[1])))
            nodedic[start]['connections'][key] = (starters,
                        abs((startcoord[0] - starters[0]) + (startcoord[1] -
                        starters[1])))
            return nodedic


def getnode(picture, pictureload):

    def randerz(dicorlist):
        while True:
            x = chr(random.randint(65, 90)) + chr(random.randint(65, 90)) + \
                chr(random.randint(65, 90)) + chr(random.randint(65, 90)) + \
                chr(random.randint(65, 90)) + chr(random.randint(65, 90)) + \
                chr(random.randint(65, 90)) + chr(random.randint(65, 90)) + \
                chr(random.randint(65, 90)) + chr(random.randint(65, 90)) + \
                chr(random.randint(65, 90)) + chr(random.randint(65, 90))
            if x not in dicorlist:
                return x

    width = picture.width
    height = picture.height
    matrix = [[]]
    for y in range(height):
        for x in range(width):
            matrix[-1].append(pictureload[x, y])
        if not y == height - 1:
            matrix.append([])
    c = ChainMap()        # Create root context
    nodedic = c.new_child()
    nodedic['S'] = {'coordinate': (0, matrix[0].index(1)), 'connections': {}}
    nodedic['E'] = {'coordinate': (height - 1, matrix[-1].index(1)),
                    'connections': {}}

    for x in range(1, height - 1):
        for y in range(width):
            # print('try', (x,y))
            if matrix[x][y] == 1:
                isnode = NSEWget((x, y))
                # if (x, y) == (1, 6):
                # print('for 1/6', isnode)
                for item in range(len(isnode)):
                    if isgoodcoord(isnode[item], matrix, []):
                        isnode[item] = 1
                    else:
                        isnode[item] = 0
                if sum(isnode[:2]) >= 1 and sum(isnode[2:]) >= 1:
                    # print('tick')
                    # print('nodeget',nodename,(x,y))
                    # print('add node', (x,y), time.time())
                    nodedic[randerz(nodedic)] = {"coordinate": (x, y),
                                                 'connections': {}}
    keylist = list(nodedic.keys())
    thelist = [nodedic[key]["coordinate"] for key in keylist]
    print('building dic', time.time())
    starttime = time.time()
    for key in nodedic:
        for direction in "NE":
            nodedic = connectnode(key, matrix, direction, nodedic, keylist,
                                  thelist)
        # print(nodedic)
    print('done', time.time()-starttime)
    return nodedic


def getnodeMos(picture, pictureload):
    '''My implementation idea was to only capture nodes that act as
    branching junctions. This reduces the size of the hashtable
    necessary to represent the maze abstractly in memory. The major
    downfall of this implementation is the difficulty of reconstructing
    directions from a map so far abstracted from the original. Was
    considering another targeted flood-fill to just find the paths
    between nodes, but a more efficient solution must exist.'''

    width = picture.width
    height = picture.height
    matrix = [[]]
    for y in range(height):
        for x in range(width):
            matrix[-1].append(pictureload[x, y])
        if not y == height-1:
            matrix.append([])
    nodedic = {'S': {'coordinate': (0, matrix[0].index(1)), 'connections': {}},
               'E': {'coordinate': (height - 1, matrix[-1].index(1)),
               'connections': {}}}

    alpha = 'ABCDFGHIJKLMNOPQRTUVWXYZabcedfghijklmnopqrstuvwxyz0123456789'
    for x in range(1, height - 1):
        for y in range(width):

            if matrix[x][y] == 1:
                # print('try', (x, y))
                isnode = [des for des in NSEWget((x, y)) if
                          isgoodcoord(des, matrix, [])]
                if len(isnode) >= 3:
                    # print('tick')
                    nodedic[alpha[0]] = {"coordinate": (x, y), 'connections': {}}
                    alpha = alpha[1:]
    return nodedic
