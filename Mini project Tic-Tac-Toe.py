"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}
# dimension of the board

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    if board.check_win():
        return SCORES[board.check_win()], (-1, -1)
    else:   
        best_score = -SCORES[player] 
        best_move = (best_score,(-1, -1))
        possible_moves = board.get_empty_squares()        
        
        for possible_move in possible_moves:
            current_board = board.clone()
            current_board.move(possible_move[0], possible_move[1], player) 
            result = mm_move(current_board, provided.switch_player(player))
            score = result[0] 
           
            if score * SCORES[player] > best_score * SCORES[player]:
                best_score = score
                best_move =  (best_score, possible_move)
            if best_score == SCORES[player]:
                break
        return best_move    
            
                
        


def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

provided.play_game(move_wrapper, 1, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
