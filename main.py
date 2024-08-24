import pygame as pg
import pygame.display

pg.display.init()
pg.font.init()

#set size
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
GRID_WIDTH = 400
GRID_HEIGHT = 400

x_offset = (WINDOW_HEIGHT - GRID_HEIGHT) / 2
y_offset = (WINDOW_WIDTH - GRID_WIDTH) / 2

screen = pg.display.set_mode(size=(WINDOW_WIDTH,WINDOW_HEIGHT))
pg.display.set_caption("Tic Tac Toe")
bg_color = (255,255,255)

#image
img_scaled_height = 400/3
img_scaled_width = 400/3
x_img = pg.image.load("X.png");
x_img = pg.transform.scale(x_img,(img_scaled_width,img_scaled_height))
o_img = pg.image.load("O.jpg");
o_img = pg.transform.scale(o_img,(img_scaled_width,img_scaled_height))


arr_game_grid = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

#functions
def display_grid():
    start_x = GRID_WIDTH/3
    start_y = GRID_HEIGHT/3
    end_x = GRID_WIDTH
    end_y = GRID_HEIGHT

    #border
    # pg.draw.line(screen, (255, 0, 0), (x_offset, y_offset), (end_x+x_offset,end_y+y_offset), 3)
    # pg.draw.line(screen, (255, 0, 0), (x_offset, y_offset), (end_x + x_offset, y_offset), 3)
    # pg.draw.line(screen, (255, 0, 0), (x_offset, y_offset + GRID_HEIGHT), (end_x + x_offset, y_offset + GRID_HEIGHT), 3)
    # pg.draw.line(screen, (255, 0, 0), (x_offset, y_offset), (x_offset, y_offset+ GRID_HEIGHT), 3)
    # pg.draw.line(screen, (255, 0, 0), (x_offset+ GRID_WIDTH, y_offset), (GRID_WIDTH + x_offset,GRID_HEIGHT+y_offset), 3)



    #draw vertical lines

    pg.draw.line(screen,(0,0,0),(start_x + x_offset,y_offset),(start_x + x_offset,end_y+y_offset), 5)
    pg.draw.line(screen, (0, 0, 0), (start_x*2 + x_offset, y_offset), (start_x*2 + x_offset, end_y + y_offset), 5)
    #draw horizontal lines
    pg.draw.line(screen, (0, 0, 0), (x_offset,start_y + y_offset), (end_x + x_offset, start_y + y_offset), 5)
    pg.draw.line(screen, (0, 0, 0), (x_offset, start_y*2 + y_offset ), (end_x + x_offset, start_y*2 + y_offset ), 5)

def display_moves():
    x_cor = GRID_WIDTH/3
    y_cor = GRID_HEIGHT/3

    for i_index,i_value in enumerate(arr_game_grid):
        for j_index, value in enumerate(i_value):
            if value == 1:
                screen.blit(x_img,(x_offset + x_cor * j_index, y_offset + y_cor * i_index) )
            elif value == 2:
                screen.blit(o_img, (x_offset + x_cor * j_index, y_offset + y_cor * i_index))

def display_winner(winner_font,player):
    winner_text = winner_font.render(f"Player: {player} wins!", True, (255,0,0))
    winner_rect = winner_text.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4))

    return winner_text, winner_rect

def save_moves(x,y):
    #boundries
    x_bound = GRID_WIDTH/3
    y_bound = GRID_HEIGHT/3

    if x_offset < x < x_offset + x_bound:
        if y_offset < y < y_offset + y_bound:
            return (0, 0)
        elif y_offset + y_bound < y < y_offset + y_bound * 2:
            return (1, 0)
        elif y_offset + y_bound * 2 < y < y_offset + y_bound * 3:
            return (2, 0)

    elif x_offset + x_bound < x < x_offset + x_bound * 2:
        if y_offset < y < y_offset + y_bound:
            return (0, 1)
        elif y_offset + y_bound < y < y_offset + y_bound * 2:
            return (1, 1)
        elif y_offset + y_bound * 2 < y < y_offset + y_bound * 3:
            return (2, 1)

    elif x_offset + x_bound * 2 < x < x_offset + x_bound * 3:
        if y_offset < y < y_offset + y_bound:
            return (0, 2)
        elif y_offset + y_bound < y < y_offset + y_bound * 2:
            return (1, 2)
        elif y_offset + y_bound * 2 < y < y_offset + y_bound * 3:
            return (2, 2)

def apply_move(player, index_one, index_two):
    if arr_game_grid[index_one][index_two] == 0:
        arr_game_grid[index_one][index_two] = player
        return True

def switch_player(player):
    if player ==1:
        return 2
    else:
        return 1

def check_win(player):
    if (arr_game_grid[0][0] == player) and (arr_game_grid[0][1] == player) and (arr_game_grid[0][2] == player):
        return True
    if (arr_game_grid[1][0] == player) and (arr_game_grid[1][1] == player) and (arr_game_grid[1][2] == player):
        return True
    if (arr_game_grid[2][0] == player) and (arr_game_grid[2][1] == player) and (arr_game_grid[2][2] == player):
        return True
    if (arr_game_grid[0][0] == player) and (arr_game_grid[1][0] == player) and (arr_game_grid[2][0] == player):
        return True
    if (arr_game_grid[0][1] == player) and (arr_game_grid[1][1] == player) and (arr_game_grid[2][1] == player):
        return True
    if (arr_game_grid[0][2] == player) and (arr_game_grid[1][2] == player) and (arr_game_grid[2][2] == player):
        return True
    if (arr_game_grid[0][0] == player) and (arr_game_grid[1][1] == player) and (arr_game_grid[2][2] == player):
        return True
    if (arr_game_grid[0][2] == player) and (arr_game_grid[1][1] == player) and (arr_game_grid[2][0] == player):
        return True

    return False

def reset_arr_game_grid():
    for i in arr_game_grid:
        for j_index, value in enumerate(i):
            i[j_index] = 0

    print(arr_game_grid)


def main():

    running = True
    game_end = False
    player = 1
    winner_font = pg.font.Font(None,74)
    winner_text = None
    winner_rect = None
    bool_winner = False
    move_count = 0


    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.display.quit()

            if event.type == pg.MOUSEBUTTONDOWN:

                if game_end == False:
                    pos = pg.mouse.get_pos()
                    move = save_moves(pos[0],pos[1])

                    try:
                        if apply_move(player, move[0],move[1]):
                                if check_win(player):
                                    bool_winner = True
                                    game_end = True
                                else:
                                    player = switch_player(player)
                                    move_count += 1

                                    if move_count > 8:
                                        game_end = True

                    except:
                        print("Failed to apply move")

        try:
            screen.fill(bg_color)
            display_grid()
            display_moves()
            if move_count == 9:
                pg.display.update()

            if game_end == True:
                if bool_winner:
                    winner_text, winner_rect = display_winner(winner_font, player)
                    screen.blit(winner_text, winner_rect)
                else:
                    pg.time.delay(1000)
                    reset_arr_game_grid()
                    display_moves()
                    game_end = False
                    move_count = 0

            pg.display.update()

        except:
            print("Failed to display")

if __name__ == "__main__":
    main()
