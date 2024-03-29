template: http://www.codeskulptor.org/#poc_tttmm_template.py
TTTboard class: 
class TTTBoard:
    """
    Class to represent a Tic-Tac-Toe board.
    """

    def __init__(self, dim, reverse = False, board = None):
        """
        Initialize the TTTBoard object with the given dimension and 
        whether or not the game should be reversed.
        """
            
    def __str__(self):
        """
        Human readable representation of the board.
        """

    def get_dim(self):
        """
        Return the dimension of the board.
        """
    
    def square(self, row, col):
        """
        Returns one of the three constants EMPTY, PLAYERX, or PLAYERO 
        that correspond to the contents of the board at position (row, col).
        """

    def get_empty_squares(self):
        """
        Return a list of (row, col) tuples for all empty squares
        """

    def move(self, row, col, player):
        """
        Place player on the board at position (row, col).
        player should be either the constant PLAYERX or PLAYERO.
        Does nothing if board square is not empty.
        """
    def check_win(self):
        """
        Returns a constant associated with the state of the game
            If PLAYERX wins, returns PLAYERX.
            If PLAYERO wins, returns PLAYERO.
            If game is drawn, returns DRAW.
            If game is in progress, returns None.
        """
            
    def clone(self):
        """
        Return a copy of the board.
        """
For this assignment, your task is to implement a machine player for Tic-Tac-Toe that uses a Minimax strategy to decide its next move.
You will be able to use the same console-based interface and graphical user interface to play the game as you did before. 
Although the game is played on a 3 X 3 grid, your version should be able to handle any square grid (however, the time it will take to 
search the tree for larger grid sizes will be prohibitively slow). 

This project does not require you to write a lot of code. It does, however, bring together a lot of concepts that we have previously seen 
in the class. We would like you tothink about how these concepts are coming together to enable you to build a relatively complex machine player
with very little code. Further, you should think about the situations in which Minimax or Monte Carlo might produce better/worse machine players 
for games other than Tic-Tac-Toe.

We have provide a TTTBoard class for you to use. This class keeps track of the current state of the game board. You should familiarize youself with the 
interface to the TTTBoard class in the ""poc_ttt_provided" module. The provided module also has a "swithc_player(player) funcgion that returns the
other player (PLAYERX or PLAYER0). The provided module defines the constants EMPTY, PLAYERX, PLAYER0, and DRAW for you to use in your code.
The provided TTTBoard calss and GUI use these same constants, so you will need to use them in your code, as well.

At the bottom of the provided template, there are example calls to the GUI and console game player. You may uncomment and modify these during the 
development of your machine player to actually use it in the game. Note that these are the same calls we used previously for your Monte Carlo strategy, 
so we take an "ntrials" parameter. You can pass anything you want as "ntrials" , since  you will not e using it for Minimax. IN order to allow us to use 
the same infrastructure, we have also provided a "move-wrapper" function in the template that you can pass to "play_game" and "run_gui". This wrapper 
simply translates between the inputs and outputs of your function and those that were expected if you were implementing a Monte Carlo player.

Machine Player Strategy
Your machine player should use a Minimax strategy to choose the next move from a given Tic-Tac-Toe position. As the objective of this assignment is to help 
you bring together what you have learned, we ask that you do not search for pseudo-code to implement Minimax. At this point in the class, we hope that you 
can use the examples in the lectures and an English language description and be able to implement Minimax.

The general idea on Minimax is to search the entire game tree alternating between minimizing and maximizing the score at each level. For this to work,
you need to start at the bottom of the tree and work back towards the root. However, instead of actually building the game tree to do this, you should
use recursion to search the tree in a depth-first manner. Your recursive function should call itself on each child of the current board position and
then pick the move that maximizes (or minimizes, as appropriate) the score. If you do this, your recursive function will naturally explore all the way
down to the bottom of the tree along each path in turn, leading to a depth first search that will implement Minimax. The following page describes the 
process in more detail.

As you recursively call your minimax function, you should create a copy of the board to pass to the next level. When the function returns, you no 
longer need that copy of the board. In this manner, you are dynamically constructing the part of the game tree that you are actively looking at, 
but you do not need to keep it around.

For this mini-project, you need only implement one function:
mm_move(board, player): This function takes a current board and which player should move next. The function should use Minimax to return a tuple
which is a score for the current board and the best move for the player in the form of a (row, column) tuple. In situations in which the game is over,
you should return a valid score and the move(-1,-1). As (-1, -1) is an illegal move, it should only be returned in cases where there is no move 
that can be made.

You should imports the TTT class and a wrapper function to enable you to play the game.

Hints
You do not need to write a lot of code to implement Minimax, but it can be difficult to get everything working correctly.
Here are some hints that may help you out:

Do not forget the base case in your recursive function. Think carefully about when you can return with an answer immediately.

Remember to make a copy of the board before you recursively call your function. If you do not, you will modify the current board and you will not be 
searching the correct tree.

The SCORES dictionary is useful. You should use it to score a completed board. For example, the score of a board in which X has won should be 
SCORES[provided.PLAYERX]. If the game is a draw, you should score the board as 0

In Minimax, you need to alternate between maximizing and minimizing. Given the SCORES that we have provided you with, player X is always the 
maximizing player and play O is always the minimizing player. You can use an else statement to decide when to maximize and when to minimize. 
But, you can also be more clever by noticing that if you multiply the score by SCORES[player] then you can always maximize. Why? Because this 
has the effect of negating player O's scores allowing you to maximize instead of minimize for player O.

Minimax can be slow when there are a lot of moves to explore. The way we have set up the scoring, you do not always need to search everything. 
If you find a move that yields a winning score (+1 for X or -1 for O), you know that you cannot do any better by continuing to search the other 
possible moves from the current board. So, you can just return immediately with the score and move at that point. This will significantly speed 
up the search.
