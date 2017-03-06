def naiveimp(matrix):
  def NSEWget(xycoord):
    return [(xycoord[0]-1, xycoord[1]), (xycoord[0]+1,xycoord[1]), (xycoord[0],xycoord[1]+1), (xycoord[0],xycoord[1]-1)]
  start = (0,matrix[matrix.index(1)])
  end = (len(matrix)-1,matrix[-1][matrix.index(1)])
  beenlist=[]
  nodelist=[]
  outlist=[start]
  while not start == end:
    checks=NSEWget(start)
    for coord in checks:
      if not matrix[coord[0]][coord[1]]==1 and not coord[0] <0 and not coord[0] >=len(matrix) and not coord[1]<0 and not coord[1]>=len(matrix[0]) and not coord in beenlist:
        beenlist.append(coord)
        outlist.append(coord)
        start = coord
        isnode = [matrix[des[0]][des[1]] for des in NSEWget(coord)])
        if isnode.count(1)>=3:
          nodelist.append(coord)
        break
      else:
        continue
    if nodelist==[]:
      raise error
    start = nodelist.pop()
    outlist = outlist[:outlist.index(start)+1]
 return outlist
