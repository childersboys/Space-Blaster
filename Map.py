import console

done = False

tiles = dict()
tiles[0] = '🌳'
tiles[2] = '🏠'
tiles[3] = '🔱'
tiles[4] = '🌲'
tiles[1] = '🌿'
me = dict()
me['char'] = '😀'

map = [0, 4, 0, 0, 0, 0, 0, 0,
       0, 1, 1, 1, 1, 1, 1, 0,
       0, 1, 1, 1, 1, 1, 1, 0,
       0, 1, 1, 1, 1, 1, 1, 0,
       0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0,
       0, 1, 1, 1, 1, 1, 1, 0,
       0, 0, 0, 0, 0, 0, 4, 0,
       0, 0, 3, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0]
rows = 10
cols = 8

me['x'] = 2
me['y'] = 2

def draw():
	console.clear()
	for row in range(0, rows):
		for col in range(0, cols):
			if row == me['x'] and col == me['y']:
				print(me['char'], end='')
			else:
				print(tiles[map[(row*cols)+col]], end='')
		print()

def move():
	global done
	cmd = input().lower()
	if cmd == 'w':
		me['y'] = me['y'] - 1
	elif cmd == 'e':
		me['y'] = me['y'] + 1
	elif cmd == 'n':
		me['x'] = me['x'] - 1
	elif cmd == 's':
		me['x'] = me['x'] + 1
	elif cmd == 'done':
		done = True
		
def Bounds():
	if me['x'] == 0 and me['y'] == 1:
		me['x'] = 6
		me['y'] = 2
	elif me['x'] == 7 and me['y'] == 6:
		me['x'] = 3
		me['y'] = 6
	elif me['x'] == 0:
		me['x'] = me['x'] + 1
	elif me['y'] == 0:
		me['y'] = me['y'] + 1
	elif me['x'] == 4:
		me['x'] = me['x'] - 1
	elif me['x'] == 5:
		me['x']= me['x'] + 1
	elif me['y'] == 7:
		me['y'] = me['y'] - 1
	elif me['x'] == 7:
		me['x'] = me['x'] - 1
while done == False:
	draw()
	move()
	Bounds()
	
