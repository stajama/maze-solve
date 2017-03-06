def naiverec(matrix,start=None,end=None,been=None,pathlist=None):
  if start in been or matrix[start[0]][start[1]] == 0:
    return False
  elif start == end:
    return pathlist
  if start == None:
    start =(0,matrix[0].index(1))
    end = (len(matrix)-1,matrix[-1].index(1))
    been=[]
    pathlist = [start]
  for coord in [(start[0]-1, start[1]), (start[0]+1,start[1]), (start[0],start[1]+1), (start[0],start[1]-1)]:
    if not matrix[coord[0]][coord[1]]==1 and not coord[0] <0 and not coord[0] >=len(matrix) and not coord[1]<0 and not coord[1]>=len(matrix[0]) and not coord in been:
      newbeen = been +[coord]
    
      newpath = pathlist+[coord]
      nextstep = naiverec(matrix,coord,end,newbeen,newpath)
      if not newpath==False:
        return newpath
  return False
