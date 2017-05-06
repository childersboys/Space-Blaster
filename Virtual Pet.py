import console
from random import randint

# Attributes
Hunger = 0
Thirst = 0
Fatigue = 0
Enjoyment = 0
Age = 0
flag = False

# Randomized things
AnimalTypes = ['eeklor', 'trillinsi', 'plokwei', 'intricose', 'charaldim', 'klonesalp', 'blixerit']
BodyDecor = ['horned', 'spiked', 'shiny', 'glowing', 'icy', 'shadowed', 'time traveling']
detail = BodyDecor[randint(0, 6)]
Body = ['small', 'large', 'giant', 'staggeringly large']
bodysize = Body[randint(0, 3)]
Colors = ['red', 'green', 'blue',
          'purple', 'yellow', 'orange', 'octarine']
scalecolor = Colors[randint(0,6)]
eyecolor = Colors[randint(0,3)]
Sizes = ['tiny', 'small', 'medium',
         'large', 'giant']
scalesize = Sizes[randint(0,4)]


Animal = dict()
Animal['species'] = AnimalTypes[randint(0, 6)]
Animal['hunger'] = 0
Animal['thirst'] = 0
Animal['fatigue'] = 0
Animal['age'] = 0
Animal['happiness'] = 0
Animal['maxage'] = randint(80, 110)
#print(Animal)
#input()

# functions 
def Increment():
	global Animal
	Animal['hunger'] += 1
	Animal['thirst'] += 1
	Animal['fatigue'] += 1
	Animal['happiness'] += 1
	Animal['age'] += 1
	#print(Animal)

def Hungerlevels():
	global Animal
	global flag
	if 0 <= Animal['hunger'] <= 49:
		print('I am not hungry.')
	elif 50 <= Animal['hunger'] <= 89:
		print('I am hungry.')
	elif 90 <= Animal['hunger'] <= 99:
		print('I am starving! Feed me!')
	elif Animal['hunger'] == 100:
		print(Name, 'Starved. ')
		flag = False
		
def Thirstlevels():
	global Animal
	global flag
	if 0 <= Animal['thirst'] <= 49:
		print('I am not thirsty.')
	elif 50 <= Animal['thirst'] <= 89:
		print('I am thirsty.')
	elif 90 <= Animal['thirst'] <= 99:
		print('I am drying up! Give me water!')
	elif Animal['thirst'] == 0:
		print(Name, 'Died. ')
		flag = False

def Fatiguelevels():
	global Animal
	global flag
	if 0 <= Animal['fatigue'] <= 49:
		print('I am not tired.')
	elif 50 <= Animal['fatigue'] <= 89:
		print('I am tired.')
	elif 90 <= Animal['fatigue'] <= 99:
		print('I am about to collapse! Let me sleep!')
	elif Animal['fatigue'] == 100:
		print(Name, 'Died. ')
		flag = False

def Enjoymentlevels():
	global Animal
	global flag
	if 0 <= Animal['happiness'] <= 49:
		print('I am having fun!')
	elif 50 <= Animal['happiness'] <= 89:
		print('I am bored.')
	elif 90 <= Animal['happiness'] <= 99:
		print('I will run away soon! Give me something to do!')
	elif Animal['happiness'] == 100:
		print(Name, 'Ran Away. ')
		flag = False
		
def food():
	global Animal
	print('He ate the food. ')
	Animal['hunger'] -= 2
	
def water():
	global Animal
	print('He drank the water. ')
	Animal['thirst'] -= 2
	
def tiredness():
	global Animal
	print('He took a nap. ')
	Animal['fatigue'] -= 2
	
def Play():
	global Animal
	print('He is happy to play. ')
	Animal['happiness'] -= 2

def prepare():
  global Name
  console.set_font('Academy Engraved LET', 16)
  console.set_color(.23, 1.0, .45)
  Name = input('Name your pet! ')
  console.set_color(.0, .86, 1.2)
  console.set_font('Academy Engraved LET', 16)

# run it
prepare()
console.clear()
console.set_color(.23, 1.0, .45)

def Status():
	Hungerlevels()
	Thirstlevels()
	Fatiguelevels()
	Enjoymentlevels()

def offerwater():
	console.clear()
	water()

def playwith():
	console.clear()
	Play()
	
def offerfood():
	console.clear()
	food()
	
def letrest():
	console.clear()
	tiredness()
	
def quit():
	global flag
	console.clear()
	flag = False

def xyzzy():
	global flag
	console.clear()
	print(Name, 'has discovered the easter egg, and has run away with it! ')
	flag = False
	
commands = dict()
commands['xyzzy'] = xyzzy
commands['quit'] = quit
commands['offer food'] = offerfood
commands['play'] = playwith
commands['offer water'] = offerwater
commands['let rest'] = letrest
commands['Play'] = playwith
commands['Xyzzy'] = xyzzy
commands['Quit'] = quit
commands['Offer Food'] = offerfood
commands['Let Rest'] = letrest
commands['Offer Water'] = offerwater


flag = True
while flag:
	console.set_color(.0, .57, 1.0)
	print(Name, 'is a', bodysize, detail, Animal['species'], 'covered with', scalesize, scalecolor, 'scales, with', eyecolor, 'eyes.')
	console.set_color(1.0, .0, .0)
	print('You may use the following commands: Play, Let Rest, Offer Food, Offer Water, Quit. What each thing does is clear.')
	console.set_color(.23, 1.0, .45)
	print('What do you do?')
	Increment()
	Status()
	if Animal['age'] == 1:
		print(Name, 'is', Animal['age'], 'day old. ')
	else:
		print(Name, 'is', Animal['age'], 'days old. ')
	c = input()
	for key in commands:
		if key == c:
			commands[key]()
	if Animal['age'] == Animal['maxage']:
		console.clear()
		print(Name, 'the', creature, 'lived to an old age of', Animal['maxage'], 'and has died of old age. Good job for completing the game!')
		flag = False

print('Goodbye!')
