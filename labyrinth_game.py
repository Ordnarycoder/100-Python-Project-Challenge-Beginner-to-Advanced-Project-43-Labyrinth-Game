import pygame
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
CELL_SIZE = 50 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

player_pos = [1, 1]

goal_pos = [7, 8]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Labyrinth Game")

def draw_maze():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if maze[row][col] == 1:
                pygame.draw.rect(screen, BLACK, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)

def draw_player():
    player_rect = pygame.Rect(
        player_pos[1] * CELL_SIZE + 5,
        player_pos[0] * CELL_SIZE + 5,
        CELL_SIZE - 10,
        CELL_SIZE - 10,
    )
    pygame.draw.rect(screen, BLUE, player_rect)

def draw_goal():
    goal_rect = pygame.Rect(
        goal_pos[1] * CELL_SIZE + 5,
        goal_pos[0] * CELL_SIZE + 5,
        CELL_SIZE - 10,
        CELL_SIZE - 10,
    )
    pygame.draw.rect(screen, GREEN, goal_rect)

def move_player(dx, dy):
    new_x = player_pos[0] + dx
    new_y = player_pos[1] + dy
    if maze[new_x][new_y] == 0:  
        player_pos[0] = new_x
        player_pos[1] = new_y

def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            move_player(-1, 0)
        if keys[pygame.K_DOWN]:
            move_player(1, 0)
        if keys[pygame.K_LEFT]:
            move_player(0, -1)
        if keys[pygame.K_RIGHT]:
            move_player(0, 1)
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_w]:
            move_player(-1, 0)
        if keys[pygame.K_s]:
            move_player(1, 0)
        if keys[pygame.K_a]:
            move_player(0, -1)
        if keys[pygame.K_d]:
            move_player(0, 1)    

        if player_pos == goal_pos:
            print("You win!")
            pygame.quit()
            sys.exit()

        screen.fill(WHITE)
        draw_maze()
        draw_player()
        draw_goal()
        pygame.display.flip()

        clock.tick(30)

if __name__ == "__main__":
    main()
