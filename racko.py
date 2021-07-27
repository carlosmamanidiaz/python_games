# File: racko.py
# Description: A program that simulates the card and number game
# Rack-O. Players use the keyboard and take turns.


import random


def main():
	"""Play one game of Rack-O."""
	# Get the rack size, create the deck, and deal the initial racks.
	rack_size = prep_game()
	deck = list(range(1, 61))
	random.shuffle(deck)	
	discard_pile = [] # Create a empy list to fill with discard cards
	player_1_rack = get_rack(deck, rack_size) # Get the player's deck
	deck = [x for x in deck if x not in player_1_rack] # delete the player's deck from the full deck of cards
	player_2_rack = get_rack(deck, rack_size) # Get the player's deck
	deck = [x for x in deck if x not in player_2_rack] # delete the player's deck from the full deck of cards
	discard = deck.pop(0) # Get dicard card
	discard_pile.append(discard)
	check = False
	
	while not (check): # A while loop is used for players to play until one of them completes their deck in ascending order. 
		print("Player 1's turn.")
		print(f"Your current rack  {player_1_rack}")
		print("Top of discard pile ", discard)
		player_1_rack,discard = take_turn(deck, discard, player_1_rack) #Take the player's turn 
		print()	
		discard_pile.append(discard)
		check = is_sorted(player_1_rack) # Check if any of the players achieved to have their deck with ascending numbers.
		if len(deck) < 1 :
			print("Deck is empty. Shuffling discard pile.")
			deck = list(reversed(discard_pile))# Reserve the discard pile order and now it will be the new deck
			random.shuffle(deck)
			discard = deck.pop(0)
			discard_pile = []

		if check:# If check is true then the player has his deck of cards in ascending order
			print("Player 1 wins!")
			break
		
		print("Player 2's turn.")
		print(f"Your current rack  {player_2_rack}")
		print("Top of discard pile ", discard)
		player_2_rack,discard = take_turn(deck, discard, player_2_rack) #Take the player's turn
		discard_pile.append(discard)
		print()	
		if len(deck) < 1 :
			print("Deck is empty. Shuffling discard pile.")
			deck = list(reversed(discard_pile))	# Reserve the discard pile order and now it will be the new deck		
			random.shuffle(deck)
			discard = deck.pop(0)
			discard_pile = []
		check = is_sorted(player_2_rack) # Check if any of the players achieved to have their deck with ascending numbers.
		if check: # If check is true then the player has his deck of cards in ascending order
			print("Player 2 wins!")
			break
	# CS303e students. Complete the main method to play
	# one complete game of Rack-O using the specified functions.


def prep_game():
	"""Get ready to play 1 game.

	Show the instructions if the user wants to see them.
	Set the seed for the random number generator.
	Return the size of the rack to use.
	"""

	print('----- Welcome to Rack - O! -----')
	if input('Enter y to display instructions: ') == 'y':
		instructions()
	print()
	random.seed(int(input('Enter number for initial seed: ')))
	rack_size = int(input('Enter the size of the rack to use. '
						  + 'Must be between 5 and 10: '))
	while not 5 <= rack_size <= 10:
		print(rack_size, 'is not a valid rack size.')
		rack_size = int(input('Enter the size of the rack to use. '
							  + 'Must be between 5 and 10: '))
	print()
	return rack_size


def instructions():
	"""Print the instructions of the game."""
	print()
	print('The goal of the game is to get the cards in your rack of cards')
	print('into ascending order. Your rack has ten slots numbered 1 to 10.')
	print('During your turn you can draw the top card of the deck or take')
	print('the top card of the discard pile.')
	print('If you draw the top card of the deck, you can use that card to')
	print('replace a card in one slot of your rack. The replaced card goes to')
	print('the discard pile.')
	print('Alternatively you can simply choose to discard the drawn card.')
	print('If you take the top card of the discard pile you must use it to')
	print('replace a card in one slot of your rack. The replaced card goes')
	print('to the top of the discard pile.')

def take_turn(deck, discard, player_rack):
	"""Take the player's turn.

	Give them the choice of drawing or taking the top card of the
	discard pile. If they draw they can replace a card or discard the
	draw. If they take the top card of the discard pile they must
	replace a card in their rack.
	"""
	
	choice = input("Enter d to draw anything else to take top of discard pile: ")
	print()
	if choice == "d":
		drew = deck.pop(0) # Get a card from the full deck of cards
		print(f"drew the {drew}")
		if input("Enter p to place card, anything else to discard it: ") == "p":
			player_rack, discard = place_card(player_rack, drew, discard) # Function to replace one card with another
		else: 
			discard = drew
			print(f"The rack after the turn  {player_rack}")
		return player_rack, discard
	else:
		player_rack, discard = place_card(player_rack, discard, discard) # Function to replace one card with another
		return player_rack, discard
	

def place_card(player_rack, new_card, discard):
	"""Ask the player which card to replace in their rack.

	Replace it with the given new card. Place the card removed
	from the player's rack at the top of the discard pile.
	Error checks until player enters a card that is currently
	in their rack.
	"""
	card_number = 0
	while card_number not in player_rack: # A while loop is used for verify if the card entered is in the player's deck
		card_number = int(input(f"Enter the card number to replace with the {new_card}: "))
		if card_number not in player_rack: # If the card is not in the player's deck send a message
			print(f"{card_number} is not in your rack.")
		
	player_rack[player_rack.index(card_number)] = new_card # Replace the card from player's deck for the new card
	discard = card_number # Leave the old card of the player in the discard pile
	print(f"The rack after the turn  {player_rack}")

	return player_rack, discard



def is_sorted(rack):
	"""Return if this rack is sorted in ascending order.

	CS303e assignment limitation:
	Do not create any new lists in this function.
	"""
	# To check for strictly increasing list (Boolean Output)
	check = all(i < j for i, j in zip(rack, rack[1:]))

	return check


def get_rack(deck, rack_size):
	"""Deal the top rack_size cards of the deck into a new rack.

	The first card goes in the first slot, the second card goes in
	the second slot, and so forth. We assume len(deck) >= rack_size.
	Return the list of ints representing the rack.
	"""
	rack_player = deck[:rack_size]
	return rack_player


main()
