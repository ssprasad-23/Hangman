class Hangman:
	def __init__(self):
		self.board = []
		self.lives = 6
		self.word = ["papaya", "banana", "cherry"]
		self.winword = ""

	def main(self):
		start = input("start new game? Y/N").lower()
		print(start)

new_game = Hangman()
new_game.main()



