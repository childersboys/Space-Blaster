import console
import random

# Attributes
Hunger = -1
Thirst = -1
Fatigue = -1
Enjoyment = 101
# Randomized things
BodyDecor = ['horned', 'spiked', 'shiny', 'glowing']
detail = BodyDecor[random.randint(0, 3)]
Body = ['small', 'large', 'giant']
bodysize = Body[random.randint(0, 2)]
ColorsScale = ['red', 'green', 'blue',
          'purple', 'yellow', 'orange']
scalecolor = ColorsScale[random.randint(0,5)]
ColorsEye = ['red', 'green', 'blue',
          'purple', 'yellow', 'orange']
eyecolor = ColorsEye[random.randint(0,5)]
Sizes = ['tiny', 'small', 'medium',
         'large', 'giant']
scalesize = Sizes[random.randint(0,4)]

# functions 
def Increment():
	global Hunger, Thirst, Fatigue
	global Enjoyment
	Hunger = Hunger + 1
	Thirst = Thirst + 1
	Fatigue = Fatigue + 1
	Enjoyment = Enjoyment - 1

def Hungerlevels():
	global Hunger, Thirst, Fatigue
	global Enjoyment, flag
	if Hunger == 0 or 49:
		print('I am not hungry.')
	elif Hunger == 50 or 89:
		print('I am hungry.')
	elif Hunger == 90:
		print('I am starving! Feed me!')
	elif Hunger == 100:
		print(Name, 'Died. ')
		flag = False
def Thirstlevels():
	global Hunger, Thirst, Fatigue
	global Enjoyment, flag
	if Thirst == 0 or 49:
		print('I am not thirsty.')
	elif Hunger == 50 or 89:
		print('I am thirsty.')
	elif Hunger == 90:
		print('I am drying up! Give me water!')
	elif Hunger == 100:
		print(Name, 'Died. ')
		flag = False

def Fatiguelevels():
	global Hunger, Thirst, Fatigue
	global Enjoyment, flag
	if Hunger == 0 or 49:
		print('I am not tired.')
	elif Hunger == 50 or 89:
		print('I am tired.')
	elif Hunger == 90:
		print('I am about to collapse! Let me sleep!')
	elif Hunger == 100:
		print(Name, 'Died. ')
		flag = False

def Enjoymentlevels():
	global Hunger, Thirst, Fatigue
	global Enjoyment, flag
	if Hunger == 0 or 49:
		print('I am having fun!')
	elif Hunger == 50 or 89:
		print('I am bored.')
	elif Hunger == 90:
		print('I will run away soon! Give me something to do!')
	elif Hunger == 100:
		print(Name, 'Ran Away. ')
		flag = False
def food():
	global Hunger
	print('He ate the food. ')
	Hunger = Hunger - 1
	
def water():
	global Thirst
	print('He drank the water. ')
	Thirst = Thirst - 1
	
def tiredness():
	global Fatigue
	print('He took a nap. ')
	Fatigue = Fatigue - 1
	
def Play():
	global Enjoyment
	print('He is happy to play. ')
	Enjoyment = Enjoyment + 1

def prepare():
  global Name
  console.set_font('Academy Engraved LET', 36)
  console.set_color(.23, 1.0, .45)
  Name = input('Name your pet! ')
  console.set_color(.0, .86, 1.2)
  console.set_font('Academy Engraved LET', 36)

# run it
prepare()
print(Name, 'is a', bodysize, detail, 'creature. It is covered in', scalesize, scalecolor, 'scales, with', eyecolor, 'eyes.')
console.set_color(1.0, .0, .0)
print('You may use the following commands: Play, Let Rest, Offer Food, Offer Water, Quit')
console.set_color(.23, 1.0, .45)

def Status():
	Hungerlevels()
	Thirstlevels()
	Fatiguelevels()
	Enjoymentlevels()
	
flag = True
while flag:
	print('What do you do?')
	Increment()
	Status()
	cmd = input().lower()
	if cmd == 'quit':
		flag = False
	elif cmd == 'offer food':
		food()
	elif cmd == 'play':
		Play()
	elif cmd == 'offer water':
		water()
	elif cmd == 'let rest':
		tiredness()
	elif cmd == 'xyzzy':
		print(Name, 'has discovered the easter egg, and has run away with it! ')
		flag = False
	elif cmd == 'plugh':
		print(Name, 'yawns')

print('Goodbye!')
