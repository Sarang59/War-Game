from RandomNumberGenerator import RandomNumberGenerator 
from Creature import Creature
from Team import Team
from HerosAttack import HerosAttack
from BeastsAttack import BeastsAttack

class War:
	team = Team()

	def __init__(self):
		self.team = self.team
		self.beasts_attacks = BeastsAttack()
	
	def getHerosTeam(self, heros_team):
		result = ""
		for key in heros_team:
			if heros_team[key].getAlive():
				result +=f"{heros_team[key].getIdentity()} \t\t Alive\n"
			else:
				result +=f"{heros_team[key].getIdentity()} \t\t Dead\n"
		result += "\n"
		return result

	def getBeastsTeam(self, beasts_team):
		result = ""
		for key in beasts_team:
			if beasts_team[key].getAlive():
				result +=f"{beasts_team[key].getIdentity()} \t Alive\n"
			else:
				result +=f"{beasts_team[key].getIdentity()} \t Dead\n"
		result += "\n"
		return result

	def startWar(self):
		war_break = True
		
		while war_break:
			print("\n**********MENU**********")
			print("1. Start the Fight")
			print("2. Exit")
			choice = int(input("Please make your choice: "))

			if choice == 1:
				print("\n--------------------------------------------------------------------------")
				team_defeated = False
				war = War()

				num = input("Please enter how many players should be there on both teams: ")
				heros_team = war.team.createTeam(num, True)
				beasts_team = war.team.createTeam(num, False)

				print("\nHeros Team:\n--------------------------------------------------------------------------")
				for key in heros_team:
					print(heros_team[key])
				print("\nBeasts Team:\n--------------------------------------------------------------------------")
				for key in beasts_team:
					print(beasts_team[key])
				
				cnt = 1
				while(not team_defeated):
					print(f"Round {cnt} begin: ")
					print(f"--------------------------------------------------------------------------")

					print(self.getHerosTeam(heros_team))
					hero_selected = False
					while(not hero_selected):
						hero_name = input("Please enter hero's name who will fight: ")
						if(hero_name.upper() not in heros_team or not heros_team[hero_name.upper()].getAlive()):
							print("--------------------------------------------------------------------------")
							print("Please re-enter hero's name who will fight: ")
						else:
							hero_selected = True
					hero = heros_team[hero_name.upper()]
					print("--------------------------------------------------------------------------")

					print(self.getBeastsTeam(beasts_team))
					beast_selected = False
					while(not beast_selected):
						beast_name = input("Please enter beast's name who will fight: ")
						if(beast_name.upper() not in beasts_team or not beasts_team[beast_name.upper()].getAlive()):
							print("--------------------------------------------------------------------------")
							print("Please re-enter beast's name who will fight: ")
						else:
							beast_selected = True
					beast = beasts_team[beast_name.upper()]
					print("--------------------------------------------------------------------------")

					self.beginTheFight(hero, beast)

					heros_team_health_points = 0
					for key in heros_team:
						heros_team_health_points += heros_team[key].getHealthPoints()
					if heros_team_health_points == 0:
						team_defeated = True
						print("--------------------------------------------------------------------------")
						print(f"The hero's team has been defeated....!")
						print(f"The beast's team has conquered victory over hero's team.....!")
						print(f"The Current ruler of the Kingdom is Demon King.....!")

					beasts_team_health_points = 0
					for key in beasts_team:
						beasts_team_health_points += beasts_team[key].getHealthPoints()
					if beasts_team_health_points == 0:
						team_defeated == True
						print("--------------------------------------------------------------------------")
						print(f"The beast's team has been defeated....!")
						print(f"The hero's team has conquered victory over beast's team.....!")
						print(f"The Current ruler of the Kingdom is King.....!")

					cnt += 1
					print("--------------------------------------------------------------------------")
				
			else:
				war_break = False

	def beginTheFight(self, hero, beast):
		RNG = RandomNumberGenerator()
		randomNumber = RNG.getRandomNumber(0,1)

		creature_dead = False
		attack_flag = True
		cnt = 1	
		while(not creature_dead):
			print("\n--------------------------------------------------------------------------")
			print("Clash ", cnt)
			if randomNumber == 0 and cnt == 1:
				print(f"{hero.getIdentity()} attacks first.....")
				self.attackTheBeast(hero, beast)
				attack_flag = False

			elif randomNumber == 1 and cnt == 1:
				print(f"{beast.getIdentity()} attacks first.....")
				self.attackTheHero(hero, beast)
				attack_flag = True
				
			elif attack_flag:
				print(f"Now {hero.getIdentity()} attacks.....")
				self.attackTheBeast(hero, beast)
				attack_flag = False
				
			else:
				print(f"Now {beast.getIdentity()} attacks......")
				self.attackTheHero(hero, beast)
				attack_flag = True

			if hero.getHealthPoints() == 0 and beast.getHealthPoints() == 0:
				print("--------------------------------------------------------------------------")
				print(f"The {beast.getIdentity()} and {hero.getIdentity()} both are dead")
				random = RNG.getRandomNumber(0, 1)
				if random == 0:
					print(f"This round results in a draw....!")
				else:
					print(f"This round results in a tie....!")
				hero.setAlive(False)
				beast.setAlive(False)
				creature_dead = True
			elif hero.getHealthPoints() == 0:
				print("--------------------------------------------------------------------------")
				print(f"The {beast.getIdentity()} laughs {beast.getLaugh()}")
				print(f"The {hero.getIdentity()} cries {hero.getCry()}")
				hero.setAlive(False)
				creature_dead = True
			elif beast.getHealthPoints() == 0:
				print("--------------------------------------------------------------------------")
				print(f"The {hero.getIdentity()} laughs {hero.getLaugh()}")
				print(f"The {beast.getIdentity()} cries {beast.getCry()}")
				beast.setAlive(False)
				creature_dead = True
			
			cnt += 1

	def getProperString(self, lst: list) -> str:
		result = ""
		cnt = 1
		for item in lst:
			result +=str(cnt)+". "+item+"\n"
			cnt += 1
		return result

	def attackTheBeast(self, hero, beast):
		RNG = RandomNumberGenerator()
		
		print(f"\n{self.getProperString(hero.attacks)}")
		num = int(input("Please enter attack number from list of attacks: "))
		print("--------------------------------------------------------------------------")
						
		if hero.getIdentity() == "Ranger":
			if beast.getIdentity() not in hero.getWeakAgainst():
				attack_dict = {"Wood shot" : 30, "Bullet shot" : 60}
				attack_identity = hero.attacks[num - 1]
				attack_power = attack_dict[attack_identity]
				
				if beast.getIdentity() == "Orc" or beast.getIdentity() == "Goblin" or beast.getIdentity() == "Elf":
					print(f"The {beast.getIdentity()} has been hit by {attack_identity}.....")
					decrease_power = RNG.getRandomNumber(25,30)
					self.updateHealthPoints(decrease_power, hero)
					self.updateHealthPoints(attack_power, beast)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
					
			else:
				attack_dict = {"Wood shot" : 15, "Bullet shot" : 20}
				attack_identity = hero.attacks[num - 1]
				attack_power = attack_dict[attack_identity]

				if beast.getIdentity() == "Dwarf" or beast.getIdentity() == "Werewolf":
					print(f"The {beast.getIdentity()} has been hit by {attack_identity}.....")
					print(f"However it hasn't taken too much damage.....")
					decrease_power = RNG.getRandomNumber(40,45)
					self.updateHealthPoints(decrease_power, hero)
					self.updateHealthPoints(attack_power, beast)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Minotaur":
					print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
					print(f"However the attack has been countered by shield.....")
					decrease_power = RNG.getRandomNumber(50,55)
					self.updateHealthPoints(decrease_power, beast)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
					
				elif beast.getIdentity() == "Cerberus" or beast.getIdentity() == "Centaur":
					print(f"The {beast.getIdentity()} hasn't been hit by {attack_identity}.....")
					print(f"As {beast.getIdentity()} has used agility to dodge it.....")
					decrease_power = 0
					if beast.getIdentity() == "Cerberus":
						decrease_power = RNG.getRandomNumber(50,55)
					else:
						decrease_power = RNG.getRandomNumber(60,65)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Giant":
					print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
					print(f"However the attack had not effect on Giant's humungous body. It barely scratched it.....")
					decrease_power = RNG.getRandomNumber(70,75)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Witch":
					random = RNG.getRandomNumber(0,1)
					if random == 0:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} blocked the {attack_identity} by another attack.....")
						decrease_power = RNG.getRandomNumber(30,35)
						self.updateHealthPoints(decrease_power, beast)
					else:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} flew on broom and has taken no damage at all.....")
					decrease_power = RNG.getRandomNumber(80,85)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Dragon" or beast.getIdentity() == "Phoenix":
					random = RNG.getRandomNumber(0,1)
					if random == 0:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} countered the {attack_identity} by another attack.....")
						decrease_power = RNG.getRandomNumber(30,35)
						self.updateHealthPoints(decrease_power, beast)
					else:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} flew away and has taken no damage at all.....")
					decrease_power = RNG.getRandomNumber(90,95)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Vampire":
					random = RNG.getRandomNumber(0,1)
					if random == 0:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} stopped the {attack_identity} by another attack.....")
						decrease_power = RNG.getRandomNumber(30,35)
						self.updateHealthPoints(decrease_power, beast)
					else:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} transformed into bat and flew away and has taken no damage at all.....")
						decrease_power = RNG.getRandomNumber(40,45)
						self.updateHealthPoints(decrease_power, beast)
					decrease_power = RNG.getRandomNumber(100,105)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Cat Spirit" or beast.getIdentity() == "Wendigo":
					print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
					print(f"However the {beast.getIdentity()} countered the {attack_identity} by another attack.....")
					beast_decrease_power = RNG.getRandomNumber(30,35)
					self.updateHealthPoints(beast_decrease_power, beast)
					hero_decrease_power = RNG.getRandomNumber(100,105)
					self.updateHealthPoints(hero_decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Griffin":
					random = RNG.getRandomNumber(0,1)
					if random == 0:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} stopped the {attack_identity} by another attack.....")
						decrease_power = RNG.getRandomNumber(30,35)
						self.updateHealthPoints(decrease_power, beast)
					else:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} flew away and has taken no damage at all.....")
						decrease_power = RNG.getRandomNumber(20,25)
						self.updateHealthPoints(decrease_power, beast)
					decrease_power = RNG.getRandomNumber(120,125)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
					
		elif hero.getIdentity() == "Squire":
			if beast.getIdentity() not in hero.getWeakAgainst():
				attack_dict = {"Spear combat" : 50, "Spear attack" : 40}
				attack_identity = hero.attacks[num - 1]
				attack_power = attack_dict[attack_identity]

				print(f"The {beast.getIdentity()} has been hit by {attack_identity}.....")
				decrease_power = RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, hero)
				self.updateHealthPoints(attack_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
			else:
				attack_dict = {"Spear combat" : 25, "Spear attack" : 15}
				attack_identity = hero.attacks[num - 1]
				attack_power = attack_dict[attack_identity]
				
				if beast.getIdentity() == "Elf":
					print(f"The {hero.getIdentity()} tried stopping the attack by another attack.")
					print(f"However some attacks were missed and some were hit.....!")
					print(f"And thus, {hero.getIdentity()} has been hit by {attack_identity}.....")
					print(f"{beast.getIdentity()} was also hit by some attacks of {hero.getIdentity()}")
					decrease_power = RNG.getRandomNumber(15,25)
					self.updateHealthPoints(decrease_power, beast)
					self.updateHealthPoints(attack_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Dwarf" or beast.getIdentity() == "Werewolf":
					print(f"The {beast.getIdentity()} has been hit by {attack_identity}.....")
					print(f"However it hasn't taken too much damage.....")
					decrease_power = RNG.getRandomNumber(40,45)
					self.updateHealthPoints(decrease_power, hero)
					self.updateHealthPoints(attack_power, beast)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Minotaur":					
					print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
					print(f"However the attack has been countered by shield.....")
					decrease_power = RNG.getRandomNumber(50,55)
					self.updateHealthPoints(decrease_power, beast)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
					
				elif beast.getIdentity() == "Cerberus" or beast.getIdentity() == "Centaur":
					print(f"The {beast.getIdentity()} hasn't been hit by {attack_identity}.....")
					print(f"As {beast.getIdentity()} has used agility to dodge it.....")
					decrease_power = 0
					if beast.getIdentity() == "Cerberus":
						decrease_power = RNG.getRandomNumber(50,55)
					else:
						decrease_power = RNG.getRandomNumber(60,65)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Giant":
					print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
					print(f"However the attack had not effect on Giant's humungous body. It barely scratched it.....")
					decrease_power = RNG.getRandomNumber(70,75)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Witch":
					random = RNG.getRandomNumber(0,1)
					if random == 0:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} blocked the {attack_identity} by another attack.....")
						decrease_power = RNG.getRandomNumber(30,35)
						self.updateHealthPoints(decrease_power, beast)
					else:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} flew on broom and has taken no damage at all.....")
					decrease_power = RNG.getRandomNumber(80,85)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Dragon" or beast.getIdentity() == "Phoenix":
					random = RNG.getRandomNumber(0,1)
					if random == 0:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} countered the {attack_identity} by another attack.....")
						decrease_power = RNG.getRandomNumber(30,35)
						self.updateHealthPoints(decrease_power, beast)
					else:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} flew away and has taken no damage at all.....")
					decrease_power = RNG.getRandomNumber(90,95)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Vampire":
					random = RNG.getRandomNumber(0,1)
					if random == 0:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} stopped the {attack_identity} by another attack.....")
						decrease_power = RNG.getRandomNumber(30,35)
						self.updateHealthPoints(decrease_power, beast)
					else:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} transformed into bat and flew away and has taken no damage at all.....")
						decrease_power = RNG.getRandomNumber(40,45)
						self.updateHealthPoints(decrease_power, beast)
					decrease_power = RNG.getRandomNumber(100,105)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Cat Spirit" or beast.getIdentity() == "Wendigo":
					print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
					print(f"However the {beast.getIdentity()} countered the {attack_identity} by another attack.....")
					beast_decrease_power = RNG.getRandomNumber(30,35)
					self.updateHealthPoints(beast_decrease_power, beast)
					hero_decrease_power = RNG.getRandomNumber(100,105)
					self.updateHealthPoints(hero_decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Griffin":
					random = RNG.getRandomNumber(0,1)
					if random == 0:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} stopped the {attack_identity} by another attack.....")
						decrease_power = RNG.getRandomNumber(30,35)
						self.updateHealthPoints(decrease_power, beast)
					else:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} flew away and has taken no damage at all.....")
						decrease_power = RNG.getRandomNumber(20,25)
						self.updateHealthPoints(decrease_power, beast)
					decrease_power = RNG.getRandomNumber(120,125)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
				
		elif  hero.getIdentity() == "Archer":
			if beast.getIdentity() not in hero.getWeakAgainst():
				attack_dict = {"Arrow attack" : 40}
				attack_identity = hero.attacks[num - 1]
				attack_power = attack_dict[attack_identity]

				print(f"The {beast.getIdentity()} has been hit by {attack_identity}.....")
				decrease_power = RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, hero)
				self.updateHealthPoints(attack_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

			else:
				attack_dict = {"Arrow attack" : 20}
				attack_identity = hero.attacks[num - 1]
				attack_power = attack_dict[attack_identity]

				if beast.getIdentity() == "Dwarf" or beast.getIdentity() == "Werewolf":
					print(f"The {beast.getIdentity()} has been hit by {attack_identity}.....")
					print(f"However it hasn't taken too much damage.....")
					decrease_power = RNG.getRandomNumber(40,45)
					self.updateHealthPoints(decrease_power, hero)
					self.updateHealthPoints(attack_power, beast)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Minotaur":					
					print(f"The {beast.getIdentity()} hasn't been hit by {attack_identity}.....")
					print(f"However the attack has been countered by shield.....")
					decrease_power = RNG.getRandomNumber(50,55)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
					
				elif beast.getIdentity() == "Cerberus" or beast.getIdentity() == "Centaur":
					print(f"The {beast.getIdentity()} hasn't been hit by {attack_identity}.....")
					print(f"As {beast.getIdentity()} has used agility to dodge it.....")
					decrease_power = 0
					if beast.getIdentity() == "Cerberus":
						decrease_power = RNG.getRandomNumber(50,55)
					else:
						decrease_power = RNG.getRandomNumber(60,65)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Giant":
					print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
					print(f"However the attack had not effect on Giant's humungous body. It barely scratched it.....")
					decrease_power = RNG.getRandomNumber(70,75)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Witch":
					random = RNG.getRandomNumber(0,1)
					if random == 0:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} blocked the {attack_identity} by another attack.....")
						decrease_power = RNG.getRandomNumber(30,35)
						self.updateHealthPoints(decrease_power, beast)
					else:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} flew on broom and has taken no damage at all.....")
					decrease_power = RNG.getRandomNumber(80,85)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Dragon" or beast.getIdentity() == "Phoenix":
					random = RNG.getRandomNumber(0,1)
					if random == 0:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} countered the {attack_identity} by another attack.....")
						decrease_power = RNG.getRandomNumber(30,35)
						self.updateHealthPoints(decrease_power, beast)
					else:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} flew away and has taken no damage at all.....")
					decrease_power = RNG.getRandomNumber(90,95)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Vampire":
					random = RNG.getRandomNumber(0,1)
					if random == 0:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} stopped the {attack_identity} by another attack.....")
						decrease_power = RNG.getRandomNumber(30,35)
						self.updateHealthPoints(decrease_power, beast)
					else:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} transformed into bat and flew away and has taken no damage at all.....")
						decrease_power = RNG.getRandomNumber(40,45)
						self.updateHealthPoints(decrease_power, beast)
					decrease_power = RNG.getRandomNumber(100,105)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Cat Spirit" or beast.getIdentity() == "Wendigo":
					print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
					print(f"However the {beast.getIdentity()} countered the {attack_identity} by another attack.....")
					beast_decrease_power = RNG.getRandomNumber(30,35)
					self.updateHealthPoints(beast_decrease_power, beast)
					hero_decrease_power = RNG.getRandomNumber(100,105)
					self.updateHealthPoints(hero_decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Griffin":
					random = RNG.getRandomNumber(0,1)
					if random == 0:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} stopped the {attack_identity} by another attack.....")
						decrease_power = RNG.getRandomNumber(30,35)
						self.updateHealthPoints(decrease_power, beast)
					else:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} flew away and has taken no damage at all.....")
						decrease_power = RNG.getRandomNumber(20,25)
						self.updateHealthPoints(decrease_power, beast)
					decrease_power = RNG.getRandomNumber(120,125)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
				
		elif hero.getIdentity() == "Gallant":
			if beast.getIdentity() not in hero.getWeakAgainst():
				attack_dict = {"Dagger attack" : 50, "Dagger combat" : 60}
				attack_identity = hero.attacks[num - 1]
				attack_power = attack_dict[attack_identity]

				print(f"The {beast.getIdentity()} has been hit by {attack_identity}.....")
				decrease_power = RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, hero)
				self.updateHealthPoints(attack_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
			else:
				attack_dict = {"Dagger attack" : 25, "Dagger combat" : 30}
				attack_identity = hero.attacks[num - 1]
				attack_power = attack_dict[attack_identity]

				if beast.getIdentity() == "Werewolf":
					print(f"The {beast.getIdentity()} has been hit by {attack_identity}.....")
					print(f"However it hasn't taken too much damage.....")
					decrease_power = RNG.getRandomNumber(40,45)
					self.updateHealthPoints(decrease_power, hero)
					self.updateHealthPoints(attack_power, beast)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Minotaur":					
					print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
					print(f"However the attack has been countered by shield.....")
					decrease_power = RNG.getRandomNumber(50,55)
					self.updateHealthPoints(decrease_power, beast)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
					
				elif beast.getIdentity() == "Cerberus":
					print(f"The {beast.getIdentity()} hasn't been hit by {attack_identity}.....")
					print(f"As {beast.getIdentity()} has used agility to dodge it.....")
					decrease_power = RNG.getRandomNumber(50,55)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

		elif hero.getIdentity() == "Crusader":
			if beast.getIdentity() not in hero.getWeakAgainst():
				attack_dict = {"Axe attack" : 50, "Axe combat" : 60}
				attack_identity = hero.attacks[num - 1]
				attack_power = attack_dict[attack_identity]

				print(f"The {beast.getIdentity()} has been hit by {attack_identity}.....")
				decrease_power = RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, hero)
				self.updateHealthPoints(attack_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
			else:
				attack_dict = {"Axe attack" : 25, "Axe combat" : 30}
				attack_identity = hero.attacks[num - 1]
				attack_power = attack_dict[attack_identity]

				if beast.getIdentity() == "Werewolf":
					print(f"The {beast.getIdentity()} has been hit by {attack_identity}.....")
					print(f"However it hasn't taken too much damage.....")
					decrease_power = RNG.getRandomNumber(40,45)
					self.updateHealthPoints(decrease_power, hero)
					self.updateHealthPoints(attack_power, beast)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Minotaur":					
					print(f"The {beast.getIdentity()} hasn't been hit by {attack_identity}.....")
					print(f"However the attack has been stopped by shield.....")
					decrease_power = RNG.getRandomNumber(50,55)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
					
				elif beast.getIdentity() == "Cerberus" or beast.getIdentity() == "Centaur":
					print(f"The {beast.getIdentity()} hasn't been hit by {attack_identity}.....")
					print(f"As {beast.getIdentity()} has used agility to dodge it.....")
					decrease_power = 0
					if beast.getIdentity() == "Cerberus":
						decrease_power = RNG.getRandomNumber(50,55)
					else:
						decrease_power = RNG.getRandomNumber(60,65)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Giant":
					print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
					print(f"However the attack had not effect on Giant's humungous body. It barely scratched it.....")
					decrease_power = RNG.getRandomNumber(70,75)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Witch":
					random = RNG.getRandomNumber(0,1)
					if random == 0:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} blocked the {attack_identity} by another attack.....")
						decrease_power = RNG.getRandomNumber(30,35)
						self.updateHealthPoints(decrease_power, beast)
					else:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} flew on broom and has taken no damage at all.....")
					decrease_power = RNG.getRandomNumber(80,85)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Dragon" or beast.getIdentity() == "Phoenix":
					random = RNG.getRandomNumber(0,1)
					if random == 0:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} countered the {attack_identity} by another attack.....")
						decrease_power = RNG.getRandomNumber(30,35)
						self.updateHealthPoints(decrease_power, beast)
					else:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} flew away and has taken no damage at all.....")
					decrease_power = RNG.getRandomNumber(90,95)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Vampire":
					random = RNG.getRandomNumber(0,1)
					if random == 0:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} stopped the {attack_identity} by another attack.....")
						decrease_power = RNG.getRandomNumber(30,35)
						self.updateHealthPoints(decrease_power, beast)
					else:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} transformed into bat and flew away and has taken no damage at all.....")
						decrease_power = RNG.getRandomNumber(40,45)
						self.updateHealthPoints(decrease_power, beast)
					decrease_power = RNG.getRandomNumber(100,105)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Cat Spirit" or beast.getIdentity() == "Wendigo":
					print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
					print(f"However the {beast.getIdentity()} countered the {attack_identity} by another attack.....")
					beast_decrease_power = RNG.getRandomNumber(30,35)
					self.updateHealthPoints(beast_decrease_power, beast)
					hero_decrease_power = RNG.getRandomNumber(100,105)
					self.updateHealthPoints(hero_decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Griffin":
					random = RNG.getRandomNumber(0,1)
					if random == 0:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} stopped the {attack_identity} by another attack.....")
						decrease_power = RNG.getRandomNumber(30,35)
						self.updateHealthPoints(decrease_power, beast)
					else:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} flew away and has taken no damage at all.....")
						decrease_power = RNG.getRandomNumber(20,25)
						self.updateHealthPoints(decrease_power, beast)
					decrease_power = RNG.getRandomNumber(120,125)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
				
		elif hero.getIdentity() == "Rook":
			if beast.getIdentity() not in hero.getWeakAgainst():
				attack_dict = {"Sword attack": 50, "Shield attack": 55, "Sword combat": 60}
				attack_identity = hero.attacks[num - 1]
				attack_power = attack_dict[attack_identity]

				print(f"The {beast.getIdentity()} has been hit by {attack_identity}.....")
				decrease_power = RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, hero)
				self.updateHealthPoints(attack_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
			else:
				attack_dict = {"Sword attack": 25, "Shield attack": 30, "Sword combat": 35}
				attack_identity = hero.attacks[num - 1]
				attack_power = attack_dict[attack_identity]

				if beast.getIdentity() == "Minotaur":
					print(f"The {beast.getIdentity()} has been hit by {attack_identity}.....")
					print(f"However it hasn't taken too much damage.....")
					decrease_power = RNG.getRandomNumber(25,35)
					self.updateHealthPoints(decrease_power, hero)
					self.updateHealthPoints(attack_power, beast)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
				
				elif beast.getIdentity() == "Cerberus" or beast.getIdentity() == "Centaur":
					print(f"The {beast.getIdentity()} hasn't been hit by {attack_identity}.....")
					print(f"As {beast.getIdentity()} has used agility to dodge it.....")
					decrease_power = 0
					if beast.getIdentity() == "Cerberus":
						decrease_power = RNG.getRandomNumber(50,55)
					else:
						decrease_power = RNG.getRandomNumber(60,65)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Giant":
					print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
					print(f"However the attack had not effect on Giant's humungous body. It barely scratched it.....")
					decrease_power = RNG.getRandomNumber(70,75)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Witch":
					random = RNG.getRandomNumber(0,1)
					if random == 0:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} blocked the {attack_identity} by another attack.....")
						decrease_power = RNG.getRandomNumber(30,35)
						self.updateHealthPoints(decrease_power, beast)
					else:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} flew on broom and has taken no damage at all.....")
					decrease_power = RNG.getRandomNumber(80,85)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Dragon" or beast.getIdentity() == "Phoenix":
					random = RNG.getRandomNumber(0,1)
					if random == 0:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} countered the {attack_identity} by another attack.....")
						decrease_power = RNG.getRandomNumber(30,35)
						self.updateHealthPoints(decrease_power, beast)
					else:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} flew away and has taken no damage at all.....")
					decrease_power = RNG.getRandomNumber(90,95)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Vampire":
					random = RNG.getRandomNumber(0,1)
					if random == 0:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} stopped the {attack_identity} by another attack.....")
						decrease_power = RNG.getRandomNumber(30,35)
						self.updateHealthPoints(decrease_power, beast)
					else:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} transformed into bat and flew away and has taken no damage at all.....")
						decrease_power = RNG.getRandomNumber(40,45)
						self.updateHealthPoints(decrease_power, beast)
					decrease_power = RNG.getRandomNumber(100,105)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Cat Spirit" or beast.getIdentity() == "Wendigo":
					print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
					print(f"However the {beast.getIdentity()} countered the {attack_identity} by another attack.....")
					beast_decrease_power = RNG.getRandomNumber(30,35)
					self.updateHealthPoints(beast_decrease_power, beast)
					hero_decrease_power = RNG.getRandomNumber(100,105)
					self.updateHealthPoints(hero_decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Griffin":
					random = RNG.getRandomNumber(0,1)
					if random == 0:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} stopped the {attack_identity} by another attack.....")
						decrease_power = RNG.getRandomNumber(30,35)
						self.updateHealthPoints(decrease_power, beast)
					else:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} flew away and has taken no damage at all.....")
						decrease_power = RNG.getRandomNumber(20,25)
						self.updateHealthPoints(decrease_power, beast)
					decrease_power = RNG.getRandomNumber(120,125)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
				
		elif hero.getIdentity() == "Bishop":
			if beast.getIdentity() not in hero.getWeakAgainst():
				attack_dict = {"Fire shot": 50, "Water shot": 50, "Plant shot": 55, "Thunder shot": 60}
				attack_identity = hero.attacks[num - 1]
				attack_power = attack_dict[attack_identity]

				print(f"The {beast.getIdentity()} has been hit by {attack_identity}.....")
				decrease_power = RNG.getRandomNumber(25,30)
				self.updateHealthPoints(decrease_power, hero)
				self.updateHealthPoints(attack_power, beast)
				print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
				print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
			else:
				attack_dict = {"Fire shot": 25, "Water shot": 15, "Plant shot": 30, "Thunder shot": 35}
				attack_identity = hero.attacks[num - 1]
				attack_power = attack_dict[attack_identity]

				if beast.getIdentity() == "Minotaur":
					print(f"The {beast.getIdentity()} has been hit by {attack_identity}.....")
					print(f"However it hasn't taken too much damage.....")
					decrease_power = RNG.getRandomNumber(40,45)
					self.updateHealthPoints(decrease_power, hero)
					self.updateHealthPoints(attack_power, beast)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
				
				elif beast.getIdentity() == "Cerberus":
					print(f"The {beast.getIdentity()} tried stopping the attack by another attack.")
					print(f"However some attacks were missed and some were hit.....!")
					print(f"And thus, {beast.getIdentity()} has been hit by {attack_identity}.....")
					print(f"{hero.getIdentity()} was also hit by some attacks of {beast.getIdentity()}")
					decrease_power = RNG.getRandomNumber(25,30)
					self.updateHealthPoints(decrease_power, beast)
					self.updateHealthPoints(attack_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")
				
				elif beast.getIdentity() == "Centaur":
					print(f"The {beast.getIdentity()} hasn't been hit by {attack_identity}.....")
					print(f"As {beast.getIdentity()} has used agility to dodge it.....")
					decrease_power = RNG.getRandomNumber(60,65)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Giant":
					print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
					print(f"However the attack had not effect on Giant's humungous body. It barely scratched it.....")
					decrease_power = RNG.getRandomNumber(70,75)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Witch":
					random = RNG.getRandomNumber(0,1)
					if random == 0:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} blocked the {attack_identity} by another attack.....")
						decrease_power = RNG.getRandomNumber(30,35)
						self.updateHealthPoints(decrease_power, beast)
					else:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} flew on broom and has taken no damage at all.....")
					decrease_power = RNG.getRandomNumber(80,85)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Dragon" or beast.getIdentity() == "Phoenix":
					random = RNG.getRandomNumber(0,1)
					if random == 0:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} countered the {attack_identity} by another attack.....")
						decrease_power = RNG.getRandomNumber(30,35)
						self.updateHealthPoints(decrease_power, beast)
					else:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} flew away and has taken no damage at all.....")
					decrease_power = RNG.getRandomNumber(90,95)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Vampire":
					random = RNG.getRandomNumber(0,1)
					if random == 0:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} stopped the {attack_identity} by another attack.....")
						decrease_power = RNG.getRandomNumber(30,35)
						self.updateHealthPoints(decrease_power, beast)
					else:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} transformed into bat and flew away and has taken no damage at all.....")
						decrease_power = RNG.getRandomNumber(40,45)
						self.updateHealthPoints(decrease_power, beast)
					decrease_power = RNG.getRandomNumber(100,105)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Cat Spirit" or beast.getIdentity() == "Wendigo":
					print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
					print(f"However the {beast.getIdentity()} countered the {attack_identity} by another attack.....")
					beast_decrease_power = RNG.getRandomNumber(30,35)
					self.updateHealthPoints(beast_decrease_power, beast)
					hero_decrease_power = RNG.getRandomNumber(100,105)
					self.updateHealthPoints(hero_decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

				elif beast.getIdentity() == "Griffin":
					random = RNG.getRandomNumber(0,1)
					if random == 0:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} stopped the {attack_identity} by another attack.....")
						decrease_power = RNG.getRandomNumber(30,35)
						self.updateHealthPoints(decrease_power, beast)
					else:
						print(f"The {hero.getIdentity()} hasn't been hit by {attack_identity}.....")
						print(f"However the {beast.getIdentity()} flew away and has taken no damage at all.....")
						decrease_power = RNG.getRandomNumber(20,25)
						self.updateHealthPoints(decrease_power, beast)
					decrease_power = RNG.getRandomNumber(120,125)
					self.updateHealthPoints(decrease_power, hero)
					print(f"The updated health points of {hero.getIdentity()} are: {hero.getHealthPoints()}")
					print(f"The updated health points of {beast.getIdentity()} are: {beast.getHealthPoints()}")

	def attackTheHero(self, hero, beast):
		RNG = RandomNumberGenerator()
		
		print(f"\n{self.getProperString(beast.attacks)}")
		num = int(input("Please enter attack number from list of attacks: "))
		print("--------------------------------------------------------------------------")

		if beast.getIdentity() == "Orc":
			self.beasts_attacks.OrcAttacks(hero, beast, num)
			
		elif beast.getIdentity() == "Goblin":
			self.beasts_attacks.GoblinAttacks(hero, beast, num)

		elif beast.getIdentity() == "Elf":
			self.beasts_attacks.ElfAttacks(hero, beast, num)

		elif beast.getIdentity() == "Dwarf":
			self.beasts_attacks.DwarfAttacks(hero, beast, num)

		elif beast.getIdentity() == "Werewolf":
			self.beasts_attacks.WerewolfAttacks(hero, beast, num)

		elif beast.getIdentity() == "Minotaur":
			self.beasts_attacks.MinotaurAttacks(hero, beast, num)

		elif beast.getIdentity() == "Cerberus":
			self.beasts_attacks.CerberusAttacks(hero, beast, num)

		elif beast.getIdentity() == "Centaur":
			self.beasts_attacks.CentaurAttacks(hero, beast, num)

		elif beast.getIdentity() == "Giant":
			self.beasts_attacks.GiantAttacks(hero, beast, num)

		elif beast.getIdentity() == "Witch":
			self.beasts_attacks.WitchAttacks(hero, beast, num)

		elif beast.getIdentity() == "Dragon":
			self.beasts_attacks.DragonAttacks(hero, beast, num)

		elif beast.getIdentity() == "Succubus":
			self.beasts_attacks.SuccubusAttacks(hero, beast, num)

		elif beast.getIdentity() == "Vampire":
			self.beasts_attacks.VampireAttacks(hero, beast, num)

		elif beast.getIdentity() == "Phoenix":
			self.beasts_attacks.PhoenixAttacks(hero, beast, num)

		elif beast.getIdentity() == "Cat Spirit":
			self.beasts_attacks.CatSpiritAttacks(hero, beast, num)

		elif beast.getIdentity() == "Wendigo":
			self.beasts_attacks.WendigoAttacks(hero, beast, num)

		elif beast.getIdentity() == "Griffin":
			self.beasts_attacks.GriffinAttacks(hero, beast, num)

	def updateHealthPoints(self, attack_power, creature):
		if creature.getHealthPoints() - attack_power <= 0:
			creature.setHealthPoints(0)
		else:	
			creature.setHealthPoints(creature.getHealthPoints() - attack_power)


if __name__ == "__main__":
	war = War()
	
	war.startWar()

