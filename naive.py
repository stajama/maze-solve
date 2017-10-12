import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)

def naiverec(matrix, start=None, end=None, been=None, pathlist=None):
    '''Simple recursive function attempting a naive flood-fill of
    maze. This function will likely fail on larger mazes.'''



    if start is None:
        start = (0, matrix[0].index(1))
        end = (len(matrix) - 1, matrix[-1].index(1))
        been = [start]
        pathlist = [start]
    # logging.debug("starting position: (" + str(start))
    if matrix[start[0]][start[1]] == 0:
        return False
    elif start == end:
        return pathlist
    for coord in [(start[0] - 1, start[1]), (start[0] + 1, start[1]),
                  (start[0], start[1] + 1), (start[0], start[1] - 1)]: 
        '''New list of coordinates to check, in order: UP, DOWN, RIGHT, LEFT'''
        if (coord[0] >= 0 and coord[0] <= len(matrix) - 1)  and\
           (coord[1] >= 0 and coord[1] <= len(matrix[0]) - 1):
            # if index within bounds of matrix:
            if coord not in been: 
                # if this step is not regressing to previously explored areas:
                newbeen = been + [coord]
                newpath = pathlist + [coord]
                nextstep = naiverec(matrix, coord, end, newbeen, newpath)
                if nextstep:
                    return nextstep
    return False


def naiveimp(matrix):
    '''Function is an attempt to recreate the brute force
    effectiveness of a recursive naive flood-fill without the danger of
    reaching the maximum recursion depth or overflowing the stack.'''

    logging.debug("Start of naiveimp search, matrix - " + str(matrix))
    def NSEWget(xycoord):
        return [(xycoord[0] - 1, xycoord[1]), (xycoord[0] + 1, xycoord[1]),
                (xycoord[0], xycoord[1] + 1), (xycoord[0], xycoord[1] - 1)]

    def isgoodcoord(coordinate, matr, been):
        '''isgoodcoord checks that the coordinate provided is not off the
            matrix (preventing index errors), is not a wall, and has not been
            previously visited. Can be used to check the former 2 conditions
            only by feeding an empty list into thr third argument.'''
        if coordinate[0] >= 0 and coordinate[0] <= len(matr) - 1 and\
           coordinate[1] >= 0 and coordinate[1] <= len(matr[0]) - 1 and\
           matr[coordinate[0]][coordinate[1]] == 1 and coordinate not in been:
            return True
        return False

    start = (0, matrix[0].index(1))
    end = (len(matrix) - 1, matrix[-1].index(1))

    beenlist = [start]
    nodelist = []
    outlist = [start]
    logging.debug("starting values:\nstart - " + str(start) + "\nend - " + str(end) + "\nnodelist, beenlist, and outlist;" + str(nodelist) + ", " + str(beenlist) + ", " + str(outlist))

    while start != end:

        checks = NSEWget(start)
        logging.debug("Starting at " + str(start) + ", checking coordinates " + str(checks))
        for coord in checks:


            if isgoodcoord(coord, matrix, beenlist):
                logging.debug(str(coord) + " is good...")
                beenlist.append(coord)
                outlist.append(coord)
                start = coord

                isnode = [matrix[des[0]][des[1]] for des in NSEWget(coord)
                          if isgoodcoord(des, matrix, [])]

                '''In this implementation, a node is defined as any junction,
                representing a choice in direction to progress. By building a
                list of these nodes, if a path fails (such as a dead end), the
                code will jump back to the last node visited to continue
                crawling the maze, exploring all possible avenues for the
                exit.'''

                if isnode.count(1) >= 3:
                    nodelist.append(coord)
                logging.debug("End of loop 1 update:\n ")
                break
        else:
            if nodelist == []:
                return False
            start = nodelist.pop()
            outlist = outlist[:outlist.index(start) + 1]
        logging.debug("Sanity Check:\nBeen - " + str(beenlist) + "\nToCheck - " + str(nodelist))
    logging.debug('End of function, result: ' + str(outlist))
    return outlist
