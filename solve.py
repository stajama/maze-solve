from PIL import Image;
import time
from pixelmaze import pixelget
from naive import naiverec
from naive import naiveimp
from dijkstra import dijkstraRun
from dijkstra import printcoords
from nodeget import getnode

# Load Image
print("Loading Image")
im = Image.open('tiny.png')
xm = im.load()

#Create the maze (and time it) - for many mazes this is more time consuming than solving the maze
print ("Creating Maze")
t0 = time.time()
print(pixelget(im,xm))
matrix = pixelget(im,xm)
t1 = time.time()

#print("Node Count:");
print(t1, t0)
total = t1-t0
print("Time elapsed:", total, "\n")

print('Trying Naive Recursive Solution')
t0 = time.time()
print(naiverec(matrix))
t1 = time.time()
total = t1-t0
print("Time elapsed:", total, "\n")

print('Trying Naive Imperative Solution')
t0 = time.time()
print(naiverec(matrix))
t1 = time.time()
total = t1-t0
print("Time elapsed:", total, "\n")


print ("Now creating Maze-Node Map")
t0 = time.time()
matrix = getnode(im,xm)
print(matrix)
t1 = time.time()

print("Node Count:", len(matrix));
total = t1-t0
print("Time elapsed:", total, "\n")

print('Trying Dijkstra')
t0 = time.time()
get = dijkstraRun(matrix)
print(get)
gets = printcoords(get,matrix)
print(gets)
t1 = time.time()
total = t1-t0
print("Time elapsed:", total, "\n")
