from classes.Game import Game


def main():

    players_count = 2
    board_size = 10
    dice_count = 1

    game = Game(board_size, players_count)
    game.initialise_game()
    game.play_game()

    return None


main()
