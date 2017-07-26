import console, sys, time

box = dict()
box['a1'] = '#'
box['a2'] = '#'
box['a3'] = '#'
box['b1'] = '#'
box['b2'] = '#'
box['b3'] = '#'
box['c1'] = '#'
box['c2'] = '#'
box['c3'] = '#'

map = ''

def do_x():
	console.clear()
	global box, map
	map = 'A {0}|{1}|{2}\n  -|-|-\nB {3}|{4}|{5}\n  -|-|-\nC {6}|{7}|{8}\n  1 2 3 '.format(box['a1'], box['a2'], box['a3'], box['b1'], box['b2'], box['b3'], box['c1'], box['c2'], box['c3'],)
	print(map)
	x = input().lower()
	if x == 'a1' and box['a1'] == '#':
		box['a1'] = 'X'
	elif x == 'a2' and box['a2'] == '#':
		box['a2'] = 'X'
	elif x == 'a3' and box['a3'] == '#':
		box['a3'] = 'X'
	elif x == 'b1' and box['b1'] == '#':
		box['b1'] = 'X'
	elif x == 'b2' and box['b2'] == '#':
		box['b2'] = 'X'
	elif x == 'b3' and box['b3'] == '#':
		box['b3'] = 'X'
	elif x == 'c1' and box['c1'] == '#':
		box['c1'] = 'X'
	elif x == 'c2' and box['c2'] == '#':
		box['c2'] = 'X'
	elif x == 'c3' and box['c3'] == '#':
		box['c3'] = 'X'
	elif x == 'quit':
		sys.exit()
	elif x == 'win':
		console.clear()
		print('X won!')
		time.sleep(4)
		print('Actually, no. Try again. ')
		time.sleep(4)
		do_x()
	else:
		do_x()
		
def do_o():
	console.clear()
	global box, map
	map = 'A {0}|{1}|{2}\n  -|-|-\nB {3}|{4}|{5}\n  -|-|-\nC {6}|{7}|{8}\n  1 2 3 '.format(box['a1'], current['a2'], current['a3'], current['b1'], current['b2'], current['b3'], current['c1'], current['c2'], current['c3'],)
	print(map)
	o = input().lower()
	if o == 'a1' and current['a1'] == '#':
		current['a1'] = 'O'
	elif o == 'a2' and current['a2'] == '#':
		current['a2'] = 'O'
	elif o == 'a3' and current['a3'] == '#':
		current['a3'] = 'O'
	elif o == 'b1' and current['b1'] == '#':
		current['b1'] = 'O'
	elif o == 'b2' and current['b2'] == '#':
		current['b2'] = 'O'
	elif o == 'b3' and current['b3'] == '#':
		current['b3'] = 'O'
	elif o == 'c1' and current['c1'] == '#':
		current['c1'] = 'O'
	elif o == 'c2' and current['c2'] == '#':
		current['c2'] = 'O'
	elif o == 'c3' and current['c3'] == '#':
		current['c3'] = 'O'
	elif o == 'quit':
		sys.exit()
	elif o == 'win':
		console.clear()
		print('O won!')
		time.sleep(4)
		print('Actually, no. Try again. ')
		time.sleep(4)
		do_o()
	else:
		do_o()
		
def win_x():
	global map
	if current['a1'] == 'X' and current['a2'] == 'X' and current['a3'] == 'X':
		console.clear()
		map = 'A {0}|{1}|{2}\n  -|-|-\nB {3}|{4}|{5}\n  -|-|-\nC {6}|{7}|{8}\n  1 2 3 '.format(current['a1'], current['a2'], current['a3'], current['b1'], current['b2'], current['b3'], current['c1'], current['c2'], current['c3'],)
		print(map)
		print('')
		print('X won!')
		sys.exit()
	elif current['a1'] == 'X' and current['b1'] == 'X' and current['c1'] == 'X':
		console.clear()
		map = 'A {0}|{1}|{2}\n  -|-|-\nB {3}|{4}|{5}\n  -|-|-\nC {6}|{7}|{8}\n  1 2 3 '.format(current['a1'], current['a2'], current['a3'], current['b1'], current['b2'], current['b3'], current['c1'], current['c2'], current['c3'],)
		print(map)
		print('')
		print('X won!')
		sys.exit()
	elif current['a1'] == 'X' and current['b2'] == 'X' and current['c3'] == 'X':
		console.clear()
		map = 'A {0}|{1}|{2}\n  -|-|-\nB {3}|{4}|{5}\n  -|-|-\nC {6}|{7}|{8}\n  1 2 3 '.format(current['a1'], current['a2'], current['a3'], current['b1'], current['b2'], current['b3'], current['c1'], current['c2'], current['c3'],)
		print(map)
		print('')
		print('X won!')
		sys.exit()
	elif current['b1'] == 'X' and current['b2'] == 'X' and current['b3'] == 'X':
		console.clear()
		map = 'A {0}|{1}|{2}\n  -|-|-\nB {3}|{4}|{5}\n  -|-|-\nC {6}|{7}|{8}\n  1 2 3 '.format(current['a1'], current['a2'], current['a3'], current['b1'], current['b2'], current['b3'], current['c1'], current['c2'], current['c3'],)
		print(map)
		print('')
		print('X won!')
		sys.exit()
	elif current['c1'] == 'X' and current['c2'] == 'X' and current['c3'] == 'X':
		console.clear()
		map = 'A {0}|{1}|{2}\n  -|-|-\nB {3}|{4}|{5}\n  -|-|-\nC {6}|{7}|{8}\n  1 2 3 '.format(current['a1'], current['a2'], current['a3'], current['b1'], current['b2'], current['b3'], current['c1'], current['c2'], current['c3'],)
		print(map)
		print('')
		print('X won!')
		sys.exit()
	elif current['b2'] == 'X' and current['a2'] == 'X' and current['c2'] == 'X':
		console.clear()
		map = 'A {0}|{1}|{2}\n  -|-|-\nB {3}|{4}|{5}\n  -|-|-\nC {6}|{7}|{8}\n  1 2 3 '.format(current['a1'], current['a2'], current['a3'], current['b1'], current['b2'], current['b3'], current['c1'], current['c2'], current['c3'],)
		print(map)
		print('')
		print('X won!')
		sys.exit()
	elif current['a3'] == 'X' and current['b3'] == 'X' and current['c3'] == 'X':
		console.clear()
		map = 'A {0}|{1}|{2}\n  -|-|-\nB {3}|{4}|{5}\n  -|-|-\nC {6}|{7}|{8}\n  1 2 3 '.format(current['a1'], current['a2'], current['a3'], current['b1'], current['b2'], current['b3'], current['c1'], current['c2'], current['c3'],)
		print(map)
		print('')
		print('X won!')
		sys.exit()
	elif current['c1'] == 'X' and current['b2'] == 'X' and current['a3'] == 'X':
		console.clear()
		map = 'A {0}|{1}|{2}\n  -|-|-\nB {3}|{4}|{5}\n  -|-|-\nC {6}|{7}|{8}\n  1 2 3 '.format(current['a1'], current['a2'], current['a3'], current['b1'], current['b2'], current['b3'], current['c1'], current['c2'], current['c3'],)
		print(map)
		print('')
		print('X won!')
		sys.exit()
	else:
		pass
		
def win_o():
	global map
	if current['a1'] == 'O' and current['a2'] == 'O' and current['a3'] == 'O':
		console.clear()
		map = 'A {0}|{1}|{2}\n  -|-|-\nB {3}|{4}|{5}\n  -|-|-\nC {6}|{7}|{8}\n  1 2 3 '.format(current['a1'], current['a2'], current['a3'], current['b1'], current['b2'], current['b3'], current['c1'], current['c2'], current['c3'],)
		print(map)
		print('')
		print('O won!')
		sys.exit()
	elif current['a1'] == 'O' and current['b1'] == 'O' and current['c1'] == 'O':
		console.clear()
		map = 'A {0}|{1}|{2}\n  -|-|-\nB {3}|{4}|{5}\n  -|-|-\nC {6}|{7}|{8}\n  1 2 3 '.format(current['a1'], current['a2'], current['a3'], current['b1'], current['b2'], current['b3'], current['c1'], current['c2'], current['c3'],)
		print(map)
		print('')
		print('O won!')
		sys.exit()
	elif current['a1'] == 'O' and current['b2'] == 'O' and current['c3'] == 'O':
		console.clear()
		map = 'A {0}|{1}|{2}\n  -|-|-\nB {3}|{4}|{5}\n  -|-|-\nC {6}|{7}|{8}\n  1 2 3 '.format(current['a1'], current['a2'], current['a3'], current['b1'], current['b2'], current['b3'], current['c1'], current['c2'], current['c3'],)
		print(map)
		print('')
		print('O won!')
		sys.exit()
	elif current['b1'] == 'O' and current['b2'] == 'O' and current['b3'] == 'O':
		console.clear()
		map = 'A {0}|{1}|{2}\n  -|-|-\nB {3}|{4}|{5}\n  -|-|-\nC {6}|{7}|{8}\n  1 2 3 '.format(current['a1'], current['a2'], current['a3'], current['b1'], current['b2'], current['b3'], current['c1'], current['c2'], current['c3'],)
		print(map)
		print('')
		print('O won!')
		sys.exit()
	elif current['c1'] == 'O' and current['c2'] == 'O' and current['c3'] == 'O':
		console.clear()
		map = 'A {0}|{1}|{2}\n  -|-|-\nB {3}|{4}|{5}\n  -|-|-\nC {6}|{7}|{8}\n  1 2 3 '.format(box['a1'], box['a2'], box['a3'], box['b1'], box['b2'], box['b3'], box['c1'], box['c2'], box['c3'],)
		print(map)
		print('')
		print('O won!')
		sys.exit()
	elif box['b2'] == 'O' and box['a2'] == 'O' and box['c2'] == 'O':
		console.clear()
		map = 'A {0}|{1}|{2}\n  -|-|-\nB {3}|{4}|{5}\n  -|-|-\nC {6}|{7}|{8}\n  1 2 3 '.format(box['a1'], box['a2'], box['a3'], box['b1'], box['b2'], box['b3'], box['c1'], box['c2'], box['c3'],)
		print(map)
		print('')
		print('O won!')
		sys.exit()
	elif box['a3'] == 'O' and box['b3'] == 'O' and box['c3'] == 'O':
		console.clear()
		map = 'A {0}|{1}|{2}\n  -|-|-\nB {3}|{4}|{5}\n  -|-|-\nC {6}|{7}|{8}\n  1 2 3 '.format(box['a1'], box['a2'], box['a3'], box['b1'], box['b2'], box['b3'], box['c1'], box['c2'], box['c3'],)
		print(map)
		print('')
		print('O won!')
		sys.exit()
	elif box['c1'] == 'O' and box['b2'] == 'O' and box['a3'] == 'O':
		console.clear()
		map = 'A {0}|{1}|{2}\n  -|-|-\nB {3}|{4}|{5}\n  -|-|-\nC {6}|{7}|{8}\n  1 2 3 '.format(box['a1'], box['a2'], box['a3'], box['b1'], box['b2'], box['b3'], box['c1'], box['c2'], box['c3'],)
		print(map)
		print('')
		print('O won!')
		sys.exit()
	else:
		pass
		
def win():
	win_x()
	win_o()
	
while True:
	do_x()
	win()
	do_o()
	win()
