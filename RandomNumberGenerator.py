import random

class RandomNumberGenerator:

	def getRandomNumber(self, minLimit, maxLimit):
		return random.randint(minLimit, maxLimit)

