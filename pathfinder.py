import pygame, sys


def main():
    #Declaring colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    #Creating a size for window initialization
    size = (605, 605)

    # Declaring the height and width of the boxes
    height = 25
    width = 25

    # Declaring the margin of the boxes
    margin = 5

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

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (width + margin)
                row = pos[1] // (height + margin)
                if firstclick:
                    grid[row][column] = 1
                    firstclick = False
                    secondclick = True
                elif secondclick:
                    grid[row][column] = 2
                    secondclick = False
                else:
                    grid[row][column] = 3

        # Creating the grid
        for row in range(20):
            for column in range(20):
                color = WHITE
                if grid[row][column] == 1:
                    color = RED
                elif grid[row][column] == 2:
                    color = BLUE
                elif grid[row][column] == 3:
                    color = GREEN
                pygame.draw.rect(screen, color, [(margin + width) * column + margin, (margin + height) * row + margin, width, height], 0)
        
        pygame.display.flip()

if __name__ =="__main__":
    main()