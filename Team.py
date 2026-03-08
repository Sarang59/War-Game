from RandomNumberGenerator import RandomNumberGenerator 
from Creature import Creature 

class Team:

	def __init__(self):
		self.team = {}
	
	def getCreatureDict(self):
		return self.team

	def setCreatureDict(self, team):
		self.team = team

	def createTeam(self, number, flag):
		creature_team = Team()
		if flag:
			randomNumList = []
			for _ in range(int(number)):
				creature = creature_team.getRandomCreature(randomNumList, flag)
				creature_team.team[creature.getIdentity().upper()] = creature
		else:
			randomNumList = []
			for _ in range(int(number)):
				creature = creature_team.getRandomCreature(randomNumList, flag)
				creature_team.team[creature.getIdentity().upper()] = creature

		return creature_team.team

	def getRandomCreature(self, randomNumList, flag):
		heros_list = ["Ranger", "Squire", "Archer", "Rook", "Gallant", "Crusader", "Bishop", "Knight", "Gladiator", "Paladin", "Musketeer", "Hercules", "Thunderer", "Champion", "Wizard", "Magical Knight", "General"]
		heros_dict = {"Ranger": [300, "Why me....!", "Zehahaha", "Slingshot", 
								["Dwarf", "Werewolf", "Minotaur", "Cerberus", "Centaur", "Giant", "Witch", "Dragon", "Vampire", "Phoenix", "Cat Spirit", "Wendigo", "Griffin"], 
								["Wood shot", "Bullet shot"]],
					  "Squire": [350, "Damn you...!", "Darishishishi", "Spear", 
					  			["Goblin", "Elf", "Dwarf", "Werewolf", "Minotaur", "Cerberus", "Centaur", "Giant", "Witch", "Dragon", "Vampire", "Phoenix", "Cat Spirit", "Wendigo", "Griffin"],
					  			["Spear combat", "Spear attack"]],
					  "Archer": [400, "Damn, I lost...!", "Rorororo", "Bow and Arrows", 
					  			["Dwarf", "Werewolf", "Minotaur", "Cerberus", "Giant", "Witch", "Dragon", "Vampire", "Phoenix", "Cat Spirit", "Wendigo", "Griffin"],
					  			["Arrow attack"]],
					  "Gallant": [450, "You got lucky this time...!", "Hihihihihihi", "Two Daggers", 
					  			 ["Werewolf", "Minotaur", "Cerberus", "Centaur", "Giant", "Witch", "Dragon", "Vampire", "Phoenix", "Cat Spirit", "Wendigo", "Griffin"],
					  			 ["Dagger attack", "Dagger combat"]],
					  "Crusader": [500, "Next time I will win...!", "Shishishishishi", "Two Axes", 
					  			   ["Werewolf", "Minotaur", "Cerberus", "Centaur", "Giant", "Witch", "Dragon", "Vampire", "Phoenix", "Cat Spirit", "Wendigo", "Griffin"],
					  			   ["Axe attack", "Axe combat"]],
					  "Rook": [550, "Sorry, my Sire...!", "Hahahaha", "Sword and Shield", 
					  		  ["Minotaur", "Cerberus", "Centaur", "Giant", "Witch", "Dragon", "Vampire", "Phoenix", "Cat Spirit", "Wendigo", "Griffin"],
					  		  ["Sword attack", "Shield attack", "Sword combat"]],
					  "Bishop": [600, "Zoinks, I am dead...!", "Gyagagagagaga", "Magic Staff", 
					  			["Minotaur", "Cerberus", "Centaur", "Giant", "Witch", "Dragon", "Vampire", "Phoenix", "Cat Spirit", "Wendigo", "Griffin"],
					  			["Fire shot", "Water shot", "Plant shot", "Thunder shot"]],
					  "Knight": [650, "Damn it all....!", "Khobababababa", "Sword, shield and Horse",
					  			["Centaur", "Giant", "Witch", "Dragon", "Vampire", "Phoenix", "Cat Spirit", "Wendigo", "Griffin"],
					  			["Sword attack", "Sword combat", "Tackle by horse"]],
					  "Gladiator": [700, "I will get you next time....!", "Tokhakhakhakha", "A Hammer",
					  			   ["Werewolf", "Centaur", "Giant", "Witch", "Dragon", "Vampire", "Phoenix", "Cat Spirit", "Wendigo", "Griffin"],
					  			   ["Hammer attack", "Hammer combat"]],
					  "Paladin": [750, "You knuckle head, next time I will make sure you will loose...!", "Palolololololo",
					  			 ["Centaur", "Giant", "Witch", "Dragon", "Vampire", "Phoenix", "Cat Spirit", "Wendigo", "Griffin"],
					  			 ["Sword attack", "Shield attack", "Sword combat", "Tackle by horse"]],
					  "Musketeer": [800, "I won't forget you....!", "Mushashashasha", "Crossbow and Magic",
					  			   ["Centaur", "Giant", "Witch", "Dragon", "Vampire", "Phoenix", "Cat Spirit", "Wendigo", "Griffin"],
					  			   ["Fire arrow", "Thunder arrow", "Normal arrow", "Blast arrow", "Heat arrow"]],
					  "Hercules": [850, "I won't be defeated that easily next time....!", "Herorororo", "Super Strong",
					  			  ["Dragon", "Vampire", "Phoenix", "Cat Spirit", "Wendigo", "Griffin"],
					  			  ["Tackle", "Intercept", "Throw rocks", "Close combat"]],
					  "Thunderer": [900, "Looser, I won't give up next time...!", "Thuyoyoyoyoyo", "Fast and thunder magic",
					  			   ["Giant", "Dragon", "Cat Spirit", "Wendigo", "Griffin"],
					  			   ["Thunder arrow", "Thunder laser", "Thunder storm", "Thunder bolt", "Volt tackle", "Thunder ball"]],
					  "Champion": [950, "What the Heck...!", "Chamomomomomo", "Swordsman, shield and fast",
					  			  ["Witch", "Cat Spirit", "Wendigo", "Griffin"],
					  			  ["Sword attack", "Sword combat", "Shield attack", "Sword dance", "Sword play"]],
					  "Wizard": [1000, "What just happened....!", "Wihohohohoho", "Wand and all types of magic",
					  			["Griffin", "Wendigo"], 
					  			["Fire spell", "Wind spell", "Water spell", "Thunder spell", "Plant spell", "Fire blast", "Thunder storm", "Electric spell", "Heat storm", "Nightmare"]],
					  "Magical Knight": [1050, "I will get my revenge next time...!", "Makikikikikiki", "Magic, Sword, Shield, Fast",
					  					["Griffin"],
					  					["Sword attack", "Shield attack", "Sword combat", "Fire spell", "Wind spell", "Water spell", "Thunder spell", "Plant spell", "Fire blast", "Thunder storm", "Electric spell", "Tornado"]],
					  "General": [1500, "Impossible, I can't be defeated", "Gehahahahahaha", "All rounder (Sword, Shield, Super strong and Magic)",
					  			 ["Griffin"],
					  			 ["Sword attack", "Electric sword attack", "Fire sword attack", "Sword combat", "Shield attack", "Fire spell", "Wind spell", "Water spell", "Thunder spell", "Plant spell", "Fire blast", "Thunder storm", "Electric spell", "Heat storm", "Fire storm"]]
					  }

		beasts_list = ["Orc", "Goblin", "Elf", "Dwarf", "Werewolf", "Minotaur", "Cerberus", "Giant", "Centaur", "Witch", "Dragon", "Succubus", "Vampire", "Phoenix", "Cat Spirit", "Wendigo", "Griffin"]
		beasts_dict = {"Orc": [200, "But Why....!", "Kabababababa", "Sword", 
							  ["Ranger", "Squire", "Archer", "Gallant", "Berserker", "Rook", "Bishop", "Knight", "Paladin", "Gladiator", "Musketeer", "Hercules", "Thunderer", "Champion", "Wizard", "General"],
							  ["Sword attack"]],
					  "Goblin": [250, "Jeepers...!", "Shahahahaha", "Slingshot", 
					  			["Ranger", "Archer", "Gallant", "Berserker", "Rook", "Bishop", "Knight", "Paladin", "Gladiator", "Musketeer", "Hercules", "Thunderer", "Champion", "Wizard", "General"],
					  			["Wood shot","Bullet shot"]],
					  "Elf": [300, "What the Hell...!", "Mohahahahaha", "Spear", 
					  		 ["Squire", "Archer", "Gallant", "Berserker", "Rook", "Bishop", "Knight", "Paladin", "Gladiator", "Musketeer", "Hercules", "Thunderer", "Champion", "Wizard", "General"],
					  		 ["Spear attack", "Spear combat"]],
					  "Dwarf": [350, "Please forgive me, King...!", "Gerogerogerogero", "Axe", 
					  		   ["Gallant", "Berserker", "Rook", "Bishop", "Knight", "Paladin", "Gladiator", "Musketeer", "Hercules", "Thunderer", "Champion", "Wizard", "General"],
					  		   ["Axe attack", "Axe combat"]],
					  "Werewolf": [400, "Alas...!", "Weehahahahaha", "Hammer", 
					  			  ["Rook", "Bishop", "Knight", "Paladin", "Gladiator", "Musketeer", "Hercules", "Thunderer", "Champion", "Wizard", "General"],
					  			  ["Hammer attack", "Hammer combat"]],
					  "Minotaur": [450, "You won this time, Damn...!", "Gurararara", "Sword and shield", 
					  			  ["Rook", "Bishop", "Knight", "Paladin", "Gladiator", "Musketeer", "Hercules", "Thunderer", "Champion", "Wizard", "General"],
					  			  ["Sword attack", "Shield attack", "Sword combat"]],
					  "Cerberus": [500, "Next time won't be Easy...!", "Pupupupupupupu", "Claws and agility", 
					  			  ["Bishop", "Knight", "Paladin", "Gladiator", "Musketeer", "Hercules", "Thunderer", "Champion", "Wizard", "General"],
					  			  ["Claw attack", "Claw combat"]],
					  "Centaur": [550, "Next time my arrows won't miss....!", "Serororororo", "Bow, arrows and agility",
					  			 ["Knight", "Paladin", "Musketeer", "Hercules", "Thunderer", "Champion", "Wizard", "General"],
					  			 ["Fire arrow", "Thunder arrow", "Normal arrow", "Blast arrow", "Heat arrow"]],
					  "Giant": [600, "I won't forget this Humiliation...!", "Gisasasasasa", "Super strong",
					  		   ["Knight", "Gladiator", "Musketeer", "Hercules", "Thunderer", "Champion", "Wizard", "General"],
					  		   ["Tackle", "Intercept", "Throw rocks", "Close combat"]],
					  "Witch": [650, "Jinkis....!", "Wihihihihihi", "Magic, Wand, fly on broom",
					  		   ["General", "Magical Knight", "Wizard", "Thunderer", "Champion", "Musketeer"],
					  		   ["Fire spell", "Wind spell", "Water spell", "Thunder spell", "Plant spell", "Fire blast"]],
					  "Dragon": [700, "How can I be defeated, the great Dragon...?", "Dagogogogogogo", "",
					  			["General", "Magical Knight", "Wizard", "Thunderer"],
					  			["Fire breath", "Fire blast", "Fire furnace", "Eruption", "Fire storm"]],
					  "Succubus": [750, "You bloody fool, look what have you done...!", "Sulalalalalala", "Dream magic, Charm magic, can fly",
					  			  ["General", "Magical Knight", "Wizard", "Thunderer", "Champion", "Hercules"],
					  			  ["Charm opponent", "Dream eater", "Sleep spell", "Dark Void"]],
					  "Vampire": [800, "Don't let me catch you in the dark Shadows...!", "Vapipipipipipi", "Use magic and transformation to bat",
					  			 ["General", "Magical Knight", "Wizard", "Thunderer"],
					  			 ["Curse", "Shadow sneak", "Night shade", "Shadow ball", "Ominious wind", "Sonic waves"]],
					  "Phoenix": [850, "I accept my defeat...!", "Phiphiphiphiphi", "Use magic and can fly",
					  			 ["General", "Magical Knight"],
					  			 ["Fire breath", "Fire blast", "Fire furnace", "Fire spin", "Inferno", "Heat storm"]],
					  "Cat Spirit": [900, "I will catch you in the after life...!", "Casasasasasasa", "Cat claws, Use magic and Super strong",
					  				["General", "Magical Knight", "Wizard"],
					  				["Claw attack", "Claw combat", "Fire breath", "Tackle", "Intercept", "Close combat", "Wind spell", "Water spell"]],
					  "Wendigo": [950, "I will be sure to pierce your heart next time...!", "Weegogogogogo", "Sword and use magic",
					  			 ["General, Magical Knight"],
					  			 ["Sword attack", "Sword combat", "Shield attack", "Ice spell", "Ice age", "Icicle wind", "Aurora laser"]],
					  "Griffin": [1250, "The great lord of beast won't die that easily next time...!", "Grifififififi", "Use magic, Super strong and can fly",
					  			 ["General"],
					  			 ["Tackle", "Intercept", "Close combat", "Fire spin", "Shadow claw", "Fire spell", "Wind spell", "Water spell", "Thunder spell", "Plant spell", "Fire blast", "Thunder storm", "Electric spell", "Tornado", "Heat storm"]]
					  }

		RNG = RandomNumberGenerator()
		randomNumber = RNG.getRandomNumber(0,16)
		creature_added = False
		creature = Creature()
		
		while(not creature_added):
			if(randomNumber not in randomNumList):		
				randomNumList.append(randomNumber)

				identity = "Unknown"
				characteristics = []
				if flag:
					identity = heros_list[randomNumber]
					characteristics = heros_dict[identity]
				else:
					identity = beasts_list[randomNumber]
					characteristics = beasts_dict[identity]
			
				health_points = characteristics[0]
				cry = characteristics[1]
				laugh = characteristics[2]
				alive = True
				weapon = characteristics[3]
				creature = Creature(health_points, identity, cry, laugh, alive, weapon)
				creature.setWeakAgainst(characteristics[4])
				creature.setAttacks(characteristics[5])
				creature_added = True
			else:
				randomNumber = RNG.getRandomNumber(0,16)
				
		return creature

	def __str__(self):
		result = ""
		for key in self.team:
			result +=str(self.team[key])+"\n"
		return result

if __name__ == "__main__":
	team = Team()
	
	num = input("With how many players you want to play on each side: ")
	heros_team = team.createTeam(num, True)
	beasts_team = team.createTeam(num, False)

	for key in heros_team:
		print(heros_team[key])

	for key in beasts_team:
		print(beasts_team[key])

