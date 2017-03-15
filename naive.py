'''Simple recursive function attempting a naive flood-fill of 
maze. This function will likely fail on larger mazes.'''

def naiverec(matrix,start=None,end=None,been=None,pathlist=None):
    #print('rec',start)
    if start == None:
        start =(0,matrix[0].index(1))
        end = (len(matrix)-1,matrix[-1].index(1))
        been=[start]
        pathlist = [start]
    if matrix[start[0]][start[1]] == 0:
        return False
    elif start == end:
        return pathlist
    for coord in [(start[0]-1, start[1]), (start[0]+1,start[1]), (start[0],start[1]+1), (start[0],start[1]-1)]:
        if not matrix[coord[0]][coord[1]] == 0 and not coord[0] < 0 and not coord[0] >= len(matrix) and not coord[1] < 0 and not coord[1] >= len(matrix[0]) and not coord in been:
            #print(coord)
            newbeen = been + [coord]    
            newpath = pathlist + [coord]
            nextstep = naiverec(matrix,coord,end,newbeen,newpath)
            if not nextstep == False:
                return nextstep
    return False


def naiveimp(matrix):
    def NSEWget(xycoord):
        return [(xycoord[0]-1,xycoord[1]), (xycoord[0]+1,xycoord[1]), (xycoord[0],xycoord[1]+1), (xycoord[0],xycoord[1]-1)]

    '''isgoodcoord checks that the coordinate provided is not off the 
    matrix (preventing index errors), is not a wall, and has not been 
    previously visited. Can be used to check the former 2 conditions only 
    by feeding an empty list into thr third argument.'''

    def isgoodcoord(coordinate, matr, been):
        if not coordinate[0] < 0 and not coordinate[0] > len(matr)-1 and not coordinate[1] < 0 and not coordinate[1] >= len(matr[0]) and matr[coordinate[0]][coordinate[1]] == 1 and not coordinate in been:
            return True
        return False

    start = (0,matrix[0].index(1))
    end = (len(matrix)-1,matrix[-1].index(1))
    #print(end)
    beenlist=[]
    nodelist=[]
    outlist=[start]
    
    '''Function is an attempt to recreate the brute force 
    effectiveness of a recursive naive flood-fill without the danger of 
    reaching the maximun recursion depth or overflowing the stack. '''
    while not start == end:
        #print('imp',start)
        checks=NSEWget(start)
        for coord in checks:
            #print(coord)
            if isgoodcoord(coord,matrix,beenlist):
                #print(coord)
                #print('buh ya!')
                beenlist.append(coord)
                outlist.append(coord)
                start = coord
                #print('bing', [des for des in NSEWget(coord) if isgoodcoord(des,matrix,[])==True])
                #print(isgoodcoord((10,7),matrix,[]))
                isnode = [matrix[des[0]][des[1]] for des in NSEWget(coord) if isgoodcoord(des,matrix,[]) == True]
                #print('isnode', isnode)
                
                '''In this implementation, a node is defined as any junction, 
                representing a choice in direction to progress. By building a list of 
                these nodes, if a path fails (such as a dead end), the code will jump 
                back to the last node visited to continue crawling the maze, 
                exploring all possible avenues for the exit.'''
                if isnode.count(1)>=3:
                    nodelist.append(coord)
                break
        else:
            if nodelist == []:
                raise ValueError
            start = nodelist.pop()
            outlist = outlist[:outlist.index(start)+1]
    return outlist