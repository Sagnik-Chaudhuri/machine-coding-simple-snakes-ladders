import time
from classes.Dice import Dice
from classes.Jumper import Jumper
from classes.Board import Board
from classes.Player import Player
import queue


class Game():
    def __init__(self, board_size, number_of_players) -> None:
        self.board_size = board_size
        self.number_of_players = number_of_players
        self.board = Board(self.board_size)
        self.players = queue.Queue()
        self.dice = Dice(1)
        self.ladders = []
        self.snakes = []
        self.players_position = dict()

    def initialise_game(self):

        for player in range(0, self.number_of_players):
            player_name = input("enter player name")
            player_id = input("enter id")
            self.players.put(Player(player_id, player_name))
            self.players_position[player_id] = 0

        snake_1 = Jumper(5, 2)
        snake_2 = Jumper(7, 3)
        ladder_1 = Jumper(4, 9)

        self.ladders.append(ladder_1)
        self.snakes.append(snake_1)
        self.snakes.append(snake_2)

    def play_game(self):
        while not self.players.empty():
            time.sleep(3)
            player = self.players.get()
            next_move = self.dice.roll_dice()
            print("dice rolled: ", next_move, 'for player: ', player.id)
            player_id = player.id
            current_position = self.players_position[player_id]
            final_position = current_position + next_move
            if final_position > self.board.size:
                print("Winner is Player: ", player.name)
                break

            for snake in self.snakes:
                if snake.starting_point == final_position:
                    print("player bitten by snake")
                    final_position = snake.ending_point

            for ladder in self.ladders:
                if ladder.starting_point == final_position:
                    print("player raised by ladder")
                    final_position = ladder.ending_point

            print('New Final Position', final_position)
            self.players_position[player_id] = final_position
            self.players.put(player)
