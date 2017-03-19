# About
This is a practice project, intended to test several maze solving algorithms on a single maze. Inspired by Mike Pound's Computerphile video series on Shortest-Path algorithms, the script applies 4 different algorithms to a single maze. The list of algorithms is available below.

# Getting Started
For the time being, maze selection must be hard coded into solve.py. Once maze is selected, run solve.py in CLI. The script will print the maze solution for all algorithms attempted or False for those that fail, along with the calculation time spent on each algorithim. 

# Usage
The script is designed to solve mazes feed in as a uncompressed pixel image, with a single entry point at the top and a single exit point at the bottom. Mazes may be simply-connected or more complex. The included example mazes were generated with Daedalus. 

# Metholody
The first algorithim used is a brute-force recursive flood fill search for the end. If it does not crash due to maximun recursion depth, it should provide a path to the exit. The second algorithim is a similar brute-force solution, intended to recreate the recursive search with interative code that should theoritically not fail to find a path if one exists. The third solution is a simple implementation of Dijkstra Shortest Path, measuring steps necessary to provide the shortest path to the exit. The forth solution is an simple A-Star implementation, using both the steps measurement from Dijkstra and an abstract Euclidian distance from the end to find the shortest path with priority placed on heading directionally toward the goal when possible.
