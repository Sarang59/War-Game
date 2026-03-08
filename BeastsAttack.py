from RandomNumberGenerator import RandomNumberGenerator 

class BeastsAttack:

	def __init__(self):
		self.RNG = RandomNumberGenerator()

	def OrcAttacks(self, hero, beast, num):
		attack_dict = {"Sword attack" : 25, "Sword combat" : 30}
		attack_identity = beast.attacks[num - 1]
		attack_power = attack_dict[attack_identity]
			
		if hero.getIdentity() == "Squire" or hero.getIdentity() == "Gallant" or hero.getIdentity() == "Crusader" or hero.getIdentity() == "Gladiator":
			print(f"The {hero.getIdentity()} has been hit by {attack_identity}.....")
			print(f"However it hasn't taken too much damage.....")
			self.updateHealthPoints(attack_power, hero)
			decrease_power = RNG.getRandomNumber(25,30)
			self.updateHealthPoints(decrease_power, beast)
			print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
			print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
		
		elif hero.getIdentity() == "Ranger" or hero.getIdentity() == "Archer" or hero.getIdentity() == "Bishop" or hero.getIdentity() == "Musketeer" or hero.getIdentity() == "Thunderer" or hero.getIdentity() == "Wizard":
			print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
			print(f"However the attack has been stopped by another attack.....")
			decrease_power = 0
			if hero.getIdentity() == "Wizard":
				decrease_power = self.RNG.getRandomNumber(80,85)	
			if hero.getIdentity == "Thunderer":
				decrease_power = self.RNG.getRandomNumber(70,75)	
			elif hero.getIdentity() == "Musketeer":
				decrease_power = self.RNG.getRandomNumber(60,65)
			else:
				decrease_power = self.RNG.getRandomNumber(50,55)
			self.updateHealthPoints(decrease_power, beast)
			print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
			print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
		
		elif hero.getIdentity() == "Rook" or hero.getIdentity() == "Champion":
			print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
			print(f"However the attack has been countered by shield.....")
			decrease_power = 0
			if hero.getIdentity() == "Champion":
				decrease_power = self.RNG.getRandomNumber(75,80)
			else:	
				decrease_power = self.RNG.getRandomNumber(50,55)
			self.updateHealthPoints(decrease_power, beast)
			print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
			print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

		elif hero.getIdentity() == "Knight" or hero.getIdentity() == "Paladin":
			random_no = self.RNG.getRandomNumber(0,2)
			print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")

			if random_no == 2 and hero.getIdentity() == "Paladin":
				print(f"However the attack has been countered by shield.....")
			elif random_no == 0 or random_no == 2:
				print(f"However the {hero.getIdentity()} dodged it.....")
			elif random_no == 1:
				print(f"However the attack has been countered by sword.....")
			
			decrease_power = self.RNG.getRandomNumber(55,60)
			self.updateHealthPoints(decrease_power, beast)
			print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
			print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
	
		elif hero.getIdentity() == "Hercules":
			print(f"The {hero.getIdentity()} has barely scratched by {attack_identity}.....")
			print(f"So no damage taken by {hero.getIdentity()}.....")
			decrease_power = self.RNG.getRandomNumber(65,70)
			self.updateHealthPoints(decrease_power, beast)
			print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
			print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

		elif hero.getIdentity() == "Magical Knight" or hero.getIdentity() == "General":
			random_no = RNG.getRandomNumber(0,3)
			print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
			if random_no == 0:
				print(f"However the attack has been blocked by shield.....")
			elif random_no == 1:
				print(f"However the attack has been stopped by sword.....")
			elif random_no == 2:
				print(f"However the attack has been countered by another attack.....")
			else:
				print(f"However the attack was dodged by {hero.getIdentity()}....")

			decrease_power = 0
			if hero.getIdentity() == "Magical Knight":
				decrease_power = self.RNG.getRandomNumber(85,90)
			else:
				decrease_power = self.RNG.getRandomNumber(90,100)
				
			self.updateHealthPoints(decrease_power, beast)
			print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
			print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

	def GoblinAttacks(self, hero, beast, num):
		
		if hero.getIdentity() not in beast.getWeakAgainst():
			attack_dict = {"Wood shot" : 30, "Bullet shot" : 50}
			attack_identity = beast.attacks[num - 1]
			attack_power = attack_dict[attack_identity]

			print(f"The {hero.getIdentity()} has been hit by {attack_identity}.....")
			decrease_power = self.RNG.getRandomNumber(25,30)
			self.updateHealthPoints(decrease_power, beast)
			self.updateHealthPoints(attack_power, hero)
			print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
			print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
		else:
			attack_dict = {"Wood shot" : 15, "Bullet shot" : 25}
			attack_identity = beast.attacks[num - 1]
			attack_power = attack_dict[attack_identity]

			if hero.getIdentity() == "Gallant" or hero.getIdentity() == "Crusader" or hero.getIdentity() == "Gladiator":
				print(f"The {hero.getIdentity()} has been hit by {attack_identity}.....")
				print(f"However it hasn't taken too much damage.....")
				self.updateHealthPoints(attack_power, hero)
				decrease_power = self.RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Bishop" or hero.getIdentity() == "Musketeer" or hero.getIdentity() == "Thunderer" or hero.getIdentity() == "Wizard":
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				print(f"However the attack has been stopped by another attack.....")
				decrease_power = 0
				if hero.getIdentity() == "Wizard":
					decrease_power = self.RNG.getRandomNumber(80,85)	
				if hero.getIdentity == "Thunderer":
					decrease_power = self.RNG.getRandomNumber(70,75)	
				elif hero.getIdentity() == "Musketeer":
					decrease_power = self.RNG.getRandomNumber(60,65)
				else:
					decrease_power = self.RNG.getRandomNumber(50,55)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Rook" or hero.getIdentity() == "Champion":
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				print(f"However the attack has been countered by shield.....")
				decrease_power = 0
				if hero.getIdentity() == "Champion":
					decrease_power = self.RNG.getRandomNumber(75,80)
				else:	
					decrease_power = self.RNG.getRandomNumber(50,55)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Knight" or hero.getIdentity() == "Paladin":
				random_no = self.RNG.getRandomNumber(0,2)
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")

				if random_no == 2 and hero.getIdentity() == "Paladin":
					print(f"However the attack has been countered by shield.....")
				elif random_no == 0 or random_no == 2:
					print(f"However the {hero.getIdentity()} dodged it.....")
				elif random_no == 1:
					print(f"However the attack has been countered by sword.....")
				
				decrease_power = self.RNG.getRandomNumber(55,60)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
		
			elif hero.getIdentity() == "Hercules":
				print(f"The {hero.getIdentity()} has barely scratched by {attack_identity}.....")
				print(f"So no damage taken by {hero.getIdentity()}.....")
				decrease_power = self.RNG.getRandomNumber(65,70)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Magical Knight" or hero.getIdentity() == "General":
				random_no = self.RNG.getRandomNumber(0,3)
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				if random_no == 0:
					print(f"However the attack has been blocked by shield.....")
				elif random_no == 1:
					print(f"However the attack has been stopped by sword.....")
				elif random_no == 2:
					print(f"However the attack has been countered by another attack.....")
				else:
					print(f"However the attack was dodged by {hero.getIdentity()}....")

				decrease_power = 0
				if hero.getIdentity() == "Magical Knight":
					decrease_power = self.RNG.getRandomNumber(85,90)
				else:
					decrease_power = self.RNG.getRandomNumber(90,100)
					
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

	def ElfAttacks(self, hero, beast, num):

		if hero.getIdentity() == "Squire":
			attack_dict = {"Spear attack" : 40, "Spear combat" : 50}
			attack_identity = beast.attacks[num - 1]
			attack_power = attack_dict[attack_identity]

			print(f"The {hero.getIdentity()} has been hit by {attack_identity}.....")
			decrease_power = self.RNG.getRandomNumber(25,30)
			self.updateHealthPoints(decrease_power, beast)
			self.updateHealthPoints(attack_power, hero)
			print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
			print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
		else:
			attack_dict = {"Spear combat" : 25, "Spear attack" : 15}
			attack_identity = beast.attacks[num - 1]
			attack_power = attack_dict[attack_identity]

			if hero.getIdentity() == "Gallant" or hero.getIdentity() == "Crusader" or hero.getIdentity() == "Gladiator":
				print(f"The {hero.getIdentity()} has been hit by {attack_identity}.....")
				print(f"However it hasn't taken too much damage.....")
				self.updateHealthPoints(attack_power, hero)
				decrease_power = self.RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
		
			elif hero.getIdentity() == "Bishop" or hero.getIdentity() == "Musketeer" or hero.getIdentity() == "Thunderer" or hero.getIdentity() == "Wizard":
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				print(f"However the attack has been stopped by another attack.....")
				decrease_power = 0
				if hero.getIdentity() == "Wizard":
					decrease_power = self.RNG.getRandomNumber(80,85)	
				if hero.getIdentity == "Thunderer":
					decrease_power = self.RNG.getRandomNumber(70,75)	
				elif hero.getIdentity() == "Musketeer":
					decrease_power = self.RNG.getRandomNumber(60,65)
				else:
					decrease_power = self.RNG.getRandomNumber(50,55)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Rook" or hero.getIdentity() == "Champion":
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				print(f"However the attack has been countered by shield.....")
				decrease_power = 0
				if hero.getIdentity() == "Champion":
					decrease_power = self.NG.getRandomNumber(75,80)
				else:	
					decrease_power = self.RNG.getRandomNumber(50,55)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Knight" or hero.getIdentity() == "Paladin":
				random_no = self.RNG.getRandomNumber(0,2)
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")

				if random_no == 2 and hero.getIdentity() == "Paladin":
					print(f"However the attack has been countered by shield.....")
				elif random_no == 0 or random_no == 2:
					print(f"However the {hero.getIdentity()} dodged it.....")
				elif random_no == 1:
					print(f"However the attack has been countered by sword.....")
				
				decrease_power = self.RNG.getRandomNumber(55,60)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
		
			elif hero.getIdentity() == "Hercules":
				print(f"The {hero.getIdentity()} has barely scratched by {attack_identity}.....")
				print(f"So no damage taken by {hero.getIdentity()}.....")
				decrease_power = self.RNG.getRandomNumber(65,70)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Magical Knight" or hero.getIdentity() == "General":
				random_no = self.RNG.getRandomNumber(0,3)
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				if random_no == 0:
					print(f"However the attack has been blocked by shield.....")
				elif random_no == 1:
					print(f"However the attack has been stopped by sword.....")
				elif random_no == 2:
					print(f"However the attack has been countered by another attack.....")
				else:
					print(f"However the attack was dodged by {hero.getIdentity()}....")

				decrease_power = 0
				if hero.getIdentity() == "Magical Knight":
					decrease_power = self.RNG.getRandomNumber(85,90)
				else:
					decrease_power = self.RNG.getRandomNumber(90,100)
					
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

	def DwarfAttacks(self, hero, beast, num):

		if hero.getIdentity() not in beast.getWeakAgainst():
			attack_dict = {"Axe attack" : 45, "Axe combat" : 55}
			attack_identity = beast.attacks[num - 1]
			attack_power = attack_dict[attack_identity]

			if hero.getIdentity() == "Squire":
				print(f"The {hero.getIdentity()} has been hit by {attack_identity}.....")
				decrease_power = self.RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, beast)
				self.updateHealthPoints(attack_power, hero)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
			
			elif hero.getIdentity() == "Archer" or hero.getIdentity() == "Ranger":
				print(f"The {hero.getIdentity()} tried stopping the attack by another attack. However the attack was missed.....!")
				print(f"And thus, {hero.getIdentity()} has been hit by {attack_identity}.....")
				decrease_power = self.RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, beast)
				self.updateHealthPoints(attack_power, hero)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
			
		else:
			attack_dict = {"Axe attack" : 20, "Axe combat" : 25}
			attack_identity = beast.attacks[num - 1]
			attack_power = attack_dict[attack_identity]

			if hero.getIdentity() == "Gallant" or hero.getIdentity() == "Crusader" or hero.getIdentity() == "Gladiator":
				print(f"The {hero.getIdentity()} has been hit by {attack_identity}.....")
				print(f"However it hasn't taken too much damage.....")
				self.updateHealthPoints(attack_power, hero)
				decrease_power = self.RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
			
			elif hero.getIdentity() == "Bishop" or hero.getIdentity() == "Musketeer" or hero.getIdentity() == "Thunderer" or hero.getIdentity() == "Wizard":
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				print(f"However the attack has been stopped by another attack.....")
				decrease_power = 0
				if hero.getIdentity() == "Wizard":
					decrease_power = self.RNG.getRandomNumber(80,85)	
				if hero.getIdentity == "Thunderer":
					decrease_power = self.RNG.getRandomNumber(70,75)	
				elif hero.getIdentity() == "Musketeer":
					decrease_power = self.RNG.getRandomNumber(60,65)
				else:
					decrease_power = self.RNG.getRandomNumber(50,55)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Rook" or hero.getIdentity() == "Champion":
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				print(f"However the attack has been countered by shield.....")
				decrease_power = 0
				if hero.getIdentity() == "Champion":
					decrease_power = self.RNG.getRandomNumber(75,80)
				else:	
					decrease_power = self.RNG.getRandomNumber(50,55)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Knight" or hero.getIdentity() == "Paladin":
				random_no = self.RNG.getRandomNumber(0,2)
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")

				if random_no == 2 and hero.getIdentity() == "Paladin":
					print(f"However the attack has been countered by shield.....")
				elif random_no == 0 or random_no == 2:
					print(f"However the {hero.getIdentity()} dodged it.....")
				elif random_no == 1:
					print(f"However the attack has been countered by sword.....")
				
				decrease_power = self.RNG.getRandomNumber(55,60)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
		
			elif hero.getIdentity() == "Hercules":
				print(f"The {hero.getIdentity()} has barely scratched by {attack_identity}.....")
				print(f"So no damage taken by {hero.getIdentity()}.....")
				decrease_power = self.RNG.getRandomNumber(65,70)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Magical Knight" or hero.getIdentity() == "General":
				random_no = self.RNG.getRandomNumber(0,3)
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				if random_no == 0:
					print(f"However the attack has been blocked by shield.....")
				elif random_no == 1:
					print(f"However the attack has been stopped by sword.....")
				elif random_no == 2:
					print(f"However the attack has been countered by another attack.....")
				else:
					print(f"However the attack was dodged by {hero.getIdentity()}....")

				decrease_power = 0
				if hero.getIdentity() == "Magical Knight":
					decrease_power = self.RNG.getRandomNumber(85,90)
				else:
					decrease_power = self.RNG.getRandomNumber(90,100)
					
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

	def WerewolfAttacks(self, hero, beast, num):

		if hero.getIdentity() not in beast.getWeakAgainst():
			attack_dict = {"Hammer attack" : 50, "Hammer combat" : 60}
			attack_identity = beast.attacks[num - 1]
			attack_power = attack_dict[attack_identity]

			if hero.getIdentity() == "Squire" or hero.getIdentity() == "Gallant" or hero.getIdentity() == "Crusader":
				print(f"The {hero.getIdentity()} has been hit by {attack_identity}.....")
				decrease_power = self.RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, beast)
				self.updateHealthPoints(attack_power, hero)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
			
			elif hero.getIdentity() == "Archer" or hero.getIdentity() == "Ranger":
				print(f"The {hero.getIdentity()} tried stopping the attack by another attack. However the attack was missed.....!")
				print(f"And thus, {hero.getIdentity()} has been hit by {attack_identity}.....")
				decrease_power = self.RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, beast)
				self.updateHealthPoints(attack_power, hero)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
			
		else:
			attack_dict = {"Hammer attack" : 25, "Hammer combat" : 30}
			attack_identity = beast.attacks[num - 1]
			attack_power = attack_dict[attack_identity]

			if hero.getIdentity() == "Gladiator":
				print(f"The {hero.getIdentity()} has been hit by {attack_identity}.....")
				print(f"However it hasn't taken too much damage.....")
				self.updateHealthPoints(attack_power, hero)
				decrease_power = self.RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
			
			elif hero.getIdentity() == "Bishop" or hero.getIdentity() == "Musketeer" or hero.getIdentity() == "Thunderer" or hero.getIdentity() == "Wizard":
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				print(f"However the attack has been stopped by another attack.....")
				decrease_power = 0
				if hero.getIdentity() == "Wizard":
					decrease_power = self.RNG.getRandomNumber(80,85)	
				if hero.getIdentity == "Thunderer":
					decrease_power = self.RNG.getRandomNumber(70,75)	
				elif hero.getIdentity() == "Musketeer":
					decrease_power = self.RNG.getRandomNumber(60,65)
				else:
					decrease_power = self.RNG.getRandomNumber(50,55)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Rook" or hero.getIdentity() == "Champion":
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				print(f"However the attack has been countered by shield.....")
				decrease_power = 0
				if hero.getIdentity() == "Champion":
					decrease_power = self.RNG.getRandomNumber(75,80)
				else:	
					decrease_power = self.RNG.getRandomNumber(50,55)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Knight" or hero.getIdentity() == "Paladin":
				random_no = self.RNG.getRandomNumber(0,2)
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")

				if random_no == 2 and hero.getIdentity() == "Paladin":
					print(f"However the attack has been countered by shield.....")
				elif random_no == 0 or random_no == 2:
					print(f"However the {hero.getIdentity()} dodged it.....")
				elif random_no == 1:
					print(f"However the attack has been countered by sword.....")
				
				decrease_power = self.RNG.getRandomNumber(55,60)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
		
			elif hero.getIdentity() == "Hercules":
				print(f"The {hero.getIdentity()} has barely scratched by {attack_identity}.....")
				print(f"So no damage taken by {hero.getIdentity()}.....")
				decrease_power = self.RNG.getRandomNumber(65,70)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Magical Knight" or hero.getIdentity() == "General":
				random_no = self.RNG.getRandomNumber(0,3)
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				if random_no == 0:
					print(f"However the attack has been blocked by shield.....")
				elif random_no == 1:
					print(f"However the attack has been stopped by sword.....")
				elif random_no == 2:
					print(f"However the attack has been countered by another attack.....")
				else:
					print(f"However the attack was dodged by {hero.getIdentity()}....")

				decrease_power = 0
				if hero.getIdentity() == "Magical Knight":
					decrease_power = self.RNG.getRandomNumber(85,90)
				else:
					decrease_power = self.RNG.getRandomNumber(90,100)
				
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

	def MinotaurAttacks(self, hero, beast, num):

		if hero.getIdentity() not in beast.getWeakAgainst():
			attack_dict = {"Sword attack": 50, "Shield attack": 55, "Sword combat": 60}
			attack_identity = beast.attacks[num - 1]
			attack_power = attack_dict[attack_identity]

			if hero.getIdentity() == "Squire" or hero.getIdentity() == "Gallant" or hero.getIdentity() == "Crusader":
				print(f"The {hero.getIdentity()} has been hit by {attack_identity}.....")
				decrease_power = self.RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, beast)
				self.updateHealthPoints(attack_power, hero)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
			
			elif hero.getIdentity() == "Archer" or hero.getIdentity() == "Ranger":
				print(f"The {hero.getIdentity()} tried stopping the attack by another attack. However the attack was missed.....!")
				print(f"And thus, {hero.getIdentity()} has been hit by {attack_identity}.....")
				decrease_power = self.RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, beast)
				self.updateHealthPoints(attack_power, hero)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
		else:
			attack_dict = {"Sword attack": 25, "Shield attack": 30, "Sword combat": 35}
			attack_identity = beast.attacks[num - 1]
			attack_power = attack_dict[attack_identity]

			if hero.getIdentity() == "Rook":
				print(f"The {hero.getIdentity()} tried stopping the attack by another attack.")
				print(f"However some attacks were missed and some were hit.....!")
				print(f"And thus, {hero.getIdentity()} has been hit by {attack_identity}.....")
				print(f"{beast.getIdentity()} was also hit by some attacks of {hero.getIdentity()}")
				decrease_power = self.RNG.getRandomNumber(25,35)
				self.updateHealthPoints(decrease_power, beast)
				self.updateHealthPoints(attack_power, hero)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
			
			elif hero.getIdentity() == "Gladiator":
				print(f"The {hero.getIdentity()} has been hit by {attack_identity}.....")
				print(f"However it hasn't taken too much damage.....")
				self.updateHealthPoints(attack_power, hero)
				decrease_power = self.RNG.getRandomNumber(40,45)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Bishop" or hero.getIdentity() == "Musketeer" or hero.getIdentity() == "Thunderer" or hero.getIdentity() == "Wizard":
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				print(f"However the attack has been stopped by another attack.....")
				decrease_power = 0
				if hero.getIdentity() == "Wizard":
					decrease_power = self.RNG.getRandomNumber(80,85)	
				if hero.getIdentity == "Thunderer":
					decrease_power = self.RNG.getRandomNumber(70,75)	
				elif hero.getIdentity() == "Musketeer":
					decrease_power = self.RNG.getRandomNumber(60,65)
				else:
					decrease_power = self.RNG.getRandomNumber(50,55)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Champion":
				random_no = self.RNG.getRandomNumber(0,1)
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				if random_no == 0:
					print(f"However the attack has been countered by shield.....")
				else:
					print(f"However the attack was swiftly dodged by {hero.getIdentity()}....")
				decrease_power = self.RNG.getRandomNumber(75,80)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Knight" or hero.getIdentity() == "Paladin":
				random_no = self.RNG.getRandomNumber(0,2)
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")

				if random_no == 2 and hero.getIdentity() == "Paladin":
					print(f"However the attack has been countered by shield.....")
				elif random_no == 0 or random_no == 2:
					print(f"However the {hero.getIdentity()} dodged it.....")
				elif random_no == 1:
					print(f"However the attack has been countered by sword.....")
				
				decrease_power = self.RNG.getRandomNumber(55,60)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
		
			elif hero.getIdentity() == "Hercules":
				print(f"The {hero.getIdentity()} has barely scratched by {attack_identity}.....")
				print(f"So no damage taken by {hero.getIdentity()}.....")
				decrease_power = self.RNG.getRandomNumber(65,70)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Magical Knight" or hero.getIdentity() == "General":
				random_no = self.RNG.getRandomNumber(0,3)
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				if random_no == 0:
					print(f"However the attack has been blocked by shield.....")
				elif random_no == 1:
					print(f"However the attack has been stopped by sword.....")
				elif random_no == 2:
					print(f"However the attack has been countered by another attack.....")
				else:
					print(f"However the attack was dodged by {hero.getIdentity()}....")

				decrease_power = 0
				if hero.getIdentity() == "Magical Knight":
					decrease_power = self.RNG.getRandomNumber(85,90)
				else:
					decrease_power = self.RNG.getRandomNumber(90,100)
				
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

	def CerberusAttacks(self, hero, beast, num):

		if hero.getIdentity() not in beast.getWeakAgainst():
			attack_dict = {"Claw attack": 55, "Claw combat": 60}
			attack_identity = beast.attacks[num - 1]
			attack_power = attack_dict[attack_identity]

			if hero.getIdentity() == "Squire" or hero.getIdentity() == "Gallant" or hero.getIdentity() == "Crusader":
				print(f"The {hero.getIdentity()} has been hit by {attack_identity}.....")
				decrease_power = self.RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, beast)
				self.updateHealthPoints(attack_power, hero)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Rook":
				print(f"{hero.getIdentity()} tried to stop {beast.getIdentity()} attack by shield...") 
				print(f"However {beast.getIdentity()} was too fast for {hero.getIdentity()}....!")
				print(f"And thus, {hero.getIdentity()} has been hit by {attack_identity}.....")
				decrease_power = self.RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, beast)
				self.updateHealthPoints(attack_power, hero)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")					

			elif hero.getIdentity() == "Archer" or hero.getIdentity() == "Ranger":
				print(f"The {hero.getIdentity()} tried stopping the attack by another attack. However the attack was missed.....!")
				print(f"And thus, {hero.getIdentity()} has been hit by {attack_identity}.....")
				decrease_power = self.RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, beast)
				self.updateHealthPoints(attack_power, hero)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
		else:
			attack_dict = {"Claw attack": 25, "Claw combat": 30}
			attack_identity = beast.attacks[num - 1]
			attack_power = attack_dict[attack_identity]

			if hero.getIdentity() == "Bishop" or hero.getIdentity() == "Gladiator":
				print(f"The {hero.getIdentity()} tried stopping the attack by another attack.")
				print(f"However some attacks were missed and some were hit.....!")
				print(f"And thus, {hero.getIdentity()} has been hit by {attack_identity}.....")
				print(f"{beast.getIdentity()} was also hit by some attacks of {hero.getIdentity()}")
				decrease_power = self.RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, beast)
				self.updateHealthPoints(attack_power, hero)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
			
			elif hero.getIdentity() == "Musketeer" or hero.getIdentity() == "Thunderer" or hero.getIdentity() == "Wizard":
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				print(f"However the attack has been stopped by another attack.....")
				decrease_power = 0
				if hero.getIdentity() == "Wizard":
					decrease_power = self.RNG.getRandomNumber(80,85)	
				if hero.getIdentity == "Thunderer":
					decrease_power = self.RNG.getRandomNumber(70,75)	
				elif hero.getIdentity() == "Musketeer":
					decrease_power = self.RNG.getRandomNumber(60,65)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Champion":
				random_no = self.RNG.getRandomNumber(0,1)
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				if random_no == 0:
					print(f"However the attack has been countered by shield.....")
				else:
					print(f"However the attack was swiftly dodged by {hero.getIdentity()}....")
				decrease_power = self.RNG.getRandomNumber(75,80)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Knight" or hero.getIdentity() == "Paladin":
				random_no = self.RNG.getRandomNumber(0,2)
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")

				if random_no == 2 and hero.getIdentity() == "Paladin":
					print(f"However the attack has been countered by shield.....")
				elif random_no == 0 or random_no == 2:
					print(f"However the {hero.getIdentity()} dodged it.....")
				elif random_no == 1:
					print(f"However the attack has been countered by sword.....")
				
				decrease_power = self.RNG.getRandomNumber(55,60)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
		
			elif hero.getIdentity() == "Hercules":
				print(f"The {hero.getIdentity()} has barely scratched by {attack_identity}.....")
				print(f"So no damage taken by {hero.getIdentity()}.....")
				decrease_power = self.RNG.getRandomNumber(65,70)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Magical Knight" or hero.getIdentity() == "General":
				random_no = self.RNG.getRandomNumber(0,3)
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				if random_no == 0:
					print(f"However the attack has been blocked by shield.....")
				elif random_no == 1:
					print(f"However the attack has been stopped by sword.....")
				elif random_no == 2:
					print(f"However the attack has been countered by another attack.....")
				else:
					print(f"However the attack was dodged by {hero.getIdentity()}....")

				decrease_power = 0
				if hero.getIdentity() == "Magical Knight":
					decrease_power = self.RNG.getRandomNumber(85,90)
				else:
					decrease_power = self.RNG.getRandomNumber(90,100)
				
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

	def CentaurAttacks(self, hero, beast, num):
		
		if hero.getIdentity() not in beast.getWeakAgainst():
			attack_dict = {"Normal arrow": 40, "Fire arrow": 45, "Thunder arrow": 50, "Blast arrow": 55, "Heat arrow": 60}
			attack_identity = beast.attacks[num - 1]
			attack_power = attack_dict[attack_identity]

			if hero.getIdentity() == "Squire" or hero.getIdentity() == "Gallant" or hero.getIdentity() == "Crusader" or hero.getIdentity() == "Gladiator":
				print(f"The {hero.getIdentity()} has been hit by {attack_identity}.....")
				decrease_power = self.RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, beast)
				self.updateHealthPoints(attack_power, hero)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Rook":
				print(f"{hero.getIdentity()} tried to stop {beast.getIdentity()} attack by shield...") 
				print(f"However {beast.getIdentity()} was too fast for {hero.getIdentity()}....!")
				print(f"And thus, {hero.getIdentity()} has been hit by {attack_identity}.....")
				decrease_power = self.RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, beast)
				self.updateHealthPoints(attack_power, hero)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")					

			elif hero.getIdentity() == "Archer" or hero.getIdentity() == "Ranger" or hero.getIdentity() == "Bishop":
				print(f"The {hero.getIdentity()} tried stopping the attack by another attack. However the attack was missed.....!")
				print(f"And thus, {hero.getIdentity()} has been hit by {attack_identity}.....")
				decrease_power = self.RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, beast)
				self.updateHealthPoints(attack_power, hero)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
		else:
			attack_dict = {"Normal arrow": 20, "Fire arrow": 25, "Thunder arrow": 30, "Blast arrow": 35, "Heat arrow": 40}
			attack_identity = beast.attacks[num - 1]
			attack_power = attack_dict[attack_identity]

			if hero.getIdentity() == "Knight" or hero.getIdentity() == " Paladin" or hero.getIdentity() == "Musketeer":
				print(f"The {hero.getIdentity()} tried stopping the attack by another attack.")
				print(f"However some attacks were missed and some were hit.....!")
				print(f"And thus, {hero.getIdentity()} has been hit by {attack_identity}.....")
				print(f"{beast.getIdentity()} was also hit by some attacks of {hero.getIdentity()}")
				decrease_power = self.RNG.getRandomNumber(20,40)
				self.updateHealthPoints(decrease_power, beast)
				self.updateHealthPoints(attack_power, hero)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Champion":
				random_no = self.RNG.getRandomNumber(0,1)
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				if attack_identity == "Heat arrow":
					print(f"However the attack has been countered by sword....")
				else:
					if random_no == 0:
						print(f"However the attack has been countered by shield.....")
					else:
						print(f"However the attack was swiftly dodged by {hero.getIdentity()}....")
				decrease_power = self.RNG.getRandomNumber(75,80)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Hercules":
				print(f"The {hero.getIdentity()} has been hit by {attack_identity}.....")
				print(f"However {hero.getIdentity()} hasn't taken that much damage....!")
				print(f"So no damage taken by {hero.getIdentity()}.....")
				self.updateHealthPoints(attack_power, hero)
				decrease_power = self.RNG.getRandomNumber(65,70)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Magical Knight" or hero.getIdentity() == "General":
				random_no = self.RNG.getRandomNumber(0,3)
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				if attack_identity == "Heat arrow":
					print(f"However the attack was countered by sword")
				else:
					if random_no == 0:
						print(f"However the attack has been blocked by shield.....")
					elif random_no == 1:
						print(f"However the attack has been stopped by sword.....")
					elif random_no == 2:
						print(f"However the attack has been countered by another attack.....")
					else:
						print(f"However the attack was dodged by {hero.getIdentity()}....")

				decrease_power = 0
				if hero.getIdentity() == "Magical Knight":
					decrease_power = self.RNG.getRandomNumber(85,90)
				else:
					decrease_power = self.RNG.getRandomNumber(90,100)
				
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")


	def GiantAttacks(self, hero, beast, num):
		if hero.getIdentity() not in beast.getWeakAgainst():
			attack_dict = {"Tackle": 50, "Intercept": 55, "Throw rocks": 60, "Close combat": 65}
			attack_identity = beast.attacks[num - 1]
			attack_power = attack_dict[attack_identity]

			if hero.getIdentity() == "Squire" or hero.getIdentity() == "Gallant" or hero.getIdentity() == "Crusader" or hero.getIdentity() == "Gladiator":
				print(f"The {hero.getIdentity()} has been hit by {attack_identity}.....")
				decrease_power = self.RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, beast)
				self.updateHealthPoints(attack_power, hero)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Rook":
				print(f"{hero.getIdentity()} tried to stop {beast.getIdentity()} attack by shield...") 
				print(f"However {beast.getIdentity()} smashed his {attack_identity} through his shield....!")
				print(f"And thus, {hero.getIdentity()} has been hit by {attack_identity}.....")
				decrease_power = self.RNG.getRandomNumber(30,35)
				self.updateHealthPoints(decrease_power, beast)
				self.updateHealthPoints(attack_power, hero)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Archer" or hero.getIdentity() == "Ranger" or hero.getIdentity() == "Bishop":
				print(f"The {hero.getIdentity()} tried stopping the attack by another attack. However the attack was missed.....!")
				print(f"And thus, {hero.getIdentity()} has been hit by {attack_identity}.....")
				decrease_power = self.RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, beast)
				self.updateHealthPoints(attack_power, hero)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
		else:
			attack_dict = {"Tackle": 20, "Intercept": 25, "Throw rocks": 30, "Close combat": 35}
			attack_identity = beast.attacks[num - 1]
			attack_power = attack_dict[attack_identity]

			if hero.getIdentity() == "Gladiator" or hero.getIdentity() == "Hercules":
				print(f"The {hero.getIdentity()} tried stopping the attack by another attack.")
				print(f"However some attacks were missed and some were hit.....!")
				print(f"And thus, {hero.getIdentity()} has been hit by {attack_identity}.....")
				print(f"{beast.getIdentity()} was also hit by some attacks of {hero.getIdentity()}")
				decrease_power = self.RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, beast)
				self.updateHealthPoints(attack_power, hero)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Musketeer" or hero.getIdentity() == "Thunderer" or hero.getIdentity() == "Wizard":
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				print(f"However the attack has been stopped by another attack.....")
				decrease_power = 0
				if hero.getIdentity() == "Wizard":
					decrease_power = self.RNG.getRandomNumber(80,85)	
				if hero.getIdentity == "Thunderer":
					decrease_power = self.RNG.getRandomNumber(70,75)	
				elif hero.getIdentity() == "Musketeer":
					decrease_power = self.RNG.getRandomNumber(60,65)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Champion":
				random_no = self.RNG.getRandomNumber(0,1)
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				if random_no == 0:
					print(f"However the attack has been countered by shield.....")
				else:
					print(f"However the attack was swiftly dodged by {hero.getIdentity()}....")
				decrease_power = self.RNG.getRandomNumber(75,80)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Knight" or hero.getIdentity() == "Paladin":
				random_no = self.RNG.getRandomNumber(0,2)
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")

				if random_no == 2 and hero.getIdentity() == "Paladin":
					print(f"However the attack has been countered by shield.....")
				elif random_no == 0 or random_no == 2:
					print(f"However the {hero.getIdentity()} dodged it.....")
				elif random_no == 1:
					print(f"However the attack has been countered by sword.....")
				
				decrease_power = self.RNG.getRandomNumber(55,60)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
		
			elif hero.getIdentity() == "Magical Knight" or hero.getIdentity() == "General":
				random_no = self.RNG.getRandomNumber(0,3)
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				if random_no == 0:
					print(f"However the attack has been blocked by shield.....")
				elif random_no == 1:
					print(f"However the attack has been stopped by sword.....")
				elif random_no == 2:
					print(f"However the attack has been countered by another attack.....")
				else:
					print(f"However the attack was dodged by {hero.getIdentity()}....")

				decrease_power = 0
				if hero.getIdentity() == "Magical Knight":
					decrease_power = self.RNG.getRandomNumber(85,90)
				else:
					decrease_power = self.RNG.getRandomNumber(90,100)
				
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

	def WitchAttacks(self, hero, beast, num):
		if hero.getIdentity() not in beast.getWeakAgainst():
			attack_dict = {"Fire spell": 55, "Wind spell": 60, "Water spell": 65, "Thunder spell": 70, "Plant spell": 75, "Fire blast": 80}
			attack_identity = beast.attacks[num - 1]
			attack_power = attack_dict[attack_identity]

			if hero.getIdentity() == "Squire" or hero.getIdentity() == "Gallant" or hero.getIdentity() == "Crusader" or hero.getIdentity() == "Gladiator":
				print(f"The {hero.getIdentity()} has been hit by {attack_identity}.....")
				decrease_power = self.RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, beast)
				self.updateHealthPoints(attack_power, hero)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Rook" or hero.getIdentity() == "Knight" or hero.getIdentity() == "Paladin" or hero.getIdentity() == "Hercules":
				print(f"{hero.getIdentity()} tried to stop {beast.getIdentity()} attack by shield...") 
				print(f"However {beast.getIdentity()} was too fast for {hero.getIdentity()}....!")
				print(f"And thus, {hero.getIdentity()} has been hit by {attack_identity}.....")
				decrease_power = self.RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, beast)
				self.updateHealthPoints(attack_power, hero)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")					

			elif hero.getIdentity() == "Archer" or hero.getIdentity() == "Ranger" or hero.getIdentity() == "Bishop":
				print(f"The {hero.getIdentity()} tried stopping the attack by another attack. However the attack was missed.....!")
				print(f"And thus, {hero.getIdentity()} has been hit by {attack_identity}.....")
				decrease_power = self.RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, beast)
				self.updateHealthPoints(attack_power, hero)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
		else:
			attack_dict = {"Fire spell": 25, "Wind spell": 30, "Water spell": 35, "Thunder spell": 40, "Plant spell": 45, "Fire blast": 50}
			attack_identity = beast.attacks[num - 1]
			attack_power = attack_dict[attack_identity]

			if hero.getIdentity() == "Musketeer":
				print(f"The {hero.getIdentity()} tried stopping the attack by another attack.")
				print(f"However some attacks were missed and some were hit.....!")
				print(f"And thus, {hero.getIdentity()} has been hit by {attack_identity}.....")
				print(f"{beast.getIdentity()} was also hit by some attacks of {hero.getIdentity()}")
				decrease_power = self.RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, beast)
				self.updateHealthPoints(attack_power, hero)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Champion":
				random_no = self.RNG.getRandomNumber(0,1)
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				if random_no == 0:
					print(f"However the attack has been countered by shield.....")
				else:
					print(f"However the attack was swiftly dodged by {hero.getIdentity()}....")
				decrease_power = RNG.getRandomNumber(75,80)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Thunderer" or hero.getIdentity() == "Wizard":
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				print(f"However the attack has been stopped by another attack.....")
				decrease_power = 0
				if hero.getIdentity() == "Wizard":
					decrease_power = self.RNG.getRandomNumber(80,85)	
				if hero.getIdentity == "Thunderer":
					decrease_power = self.RNG.getRandomNumber(70,75)	
				elif hero.getIdentity() == "Musketeer":
					decrease_power = self.RNG.getRandomNumber(60,65)
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			elif hero.getIdentity() == "Magical Knight" or hero.getIdentity() == "General":
				random_no = self.RNG.getRandomNumber(0,3)
				print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
				if random_no == 0:
					print(f"However the attack has been blocked by shield.....")
				elif random_no == 1:
					print(f"However the attack has been stopped by sword.....")
				elif random_no == 2:
					print(f"However the attack has been countered by another attack.....")
				else:
					print(f"However the attack was dodged by {hero.getIdentity()}....")

				decrease_power = 0
				if hero.getIdentity() == "Magical Knight":
					decrease_power = self.RNG.getRandomNumber(85,90)
				else:
					decrease_power = self.RNG.getRandomNumber(90,100)
				
				self.updateHealthPoints(decrease_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

	def DragonAttacks(self, hero, beast, num):
		pass

	def SuccubusAttacks(self, hero, beast, num):
		pass

	def VampireAttacks(self, hero, beast, num):
		pass

	def PhoenixAttacks(self, hero, beast, num):
		pass

	def CatSpiritAttacks(self, hero, beast, num):
		pass

	def WendigoAttacks(self, hero, beast, num):
		pass

	def GriffinAttacks(self, hero, beast, num):
		pass
	
	def updateHealthPoints(self, attack_power, creature):
		if creature.getHealthPoints() - attack_power <= 0:
			creature.setHealthPoints(0)
		else:	
			creature.setHealthPoints(creature.getHealthPoints() - attack_power)
