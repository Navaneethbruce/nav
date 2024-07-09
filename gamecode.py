import random

class Player:
  def __init__(self, name, color):
    self.name = name
    self.color = color
    self.pieces = [0] * 4  # List to store positions of 4 tokens (0: in home, >0: on board)

def roll_dice():
  return random.randint(1, 6)

def move_piece(player, piece_num, roll):
  current_position = player.pieces[piece_num]
  if current_position == 0:  # Check if piece is in home
    if roll == 6:
      new_position = 1  # Move out of home on rolling 6
      print(f"{player.name}'s piece {piece_num + 1} leaves home!")
    else:
      new_position = current_position  # Stay in home if not 6
  else:
    new_position = (current_position + roll) % 56  # Wrap around the board
  player.pieces[piece_num] = new_position
  return new_position

def check_collision(players, position):
  for player in players:
    for piece_num in range(4):
      if player.pieces[piece_num] == position and player.pieces[piece_num] != 0:
        player.pieces[piece_num] = 0  # Send opponent's piece back to home
        print(f"{player.name}'s piece knocks {players[0].name}'s piece {piece_num + 1} back home!")
        return True
  return False

def is_winner(player):
  return all(piece > 51 for piece in player.pieces)  # Check if all pieces are in finish area (> 51)

def main():
  num_players = int(input("Enter number of players (2-4): "))
  if num_players < 2 or num_players > 4:
    print("Invalid number of players!")
    return

  players = []
  colors = ["Red", "Green", "Blue", "Yellow"]
  for i in range(num_players):
    name = input(f"Enter player {i + 1} name: ")
    players.append(Player(name, colors[i]))

  current_player = 0
  while True:
    print(f"\n** {players[current_player].name}'s turn! **")
    roll = roll_dice()
    print(f"You rolled a {roll}.")

    if roll == 6:
      print("Roll again!")
      continue  # Roll again if 6

    choice = int(input("Choose a piece to move (1-4) or press 0 to pass: ")) - 1
    if choice < 0 or choice > 3 or players[current_player].pieces[choice] == 0:
      print("Invalid choice!")
      continue

    new_position = move_piece(players[current_player], choice, roll)
    print(f"{players[current_player].name}'s piece {choice + 1} moved to {new_position}.")

    if check_collision(players, new_position):
      continue  # Skip next player if collision happened

    if is_winner(players[current_player]):
      print(f"\n** {players[current_player].name} wins! Congratulations!**")
      break

    current_player = (current_player + 1) % num_players

if __name__ == "__main__":
  main()
