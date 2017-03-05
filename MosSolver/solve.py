from PIL import Image;
import time
from pixelmaze import pixelget
from naive import naiverec

# Load Image
print ("Loading Image");
im = Image.open('tiny.png');
xm = im.load()

# Create the maze (and time it) - for many mazes this is more time consuming than solving the maze
print ("Creating Maze");
t0 = time.time()
print(pixelget(im,xm))
matrix = pixelget(im,xm)
t1 = time.time()

print ("Node Count:");
total = t1-t0
print ("Time elapsed:", total, "\n");

print('Trying Naive Recursive Solution')
t0 = time.time()
print(naiverec(matrix))
t1 = time.time()
total = t1-t0
print ("Time elapsed:", total, "\n");
