import random



def game_play():
    print("Lets Play ROCK PAPER SCISSORS !!")
    print("LETS PLAYYYYYYYYYYYYYY")
    i = 0
    Me_score = 0
    Com_score = 0
    while(i<5):
        choose = ("rock","paper","scissors")
        com_choose = random.choice(choose)
        query = input("enter:")
        if (query == "rock"):
            if (com_choose == "rock"):
                print("ROCK")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                print("paper")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                print("Scissors")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "paper" ):
            if (com_choose == "rock"):
                print("ROCK")
                Me_score += 1
                print(f"Score:- ME :- {Me_score+1} : COM :- {Com_score}")

            elif (com_choose == "paper"):
                print("paper")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                print("Scissors")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "scissors" or query == "scissor"):
            if (com_choose == "rock"):
                print("ROCK")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                print("paper")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                print("Scissors")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
        i += 1
    
    print(f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}")

game_play()
def guessing_game():
    import random

    def guess_the_number():
        print("Welcome to the Guess the Number Game!")
        print("I'm thinking of a number between 1 and 100")

        
        secret_number = random.randint(1, 100)

        attempts = 0
        while True:
            try:

                guess = int(input("Your guess: "))
                attempts += 1

                if guess == secret_number:
                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
                    break
                elif guess < secret_number:
                    print("Too low. Try again.")
                else:
                    print("Too high. Try again.")
            except ValueError:
                print("Please enter a valid number.")

    if __name__ == "__main__":
        guess_the_number()

def tic_tac_toe():
    import pygame
    import sys
    import time


    pygame.init()


    WIDTH, HEIGHT = 600, 600
    LINE_WIDTH = 15
    WHITE = (255, 255, 255)
    LINE_COLOR = (0, 0, 0)
    BOARD_COLOR = (200, 200, 200)
    CIRCLE_COLOR = (255, 0, 0)
    CROSS_COLOR = (0, 0, 255)
    FONT_SIZE = 50


    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic Tac Toe")
    clock = pygame.time.Clock()


    font = pygame.font.Font(None, FONT_SIZE)


    board = [['' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False
    winner = None


    def draw_board():

        pygame.draw.rect(screen, BOARD_COLOR, (0, 0, WIDTH, HEIGHT))


        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT // 3), (WIDTH, HEIGHT // 3), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, 2 * HEIGHT // 3), (WIDTH, 2 * HEIGHT // 3), LINE_WIDTH)


        pygame.draw.line(screen, LINE_COLOR, (WIDTH // 3, 0), (WIDTH // 3, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (2 * WIDTH // 3, 0), (2 * WIDTH // 3, HEIGHT), LINE_WIDTH)

    def draw_symbols():
        for row in range(3):
            for col in range(3):
                if board[row][col] == 'X':
                    draw_cross(row, col)
                elif board[row][col] == 'O':
                    draw_circle(row, col)

    def draw_cross(row, col):
        x = col * WIDTH // 3
        y = row * HEIGHT // 3

        pygame.draw.line(screen, CROSS_COLOR, (x + 50, y + 50), (x + WIDTH // 3 - 50, y + HEIGHT // 3 - 50), LINE_WIDTH)
        pygame.draw.line(screen, CROSS_COLOR, (x + 50, y + HEIGHT // 3 - 50), (x + WIDTH // 3 - 50, y + 50), LINE_WIDTH)

    def draw_circle(row, col):
        x = col * WIDTH // 3 + WIDTH // 6
        y = row * HEIGHT // 3 + HEIGHT // 6

        pygame.draw.circle(screen, CIRCLE_COLOR, (x, y), WIDTH // 6 - 25, LINE_WIDTH)

    def draw_winner(winner):
        if winner:
            text = font.render(f"Player {winner} wins!", True, LINE_COLOR)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))


            for i in range(3):
                pygame.draw.rect(screen, BOARD_COLOR, (0, 0, WIDTH, HEIGHT))
                pygame.display.flip()
                time.sleep(0.5)

                screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
                pygame.display.flip()
                time.sleep(0.5)

        pygame.display.flip()

    def check_winner():

        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '':
                return board[i][0]  
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '':
                return board[0][i] 

        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
            return board[0][0]

        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
            return board[0][2] 

        return None

    def check_draw():
        for row in board:
            for cell in row:
                if cell == '':
                    return False 
        return True

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                row = y // (HEIGHT // 3)
                col = x // (WIDTH // 3)

                if board[row][col] == '':
                    board[row][col] = current_player
                    winner = check_winner()
                    if winner or check_draw():
                        game_over = True
                    else:
                        current_player = 'O' if current_player == 'X' else 'X'


        screen.fill(WHITE)
        draw_board()
        draw_symbols()
        draw_winner(winner)


        pygame.display.flip()


        clock.tick(30)

    