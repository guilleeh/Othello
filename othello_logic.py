ROWS = 8
COLUMNS = 8
EMPTY=0
WHITE=1
BLACK=2
TIE=3
WINNER = EMPTY
INVALID_MOVE = 0 #1 means true, 0 means false

BLACK_SCORE = 0
WHITE_SCORE = 0

def flip_tiles(board, turn, tile_list):
	for row, column in tile_list:
		board[row][column] = turn

def search_tiles(board, turn, row, column, diff_row, diff_col):
	'''Searches down line to get all tiles to flip'''
	new_row = row + diff_row
	new_col = column + diff_col
	tile_list = []

	while(1):
		#print("ROW: ", new_row, ", COL: ", new_col)
		if( new_row >= 0 and new_row < ROWS and new_col >= 0 and new_col < COLUMNS ):	
			if( board[new_row][new_col] == EMPTY ):
				tile_list = []
				break
			elif( board[new_row][new_col] == turn ):
				break
			elif( board[new_row][new_col] != turn ):
				tile_list.append((new_row, new_col))
			new_row = new_row + diff_row
			new_col = new_col + diff_col
		else:
			tile_list = []
			break
	flip_tiles(board, turn, tile_list)
	return len(tile_list)

def reverse_tiles(board, turn, move):
	row = int(move[0])
	column = int(move[1])
	to_flip = [] #List of tile tuples we need to flip, (ROW, COL)
	one_valid = 0 #When checking all 8 directions, have we found at least 1 poss path?, count it here...
	
	#CHECK TOP
	if( ((row-1) >= 0 and board[row-1][column] != EMPTY) 
		and board[row-1][column] != turn ):
		#print("TOP:", row-1, column)
		one_valid += search_tiles(board, turn, row, column, -1, 0)
	
	#CHECK TOP-RIGHT
	if( ((row-1) >= 0) and ((column+1) < COLUMNS)
		and board[row-1][column+1] != EMPTY and board[row-1][column+1] != turn ):
		#print("TOP-RIGHT:", row-1, column+1)
		one_valid += search_tiles(board, turn, row, column, -1, 1)
		

	#CHECK RIGHT
	if( ((column+1) < COLUMNS and board[row][column+1] != EMPTY) 
		and board[row][column+1] != turn ):
		#print("RIGHT:", row, column+1)
		one_valid += search_tiles(board, turn, row, column, 0, 1)
		

	#CHECK BOTTOM-RIGHT
	if( ((row+1) < ROWS) and ((column+1) < COLUMNS) 
		and board[row+1][column+1] != EMPTY and board[row+1][column+1] != turn ):
		#print("BOTTOM-RIGHT:", row+1, column+1)
		one_valid += search_tiles(board, turn, row, column, 1, 1)
		

	#CHECK BOTTOM
	if( ((row+1) < ROWS) and board[row+1][column] != EMPTY 
		and board[row+1][column] != turn ):
		#print("BOTTOM:", row+1, column)
		one_valid += search_tiles(board, turn, row, column, 1, 0)
		

	#CHECK BOTTOM-LEFT
	if( ((column-1) >= 0) and ((row+1) < ROWS) and 
		board[row+1][column-1] != EMPTY and board[row+1][column-1] != turn ):
		#print("BOTTOM-LEFT:", row+1, column-1)
		one_valid += search_tiles(board, turn, row, column, 1, -1)

	#CHECK LEFT
	if( ((column-1) >= 0) and board[row][column-1] != EMPTY
		and board[row][column-1] != turn ):
		#print("LEFT:", row, column-1)
		one_valid += search_tiles(board, turn, row, column, 0, -1)
		
	
	#CHECK TOP-LEFT
	if( ((column-1) >= 0) and ((row-1) >= 0)
		and board[row-1][column-1] != EMPTY and board[row-1][column-1] != turn ):
		#print("TOP-LEFT:", row-1, column-1)
		one_valid += search_tiles(board, turn, row, column, -1, -1)
		
	return one_valid

def check_if_valid(board, row, column, turn):
	if( row >= 0 and row < ROWS and column >= 0 and column < COLUMNS ):
		if( board[row][column] == EMPTY ):
			return True
	return False

def board_is_full(board):
	'''Checks if the board is full'''
	for i in range(ROWS):
		for j in range(COLUMNS):
			if ( board[i][j] == EMPTY ):
				return False 
	return True

def reset_score():
	global WHITE_SCORE
	global BLACK_SCORE
	WHITE_SCORE = 0
	BLACK_SCORE = 0

def count_tiles(board):
	reset_score()
	global WHITE_SCORE
	global BLACK_SCORE
	for i in range(ROWS):
		for j in range(COLUMNS):
			if( board[i][j] == WHITE ):
				WHITE_SCORE += 1
			elif( board[i][j] == BLACK ):
				BLACK_SCORE += 1

def check_game_over(state):
	'''Checks if the game is over'''
	global WINNER
	if( board_is_full(state) ):
		count_tiles(state)
		if( WHITE_SCORE > BLACK_SCORE ):
			WINNER = WHITE
		elif( WHITE_SCORE < BLACK_SCORE ):
			WINNER = BLACK
		else:
			WINNER = TIE
		return True
	return False


def make_move(state, move, turn):
	'''Places tile on board'''
	row = int(move[0])
	column = int(move[1])
	if (turn == WHITE):
		if ( check_if_valid(state, row, column, WHITE) ): #First, check if valid move
			if( reverse_tiles(state, turn, move) > 0 ): #Check if path available
				state[row][column] = WHITE
				return (state, True)
			else: #No path available, try again
				return (state, False)
		else:
			return (state, False)
	elif ( turn == BLACK ):
		if ( check_if_valid(state, row, column, BLACK) ):
			if( reverse_tiles(state, turn, move) > 0):
				state[row][column] = BLACK					
				return (state, True)
			else:
				return (state, False)
		else:
			return (state, False)
	return state


'''TO DO - WE HAVE TO CHECK THAT THE USER CANNOT PLACE A TILE JUST ANYWHERE IN THE BOARD'''

