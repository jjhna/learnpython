# game.py
# import the draw module
from draw_module import draw_game
from game_module import play_game

def main():
    result = play_game()
    draw_game(result)

# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
    main()