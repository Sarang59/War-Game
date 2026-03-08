class Creature:

	weak_against = []
	attacks = []

	def __init__(self, health_points = 0, identity = "Unknown", cry = "Unknown", laugh = "Unknown", alive = True, weapon = "Unknown"):
		self.health_points = health_points
		self.identity = identity
		self.cry = cry
		self.laugh = laugh
		self.alive = alive
		self.weapon = weapon
		self.weak_against = self.weak_against
		self.attacks = self.attacks
		
	def getAlive(self):
		return self.alive

	def getHealthPoints(self):
		return self.health_points

	def getIdentity(self):
		return self.identity

	def getCry(self):
		return self.cry

	def getLaugh(self):
		return self.laugh

	def getWeapon(self):
		return self.weapon

	def getWeakAgainst(self):
		return self.weak_against

	def setAlive(self, alive):
		self.alive = alive

	def getAttacks(self):
		return self.attacks

	def setHealthPoints(self, healthPoints):
		self.health_points = healthPoints

	def setIdentity(self, identity):
		self.identity = identity

	def setCry(self, cry):
		self.cry = cry

	def setLaugh(self, laugh):
		self.laugh = laugh

	def setWeapon(self, weapon):
		self.weapon = weapon

	def setWeakAgainst(self, weak_against):
		self.weak_against = weak_against

	def setAttacks(self, attacks):
		self.attacks = attacks

	def getProperString(self, lst: list) -> str:
		result = ""
		cnt = 0
		for item in lst:
			if cnt == (len(lst) - 1):
				result +=item+""
			else:
				result +=item+", "
			cnt += 1
		return result

	def __str__(self):
		attacks_result = self.getProperString(self.attacks)

		return f"| Identity: {self.identity} | Health points: {self.health_points} | Alive: {self.alive} | \n| Cry: {self.cry} |  Laugh: {self.laugh} | \n| Weapon: {self.weapon} | \n| Attacks: {attacks_result} |\n--------------------------------------------------------------------------" 

