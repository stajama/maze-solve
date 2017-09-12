import math


def dijkstraRun(nodedic):
    '''Dijkstra's solution places each available node in a priority queue,
       organized in order of shortest distance traveled. The queue here is
       implemented and a Python list rather than a more sophisticated heap.'''

    start = 'S'
    end = 'E'
    checknodes = {keys: (math.inf, '') for keys in nodedic if keys != start
                  and keys != end}
    # print('tick')
    priorityQueue = []
    for item in checknodes:
        # print(item)
        priorityQueue.append(item)
    priorityQueue = ['S'] + priorityQueue + ['E']
    endlist = []
    checknodes[start] = (0, '')
    checknodes[end] = (math.inf, '')
    # print(checknodes)
    # print('tick')
    while not priorityQueue[0] == end:
        #print('pri cue',priorityQueue)
        check = priorityQueue[0]
        priorityQueue = priorityQueue[1:]
        for connectednode in nodedic[check]['connections']:
            # print('connectednode', connectednode)
            # print('tick')
            if connectednode == 'S':
                continue
            elif nodedic[check]['connections'][connectednode][1] + \
                 checknodes[check][0] < checknodes[connectednode][0]:
                # print('tick2')
                checknodes[connectednode] = (nodedic[check]['connections'][connectednode][1]
                                            + checknodes[check][0], check)
                if not len(priorityQueue) <= 1:
                    priorityQueue = priorityQueue[:priorityQueue.index(connectednode)] + \
                                  priorityQueue[priorityQueue.index(connectednode)
                                  + 1:]
                else:
                    priorityQueue = priorityQueue[-1]
                for pos in range(len(priorityQueue)):
                    # print('pos numb',len(priorityQueue))
                    # print(pos, priorityQueue[pos])
                    # print('in priority cue', priorityQueue)
                    if checknodes[priorityQueue[pos]][0] > \
                       checknodes[connectednode][0]:
                        # print('tick')
                        priorityQueue = priorityQueue[:pos] + [connectednode] + \
                                      priorityQueue[pos:]
                        break
        # print('tick')
        # print(priorityQueue)
        # print(checknodes)
        # print([(key, checknodes[key]) for key in priorityQueue])
        endlist.append(check)
        # print(endlist, check)
    outlist = [endlist[-1]]
    check = outlist[0]
    # print('check', check)
    while not check == 'S':
        # print('outlist is a ', type(outlist))
        # print('HELP',checknodes[check][1])
        outlist = [checknodes[check][1]] + outlist
        #print('Help2',outlist)

        check = outlist[0]
        # print(outlist, check)
    outlist.append("E")
    return outlist


def printcoords(dirlist,nodedic):
    '''printcoords() is a simple solution to reverse the output of the main
       dijkstra() function. Provided the list of nodes traversed in reverse
       from dijkstra(), this function reverses the directions and outputs
       them in readable coordinates.'''

    outlist = []
    for item in range(len(dirlist)):
        outlist.append(nodedic[dirlist[item]]['coordinate'])
        if not item == len(dirlist)-1:
            nextnode = nodedic[dirlist[item+1]]['coordinate']
            current = outlist[-1]
            if nextnode[0] == current[0]:
                if abs(current[1]-nextnode[1]) > 1:
                    if current[1] > nextnode[1]:
                        turn = -1
                    else:
                        turn = 1
                    for step in range(min(current[1], nextnode[1]),
                                      max(current[1], nextnode[1]), turn):
                        #print(current[0])
                        if step == current[1]:
                            continue
                        outlist.append((current[0], step))
            elif nextnode[1] == current[1]:
                if abs(current[0]-nextnode[0]) > 1:
                    if current[0] > nextnode[0]:
                        turn = -1
                    else:
                        turn = 1
                    for step in range(min(current[0], nextnode[0]),
                                      max(current[0], nextnode[0]), turn):
                        if step == current[0]:
                            continue
                        outlist.append((step, current[1]))
    return outlist
