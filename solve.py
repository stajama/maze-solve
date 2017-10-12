#!/usr/bin/env python3
from PIL import Image
import time
from pixelmaze import pixelget
from naive import naiverec
from naive import naiveimp
from dijkstra import dijkstraRun
from dijkstra import printcoords
from nodeget import getnode
from astar import astarRun
import argparse
from validation import proofTest

parser = argparse.ArgumentParser(description='''Provides coordinate based
                                 solutions to mazes using flood-fill,
                                 Dijkstra, and A* algorithms.''')
parser.add_argument('maze_image', metavar='name of image', type=str)
args = parser.parse_args()
# Load Image
print("Loading Image")
im = Image.open(args.maze_image)
xm = im.load()

'''Create the maze (and time it) - for many mazes this is more time
consuming than solving the maze'''
print("Creating Maze")
t0 = time.time()
print(pixelget(im, xm))
matrix = pixelget(im, xm)
size = len(matrix)
print(size, ' x ', size)
t1 = time.time()

# print("Node Count:");
# print(t1, t0)
total = t1-t0
print("Time elapsed:", total, "\n")

print('Trying Naive Recursive Solution')
t0 = time.time()
nRec = None
try:
    nRec = naiverec(matrix)
    print(nRec)
except RecursionError:
    print("FAILED, maximum recursive depth exceeded")
t1 = time.time()
total = t1-t0
print("Time elapsed:", total, "\n")
if nRec != None:
    proofTest(matrix, nRec)


print('Trying Naive Imperative Solution')
t0 = time.time()
nImp = naiveimp(matrix)
print(nImp)
t1 = time.time()
total = t1-t0
print("Time elapsed:", total, "\n")
if nImp != False:
    proofTest(matrix, nImp)


print("Now creating Maze-Node Map")
t0 = time.time()
matrix, plainMatrix = getnode(im, xm), matrix
# print(matrix)
t1 = time.time()

print("Node Count:", len(matrix))
total = t1-t0
print("Time elapsed:", total, "\n")
matrix
print('Trying Dijkstra')
t0 = time.time()
get = dijkstraRun(matrix)
# print(get)
gets = printcoords(get, matrix)
print(gets, "\n", len(gets))
t1 = time.time()
total = t1-t0
print("Time elapsed:", total, "\n")
proofTest(plainMatrix, gets)

print("A* Shortest Path")
t0 = time.time()
x = astarRun(matrix)
# print(x)
aStarSol = printcoords(x, matrix)
print(aStarSol, '\n', len(printcoords(x, matrix)))
t1 = time.time()
total = t1-t0
print("Time elapsed:", total, "\n")
proofTest(plainMatrix, aStarSol)
