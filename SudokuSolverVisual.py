import time
import pandas
import pygame

grid_user =     [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0]]

grid = pandas.DataFrame(grid_user)


def block(number):
    number = int(number / 3) * 3
    return number

def check_possible(column, row, number):
    for check_number in range(9):
        # check if number already exits somewhere in column
        if number == grid[column][check_number]:
            return False
        # check if number already exits somewhere in row
        elif number == grid[check_number][row]:
            return False
    # transfer from column and row location to corresponding 3x3 block and check if number exits somewhere in block
    block_list = grid.iloc[block(row):block(row) + 3, block(column):block(column) + 3].values.tolist()
    for block_column in block_list:
        for block_element in block_column:
            if number == block_element:
                return False
    return True

def check_finished():
    for row in grid.values.tolist():
        for element in row:
            if element == 0:
                return False
    print(grid)
    print("Finished!")
    global solved_flag
    solved_flag = 1

def solve():
    for column in range(9):
        for row in range(9):
            if grid[column][row] == 0:
                for number in range(1, 10):  # 10 not included
                    if check_possible(column, row, number):
                        grid[column][row] = number

                        print(str(column) + str(row) + str(number))

                        grid_list_of_lists = grid.values.tolist()
                        grid_list = [item for sublist in grid_list_of_lists for item in sublist]
                        steps_list.append(grid_list)

                        check_finished()
                        solve()
                    if solved_flag == 0:
                        grid[column][row] = 0
                return

def draw_screen():
    screen.fill(WHITE)

    box_size = 50
    box_counter = 0
    for box_column in range(0, screen_x, box_size):
        for box_row in range(0, screen_y, box_size):
            rect = pygame.Rect(box_row, box_column, box_size, box_size)
            pygame.draw.rect(screen, BLACK, rect, 1)

            text_message = grid_list[box_counter]
            if(text_message != 0):
                textsurface = myfont.render(str(text_message), False, (0, 0, 0))
                screen.blit(textsurface, (box_row + (box_size - textsurface.get_rect()[2]) / 2,
                                          box_column + (box_size - textsurface.get_rect()[3]) / 2))
            box_counter += 1

    pygame.display.update()

def draw_screen_empty():
    screen.fill(WHITE)

    box_size = 50
    box_counter = 0
    for box_column in range(0, screen_x, box_size):
        for box_row in range(0, screen_y, box_size):
            rect = pygame.Rect(box_row, box_column, box_size, box_size)
            if('mouse_position' in globals()):
                if(int(mouse_position[0]/box_size)*box_size == box_row and int(mouse_position[1]/box_size)*box_size == box_column):
                    pygame.draw.rect(screen, GREEN, rect, 5)
                else:
                    pygame.draw.rect(screen, BLACK, rect, 1)
            else:
                pygame.draw.rect(screen, BLACK, rect, 1)

            grid_list_of_lists = grid.values.tolist()
            grid_list = [item for sublist in grid_list_of_lists for item in sublist]


            text_message = grid_list[box_counter]
            if(text_message != 0):
                textsurface = myfont.render(str(text_message), False, (0, 0, 0))
                screen.blit(textsurface, (box_row + (box_size - textsurface.get_rect()[2]) / 2,
                                          box_column + (box_size - textsurface.get_rect()[3]) / 2))
            box_counter += 1

    pygame.display.update()

def draw_startscreen():
    screen.fill(WHITE)

    text_message = "Press SPACE to"
    textsurface = myfont2.render(str(text_message), False, (0, 0, 0))
    screen.blit(textsurface, ((screen_x - textsurface.get_rect()[2])/2,(screen_y - textsurface.get_rect()[3])/2-35))

    text_message = "progress through game"
    textsurface = myfont2.render(str(text_message), False, (0, 0, 0))
    screen.blit(textsurface, ((screen_x - textsurface.get_rect()[2]) / 2, (screen_y - textsurface.get_rect()[3]) / 2+35))

    pygame.display.update()
# initialize pygame
pygame.init()

# used colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (50, 200, 50)

# create window
screen_x = 450
screen_y = 450
screen = pygame.display.set_mode((screen_x, screen_y))

# Main title of created window
pygame.display.set_caption("SudokuSolver")

# display text
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 35)
myfont2 = pygame.font.SysFont('Comic Sans MS', 35)

# run while True
gameactive = True

# for setting refresh time later
clock = pygame.time.Clock()

# extra necessary variables
solved_flag = 0
given = 0
steps_list = []
steps_counter = 0
box_size = 50
startscreen =1

while gameactive:
    # Refresh-time (per second)
    clock.tick(60)

    # check whether user did an action
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameactive = False
            print("User aborted by clicking close button!")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
        elif event.type == pygame.KEYDOWN:
            for i in range(0,10):
                if 'mouse_position' in globals() and event.key == eval("pygame.K_" + str(i)):
                    grid[int(mouse_position[0] / box_size)][int(mouse_position[1] / box_size)] = i
                if 'mouse_position' in globals() and event.key == eval("pygame.K_KP_" + str(i)):
                    grid[int(mouse_position[0] / box_size)][int(mouse_position[1] / box_size)] = i
            if event.key == pygame.K_SPACE:
                if(startscreen == 0):
                    given = 1
                startscreen = 0
                if(solved_flag == 1 and steps_counter >= len(steps_list)):
                    gameactive = False

    if startscreen == 1:
        draw_startscreen()

    if(startscreen == 0 and given == 0):
        draw_screen_empty()

    if solved_flag == 0 and given == 1:
        solve()

    if solved_flag == 1:
        if(steps_counter < len(steps_list)):
            grid_list = steps_list[steps_counter]
            steps_counter += 1
            draw_screen()
            time.sleep(0.1)

pygame.quit()
exit()
