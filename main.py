
pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6], [1, 4, 7], [0, 3, 6], [2, 5, 8]]


def print_grid():
	grid = f'\n{pos[0]} | {pos[1]} | {pos[2]}\n' \
	       f'---------\n' \
	       f'{pos[3]} | {pos[4]} | {pos[5]}\n' \
	       f'---------\n' \
	       f'{pos[6]} | {pos[7]} | {pos[8]}\n'
	print(grid)


def get_player_input(player_symbol):
	while True:
		position_input = input(f'Player {player_symbol} selects position 1-9: ')
		try:
			position = int(position_input) - 1
			if 0 <= position <= 8 and position not in ['⭕', '❌']:
				return position
			else:
				print('Choose an empty field.')
		except ValueError:
			print('Wrong value, number 1-9 only.')
		except IndexError:
			print('Enter number between 1 and 9.')


def check_draw():
	return all(pos[i] in ['⭕', '❌'] for i in range(len(pos)))


def check_winner():
	for combo in winning_combinations:
		if pos[combo[0]] == pos[combo[1]] == pos[combo[2]]:
			return True
	return False


def player_move():
	print('\nTic Tac Toe')
	print_grid()
	game_on = True
	player_1 = True
	n1 = n2 = []

	while game_on:
		position = get_player_input('⭕' if player_1 else '❌')
		if player_1:
			n1.append(position)
			pos[position] = '⭕'
		else:
			n2.append(position)
			pos[position] = '❌'
		print_grid()
		player_1 = not player_1

		if check_draw():
			print("It's a draw!")
			game_on = False

		elif check_winner():
			if player_1:
				print("Player 2 '❌' has won!")
			else:
				print("Player 1 '⭕' has won!")
			game_on = False
	print('Game ended.')


player_move()
