import sys
import random

class Hangman:
	def __init__(self):
		self.board = []
		self.lives = 6
		self.word = ["pineapple", "banana", "cherry"]
		self.winword = ""

	def main(self):
		start = input("start new game? Y/N").lower()
		if start == "y":
			self.winword = random.choice(self.word)
			#print the word in board
			# print(self.winword)
			self.setUp()
			self.play()

		else:
			sys.exit("ttyl")

	def setUp(self):
		for ch in range(len(self.winword)):
			self.board.append('_')
		print("lives" + str(self.lives))

	def play(self):
		print(self.board)
		guessed = []

		while self.lives > 0:
			letter = input("guess a letter: ")
			if letter in self.winword and letter not in guessed:
				guessed.append(letter)
				self.refreshBoard(letter)
				self.checkIfWin()
			elif letter in guessed:
				print("you have already guessed this letter! try again!")
			else:
				guessed.append(letter)
				print("that letter does not exist in the word@ try again")
				self.lives -=1
			print(self.board)
			print("lives: " + str(self.lives))
		print("you are out of lives! the word was: " + self.winword)

	def refreshBoard(self, letter):
		for i, ch in enumerate(self.winword):
			if letter == ch:
				self.board[i] = letter

	def checkIfWin(self):
		board_str = ''.join([str(ch) for ch in self.board])
		if board_str == self.winword:
			print("congrats you won!! :)")
			sys.exit()

new = Hangman()
new.main()





