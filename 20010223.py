import pygame

import mazeclass

# Initialize pygame
pygame.init()

# Set the height and width of the screen
size = [1000, 500]
screen = pygame.display.set_mode(size)

# Set title of screen
pygame.display.set_caption("Maze Project")

# Get a new maze
mazegrid = [
    [2, 2, 2, 2, 2, 2, 2, 2, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
     2, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 2],
    [2, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1,
     1, 2],
    [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 2],
    [2, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 2],
    [2, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0,
     0, 2],
    [2, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1,
     1, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0,
     0, 2],
    [2, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1,
     0, 2],
    [2, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
     0, 2],
    [2, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1,
     1, 2],
    [2, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 2],
    [2, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 2],
    [2, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0,
     0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1,
     1, 2],
    [2, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0,
     0, 2],
    [2, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1,
     0, 2],
    [2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1,
     0, 2],
    [2, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
     0, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
     2, 2]]

the_maze = mazeclass.Maze(mazegrid)


##########################################################

# Code for moving one step forward and backward

def forwardbackward(curpos):
    # Warm up at the current position
    moveto(curpos, 3)
    # moveto(curpos, 3)
    # Look for positions that can be visited
    neighbourlist = unvisitedneighbours(curpos)
    if neighbourlist != []:
        # Select the first position that can be visited
        newpos = neighbourlist[0]
        # Go to that position
        moveto(newpos, 3)
        # Warm up at the new position
        moveto(newpos, 4)
        # Move back
        moveto(curpos, 4)


def unvisitedneighbours(curpos):
    # Return list of unvisited positions that can be reached from current position
    x = curpos[0]
    y = curpos[1]
    free = []
    for newpos in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= newpos[0] < the_maze.rows and 0 <= newpos[1] < the_maze.columns:
            if the_maze.grid[newpos[0]][newpos[1]].status == 0:
                free.append(newpos)
    return free


def moveto(newpos, status, movebot=True):
    # Mark the new position as being visited
    the_maze.grid[newpos[0]][newpos[1]].status = status
    exitlocation = isexitornot(newpos)

    # If required, move to the new position
    if movebot:
        the_maze.bot_xcoord = newpos[0]
        the_maze.bot_ycoord = newpos[1]
    if (len(exitlocation) == 1):
        exit_x, exit_y = exitlocation[0]
        the_maze.bot_xcoord = exit_x
        the_maze.bot_ycoord = exit_y

    # Wait a bit and then display the current state of the maze
    pygame.time.delay(1)
    the_maze.display_maze(screen)
    pygame.display.flip()
    pygame.event.pump()


def depthfirsttraversal(curpos):
    unvisited = unvisitedneighbours(curpos)

    for move in unvisited:  # Loop through all unvisited cells
        newpos = move
        moveto(newpos, 3)  # Move to the cell and set it as a visited cell
        depthfirsttraversal(newpos)

    moveto(curpos, 4)  # Move to the cell and set it as a revisited cell


def depthfirstsearch(curpos):
    # Perform a depth first search to find exit
    moveto(curpos, 3)
    unvisited = unvisitedneighbours(curpos)
    exit = isexitornot(curpos)

    for move in unvisited:
        newpos = move

        if (len(exit) == 1):  # If exit has been found, return true
            return True

        else:
            moveto(newpos, 3)  # Otherwise move to a cell which hasnt been revisited
            if (depthfirstsearch(newpos)):  # If exit has been found, end the function call
                return True

        moveto(newpos, 4)


def isexitornot(curpos):  # Finds the coords of the exit (if a path is neighbouring the exit)
    x = curpos[0]
    y = curpos[1]
    exitcoords = []
    for newpos in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= newpos[0] < the_maze.rows and 0 <= newpos[1] < the_maze.columns:
            if the_maze.grid[newpos[0]][newpos[1]].status == 5:
                exitcoords.append(newpos)
    return exitcoords


def breadthfirstsearch(curpos):
    queue = [[curpos]]

    # Iteratively explore positions until the exit has been found
    while queue != []:

        # Set the current position and the path leading to this position
        curpath = queue.pop(0)  # Removes the first index of curpath
        curpos = curpath[-1]
        moveto(curpos, 3, False)  # Moves a path (status 3) without theseus moving

        exit = isexitornot(curpos)  # Finds the exit coords

        if (len(exit) == 1):  # If the exit list has a length of 1 (exit has been found by a path)
            for cell in curpath:  # Then loop through the path that found the exit and move to the cells in the path.
                moveto(cell, 4)  # Enable moving so theseus moves

            break  # Break the loop (otherwise the paths keep searching) Loop finishes once thesues is at the exit coords

        allroutes = [curpath + [position] for position in unvisitedneighbours(curpos)]  # Creates a path
        queue.extend(allroutes)  # Adds this path to the end of the queue


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

######################################
# -------- Main Program Loop -----------
while done == False:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:  # If user wants to perform an action
            if event.key == pygame.K_f:
                the_maze.reset(mazegrid)
                forwardbackward((the_maze.bot_xcoord, the_maze.bot_ycoord))
            if event.key == pygame.K_d:
                the_maze.reset(mazegrid)
                depthfirsttraversal((the_maze.bot_xcoord, the_maze.bot_ycoord))
            if event.key == pygame.K_s:
                the_maze.reset(mazegrid)
                depthfirstsearch((the_maze.bot_xcoord, the_maze.bot_ycoord))
            if event.key == pygame.K_b:
                the_maze.reset(mazegrid)
                breadthfirstsearch((the_maze.bot_xcoord, the_maze.bot_ycoord))

    the_maze.display_maze(screen)
    # Limit to 50 frames per second
    clock.tick(30)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# If you forget this line, the program will 'hang' on exit.
pygame.quit()
