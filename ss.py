import os

puzzle = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

#Solves the puzzle using defined functions below
def solve(board):

	nextEmpty = isEmpty(board)

	if nextEmpty == None:
		return True
	else:
		row, column = nextEmpty

	for i in range(1, 10):
		if logic(board, i, row, column):
			board[row][column] = i

			if solve(board):
				return True

		board[row][column] = 0

	return False

def logic(board, number, row, column):

	#Row
	for i in range(len(board)):
		if board[row][i] == number:
			return False

	#Column 
	for i in range(len(board)):
		if board[i][column] == number:
			return False

	#Box
	x = column // 3
	y = row // 3

	for i in range(y * 3, y * 3 + 3):
		for j in range(x * 3, x * 3 + 3):
			if board[i][j] == number:
				return False

	return True


def printBoard(board):

	for i in range(len(board)):
		if i % 3 == 0 and i != 0:
			print("- - - - - - - - - - - - ")

		for j in range(len(board)):
			if j % 3 == 0 and j != 0:
				print(" | ", end = "")
			if j == 8:
				print(board[i][j])
			else:
				print(str(board[i][j]) + " ", end = "")

def isEmpty(board):

	for i in range(len(board)):
		for j in range(len(board)):
			if board[i][j] == 0:
				return(i, j)
		
	return None

def main():
	os.system("cls")
	
	printBoard(puzzle)

	os.system("pause")
	os.system("cls")

	solve(puzzle)
	printBoard(puzzle)

main()