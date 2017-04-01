from PIL import Image;
import time
from pixelmaze import pixelget
from naive import naiverec
from naive import naiveimp
from dijkstra import dijkstraRun
from dijkstra import printcoords
from nodeget import getnode
from astar import astarRun 
import argparse

parser = argparse.ArgumentParser(description="Provides coordinate based solutions to mazes using flood-fill, Dijkstra, and A* algorithms.")
parser.add_argument('maze_image', metavar = 'name of image', type=str, )
args = parser.parse_args()
# Load Image
print("Loading Image")
im = Image.open(args.maze_image)
xm = im.load()

#Create the maze (and time it) - for many mazes this is more time consuming than solving the maze
print ("Creating Maze")
t0 = time.time()
print(pixelget(im,xm))
matrix = pixelget(im,xm)
size = len(matrix)
print(size,' x ',size)
t1 = time.time()

#print("Node Count:");
#print(t1, t0)
total = t1-t0
print("Time elapsed:", total, "\n")

print('Trying Naive Recursive Solution')
t0 = time.time()
try:
    print(naiverec(matrix))
except:
    print("FAILED")
t1 = time.time()
total = t1-t0
print("Time elapsed:", total, "\n")

print('Trying Naive Imperative Solution')
t0 = time.time()
try:
    print(naiveimp(matrix))
except:
    print("FAILED")
t1 = time.time()
total = t1-t0
print("Time elapsed:", total, "\n")


print ("Now creating Maze-Node Map")
t0 = time.time()
matrix = getnode(im,xm)
#print(matrix)
t1 = time.time()

print("Node Count:", len(matrix));
total = t1-t0
print("Time elapsed:", total, "\n")
matrix
print('Trying Dijkstra')
t0 = time.time()
get = dijkstraRun(matrix)
#print(get)
gets = printcoords(get,matrix)
print(gets,"\n",len(gets))
t1 = time.time()
total = t1-t0
print("Time elapsed:", total, "\n")

print("NEW")
t0 = time.time()
x = astarRun(matrix)
#print(x)
print(printcoords(x, matrix),'\n',len(printcoords(x, matrix)))
t1 = time.time()
total = t1-t0
print("Time elapsed:", total, "\n")
