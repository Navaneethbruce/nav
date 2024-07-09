def ai_move(player, roll):
  best_score = -float('inf')  # Initialize with negative infinity
  best_piece = None
  for piece_num in range(4):
    if player.pieces[piece_num] == 0:  # Skip pieces in home
      continue
    new_position = (player.pieces[piece_num] + roll) % 56
    score = evaluate_move(player, piece_num, new_position, roll)  # Call evaluation function
    if score > best_score:
      best_score = score
      best_piece = piece_num
  return best_piece, best_score

def evaluate_move(player, piece_num, new_position, roll):
  score = 0
  # Add points for capturing opponent's piece
  if check_collision([player], new_position):
    score += 5
  # Add points for moving closer to finish
  if new_position > player.pieces[piece_num]:
    score += (new_position - player.pieces[piece_num])
  # Subtract points for risky moves (landing on opponent's occupied position)
  for other_player in players:
    if other_player != player and other_player.pieces[0] != 0 and other_player.pieces[0] == new_position:
      score -= 3
  return score
