import pygame
import sys
import numpy as np
import heapq

"""
This pathfinder program was created by Leander Mathisen.
The purpose was to find the shortest calculated route from a start point to an end point on a grid.
The window will appear with a grid and a green button below.
To start press anywhere on the grid to define a start point and press again anywhere on the grid to define an end point.
Then any further presses on the grid will create obstacles that the shortest path will not be able to use.
After finishing start and end points and obstacles, press the green button for the shortest path to be calculated and displayed.
"""

# fscore calculator
def heuristic(a, b):
    return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

# A* pathfinding algorithm
def astar(array, start, goal):
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    oheap = []
    heapq.heappush(oheap, (fscore[start], start))

    while oheap:
        current = heapq.heappop(oheap)[1]
        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j            
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:                
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue
                
            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue
                
            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))

def main():
    #Declaring colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

    #Creating a size for window initialization
    size = (605, 700)

    # Declaring the height and width of the boxes
    height = 25
    width = 25

    # Declaring the margin of the boxes
    margin = 5

    # Initializing some variables
    start = ()
    end = ()
    route = []

    # Declaring the first and second clicks for the start and target positions
    firstclick = True
    secondclick = False

    # Declaring the grid
    grid = []
    for row in range(20):
        grid.append([])
        for column in range(20):
            grid[row].append(0)

    pygame.init()

    # Creating a window
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pathfinder")
    pygame.Surface.fill(screen, BLACK)

    # Declaring variables for if program is running or for shortest path to be built and presented
    running = True
    build = False
    print_route = False
    build_complete = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (width + margin)
                row = pos[1] // (height + margin)
                try:
                    if not build_complete:
                        if firstclick:
                            firstclick = False
                            secondclick = True
                            start = (row, column)
                        elif secondclick:
                            secondclick = False
                            end = (row, column)
                        else:
                            grid[row][column] = 1
                except:
                    build = True


        # Creating the grid
        for row in range(20):
            for column in range(20):
                color = WHITE
                if (row, column) == start:
                    color = RED
                elif (row, column) == end:
                    color = BLUE
                elif (row, column) in route:
                    color = YELLOW
                elif grid[row][column] == 1:
                    color = GREEN
                pygame.draw.rect(screen, color, [(margin + width) * column + margin, (margin + height) * row + margin, width, height], 0)
        
        # Creating the build button
        pygame.draw.rect(screen, GREEN, [0, 605, 605, 95])

        # When the button is pressed the shortest path is calculated
        while build:
            grid2 = np.array(grid)
            route = astar(grid2, start, end)
            build = False
            print_route = True
            route = route + [start]
            route = route[::-1]
            build_complete = True
        
        # Printing the route to the console
        if print_route:
            print(route)
            print_route = False
        
        # Displaying updates to the window
        pygame.display.flip()

if __name__ =="__main__":
    main()