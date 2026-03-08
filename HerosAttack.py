class HerosAttack:

	def attackRanger(self, beast, attack_power):
		print("Something 1")


	def updateHealthPoints(self, attack_power, creature):
		if creature.getHealthPoints() - attack_power <= 0:
			creature.setHealthPoints(0)
		else:	
			creature.setHealthPoints(creature.getHealthPoints() - attack_power)


			