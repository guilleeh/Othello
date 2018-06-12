import othello_logic

ROWS = 8
COLUMNS = 8
EMPTY=0
WHITE=1
BLACK=2

DEBUG = 0

my_board = [[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
			[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
			[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
			[EMPTY, EMPTY, EMPTY, BLACK, WHITE, EMPTY, EMPTY, EMPTY],
			[EMPTY, EMPTY, EMPTY, WHITE, BLACK, EMPTY, EMPTY, EMPTY],
			[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
			[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
			[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]]

def print_board( state ):
	''' Prints the board '''
	for i in range(ROWS):
		for j in range(COLUMNS):
			if state[i][j] == EMPTY:
				print(" . ", end=' ')  
			elif state[i][j] == WHITE:
				print(" W ", end=' ')
			else:
				print(" B ", end=' ')
		print()

def welcome_message():
	print("Welcome to Othello v1.0")

def choose_player():
	player = input("Who goes first BLACK or WHITE? --> ")	
	if( player == "WHITE" ):
		return WHITE
	elif( player == "BLACK" ):
		return BLACK

def change_player(turn):
	'''switches players turn'''
	if( turn == BLACK ):
		return WHITE
	return BLACK

def ask_place():
	'''asks the user for tile placement, returns coordinates'''
	coords = input("Place tile in(ROW, COLUMN): ")
	return (coords[0], coords[2])
	
def say_player_turn(turn):
	print("Player", turn, "'s turn")

def show_score():
	print("WHITE: ", othello_logic.WHITE_SCORE, ", BLACK: ", othello_logic.BLACK_SCORE)

def show_winner():
	if( othello_logic.WINNER == BLACK ):
		print("Player", BLACK, "(BLACK) has won!")
	elif( othello_logic.WINNER == WHITE ):
		print("Player", WHITE, "(WHITE) has won!")
	elif( othello_logic.WINNER == TIE ):
		print("No player won, stalemate!")

if __name__ == '__main__':
	welcome_message()
	current_player = choose_player()
	print_board(my_board)
	while( othello_logic.WINNER == EMPTY ):
		while(1):
			coords = ask_place()
			result_tup = othello_logic.make_move(my_board, coords, current_player) #tuple
			my_board = result_tup[0]
			if( result_tup[1] ):
				break
		print_board(my_board)
		othello_logic.count_tiles(my_board)
		show_score()
		if( not othello_logic.check_game_over(my_board) ):
			current_player = change_player(current_player)
			say_player_turn(current_player)
	show_winner()
