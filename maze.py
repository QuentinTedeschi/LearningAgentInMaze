# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 03:25:21 2021

@author: Quentin Tedeschi
"""
from random import randrange, random

## Functions
def printMaze(maze):
	for i in range(0, len(maze)):
		for j in range(0, len(maze[0])):
				print(str(maze[i][j]), end=" ")
		print('\n')

# Find number of surrounding cells
def surroundingCells(maze, rand_wall):
	surr_cells = 0
	if (maze[rand_wall[0]-1][rand_wall[1]] == '0'):
		surr_cells += 1
	if (maze[rand_wall[0]+1][rand_wall[1]] == '0'):
		surr_cells += 1
	if (maze[rand_wall[0]][rand_wall[1]-1] == '0'):
		surr_cells +=1
	if (maze[rand_wall[0]][rand_wall[1]+1] == '0'):
		surr_cells += 1

	return surr_cells

def create_maze(height, width):
## Main code

    maze = []
    for i in range(0, height):
    	line = []
    	for j in range(0, width):
    		line.append('1')
    	maze.append(line)

    # Randomize starting point and set it a cell
    print(height)
    starting_height = randrange(height)
    print(width)
    starting_width = randrange(width)
    if (starting_height == 0):
    	starting_height += 1
    if (starting_height == height-1):
    	starting_height -= 1
    if (starting_width == 0):
    	starting_width += 1
    if (starting_width == width-1):
    	starting_width -= 1
    
    # Mark it as cell and add surrounding walls to the list
    maze[starting_height][starting_width] = '0'
    walls = []
    walls.append([starting_height - 1, starting_width])
    walls.append([starting_height, starting_width - 1])
    walls.append([starting_height, starting_width + 1])
    walls.append([starting_height + 1, starting_width])
    
    while (walls):
    	# Pick a random wall
    	rand_wall = walls[randrange(len(walls))-1]
    	
    	# Check if it is a left wall
    	if (rand_wall[1] != 0):
    		if (maze[rand_wall[0]][rand_wall[1]-1] == '1' and maze[rand_wall[0]][rand_wall[1]+1] == '0'):
    			# Find the number of surrounding cells
    			surr_cells = surroundingCells(maze, rand_wall)
    			if (surr_cells < 2):
    				# Denote the new path
    				maze[rand_wall[0]][rand_wall[1]] = '0'
    				# Mark the new walls
    				# Upper cell
    				if (rand_wall[0] != 0):
    					if (maze[rand_wall[0]-1][rand_wall[1]] != '0'):
    						maze[rand_wall[0]-1][rand_wall[1]] = '1'
    					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
    						walls.append([rand_wall[0]-1, rand_wall[1]])
    				
    
    				# Bottom cell
    				if (rand_wall[0] != height-1):
    					if (maze[rand_wall[0]+1][rand_wall[1]] != '0'):
    						maze[rand_wall[0]+1][rand_wall[1]] = '1'
    					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
    						walls.append([rand_wall[0]+1, rand_wall[1]])
    
    				# Leftmost cell
    				if (rand_wall[1] != 0):	
    					if (maze[rand_wall[0]][rand_wall[1]-1] != '0'):
    						maze[rand_wall[0]][rand_wall[1]-1] = '1'
    					if ([rand_wall[0], rand_wall[1]-1] not in walls):
    						walls.append([rand_wall[0], rand_wall[1]-1])
    			
    
    			# Delete wall
    			for wall in walls:
    				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
    					walls.remove(wall)
    
    			continue
    
    	# Check if it is an upper wall
    	if (rand_wall[0] != 0):
    		if (maze[rand_wall[0]-1][rand_wall[1]] == '1' and maze[rand_wall[0]+1][rand_wall[1]] == '0'):
    			surr_cells = surroundingCells(maze, rand_wall)
    			if (surr_cells < 2):
    				# Denote the new path
    				maze[rand_wall[0]][rand_wall[1]] = '0'
    				# Mark the new walls
    				# Upper cell
    				if (rand_wall[0] != 0):
    					if (maze[rand_wall[0]-1][rand_wall[1]] != '0'):
    						maze[rand_wall[0]-1][rand_wall[1]] = '1'
    					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
    						walls.append([rand_wall[0]-1, rand_wall[1]])
    
    				# Leftmost cell
    				if (rand_wall[1] != 0):
    					if (maze[rand_wall[0]][rand_wall[1]-1] != '0'):
    						maze[rand_wall[0]][rand_wall[1]-1] = '1'
    					if ([rand_wall[0], rand_wall[1]-1] not in walls):
    						walls.append([rand_wall[0], rand_wall[1]-1])
    
    				# Rightmost cell
    				if (rand_wall[1] != width-1):
    					if (maze[rand_wall[0]][rand_wall[1]+1] != '0'):
    						maze[rand_wall[0]][rand_wall[1]+1] = '1'
    					if ([rand_wall[0], rand_wall[1]+1] not in walls):
    						walls.append([rand_wall[0], rand_wall[1]+1])
    
    			# Delete wall
    			for wall in walls:
    				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
    					walls.remove(wall)
    
    			continue
    
    	# Check the bottom wall
    	if (rand_wall[0] != height-1):
    		if (maze[rand_wall[0]+1][rand_wall[1]] == '1' and maze[rand_wall[0]-1][rand_wall[1]] == '0'):
    			surr_cells = surroundingCells(maze, rand_wall)
    			if (surr_cells < 2):
    				# Denote the new path
    				maze[rand_wall[0]][rand_wall[1]] = '0'
    				# Mark the new walls
    				if (rand_wall[0] != height-1):
    					if (maze[rand_wall[0]+1][rand_wall[1]] != '0'):
    						maze[rand_wall[0]+1][rand_wall[1]] = '1'
    					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
    						walls.append([rand_wall[0]+1, rand_wall[1]])
    				if (rand_wall[1] != 0):
    					if (maze[rand_wall[0]][rand_wall[1]-1] != '0'):
    						maze[rand_wall[0]][rand_wall[1]-1] = '1'
    					if ([rand_wall[0], rand_wall[1]-1] not in walls):
    						walls.append([rand_wall[0], rand_wall[1]-1])
    				if (rand_wall[1] != width-1):
    					if (maze[rand_wall[0]][rand_wall[1]+1] != '0'):
    						maze[rand_wall[0]][rand_wall[1]+1] = '1'
    					if ([rand_wall[0], rand_wall[1]+1] not in walls):
    						walls.append([rand_wall[0], rand_wall[1]+1])
    
    			# Delete wall
    			for wall in walls:
    				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
    					walls.remove(wall)
    
    
    			continue
    
    	# Check the right wall
    	if (rand_wall[1] != width-1):
    		if (maze[rand_wall[0]][rand_wall[1]+1] == '1' and maze[rand_wall[0]][rand_wall[1]-1] == '0'):
    			surr_cells = surroundingCells(maze, rand_wall)
    			if (surr_cells < 2):
					
    				maze[rand_wall[0]][rand_wall[1]] = '0'
					
    				if (rand_wall[1] != width-1):
    					if (maze[rand_wall[0]][rand_wall[1]+1] != '0'):
    						maze[rand_wall[0]][rand_wall[1]+1] = '1'
    					if ([rand_wall[0], rand_wall[1]+1] not in walls):
    						walls.append([rand_wall[0], rand_wall[1]+1])
    				if (rand_wall[0] != height-1):
    					if (maze[rand_wall[0]+1][rand_wall[1]] != '0'):
    						maze[rand_wall[0]+1][rand_wall[1]] = '1'
    					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
    						walls.append([rand_wall[0]+1, rand_wall[1]])
    				if (rand_wall[0] != 0):	
    					if (maze[rand_wall[0]-1][rand_wall[1]] != '0'):
    						maze[rand_wall[0]-1][rand_wall[1]] = '1'
    					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
    						walls.append([rand_wall[0]-1, rand_wall[1]])
							
    			for wall in walls:
    				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
    					walls.remove(wall)
    			continue
			
    	for wall in walls:
    		if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
    			walls.remove(wall)
    
    # Set entrance and exit
    for i in range(0, width):
    	if (maze[1][i] == '0'):
    		maze[0][i] = '0'
    		break
    
    for i in range(width-1, 0, -1):
    	if (maze[height-2][i] == '0'):
    		maze[height-1][i] = '0'
    		break
    
    # Print final maze
    printMaze(maze)
    
    return maze