# coding: utf-8
'''
Created from various games in Pythonista 3, along with help from my dad.

Copyright (c) 2017, Glen David Childers
'''

from scene import *
from Coin import *
from Shield import *
from Meteor import *

import sound
import random
from math import sin, cos, pi
from game_menu import MenuScene
A = Action

paused = False


def cmp(a, b):
	return ((a > b) - (a < b))

standing_texture = Texture('1.jpg')
walk_textures = [Texture('r.jpg'), Texture('r.jpg')]
hit_texture = Texture('shp:Explosion06')
hitcount = 0

		
class Power (SpriteNode):
	def __init__(self, **kwargs):
		img = 'plf:RayGunPurple'
		SpriteNode.__init__(self, img, **kwargs)
		
		
class Game (Scene):
	def setup(self):
		self.background_color = '#000000'
		self.ground = Node(parent=self)
		self.player = SpriteNode(standing_texture)
		self.player.anchor_point = (0.5, 0)
		self.add_child(self.player)
		score_font = ('Party LET', 40)
		self.score_label = LabelNode('0', score_font, parent=self)
		self.score_label.position = (self.size.w/2, self.size.h - 70)
		self.score_label.z_position = 1
		shield_font = ('Papyrus', 12)
		self.shield_label = LabelNode('0', shield_font, parent=self)
		self.shield_label.position = (60, 20)
		self.shield_label.z_position = 1
		self.items = []
		self.lasers = []
		self.run_action(A.sequence(A.wait(0.0), A.call(self.show_start_menu)))
		self.new_game()
		self.highscore = self.load_highscore()
		self.pause_button = SpriteNode('iow:pause_32', position=(32, self.size.h-36), parent=self)
		self.powerups = [50, 0]
		power_font = ('Papyrus', 12)
		self.power_label = LabelNode('0', power_font, parent=self)
		self.power_label.position = (200, 20)
		self.power_label.z_position = 1
		
	def end_game(self):
		self.shield = 0
		self.shield_label.text = '0'
		if self.score > self.highscore:
			with open('SpaceBlaster.highscore', 'w') as f:
				f.write(str(self.score))
			self.highscore = self.score
		sound.play_effect('digital:ZapThreeToneDown')
		self.show_game_over_menu()

	def update(self):
		if self.game_over:
			self.shield_label.text = 'Shields: 0%'
			return
		self.shield_label.text = 'Shields: ' + str(100 + self.powerups[1] - hitcount) + '%'
		self.power_label.text = 'Ammo: ' + str(self.powerups[0])
		self.update_player()
		self.check_item_collisions()
		self.check_laser_collisions()
		if random.random() < 0.05 * self.speed:
			self.spawn_item()
		
	def touch_began(self, touch):
		if touch.location.x < 48 and touch.location.y > self.size.h - 48:
			self.pause_menu()
		else:
			if touch.location.y > 100:
				self.shoot_laser()
	
	def update_player(self):
		g = gravity()
#		if self.powerups[1] > 200:
#			self.powerups[1] = 200
		if abs(g.x) > 0.05:
			self.player.x_scale = cmp(g.x, 0)
			x = self.player.position.x
			max_speed = 40
			x = max(0, min(self.size.w, x + g.x * max_speed))
			self.player.position = x, 32
			step = int(self.player.position.x / 40) % 2
			if step != self.walk_step:
				self.player.texture = walk_textures[step]
				sound.play_effect('game:Spaceship', 0.05, 1.0 + 0.5 * step)
				self.walk_step = step
		else:
			self.player.texture = standing_texture
			self.walk_step = -1
			self.player.shader = None
		if self.player.scale < 1:
			self.player.scale = -2
			self.player.y_scale = 2
		else:
			self.player.scale = 2
		self.shield = (100 + self.powerups[1]) - hitcount
			
	def check_item_collisions(self):
		player_hitbox = Rect(self.player.position.x - 20, 32, 40, 65)
		for item in list(self.items):
			if item.frame.intersects(player_hitbox):
				if isinstance(item, Coin):
					self.collect_item(item, value=11)
				elif isinstance(item, Power):
					self.collect_item(item, value=10)
				elif isinstance(item, Shield):
					self.collect_item(item, value=30)
				elif isinstance(item, Meteor):
					if item.destroyed:
						self.collect_item(item, 1)
					else:
						self.player_hit(item)
			elif not item.parent:
				self.items.remove(item)
		
	def new_game(self):
		# Reset everything to its initial state...
		for item in self.items:
			item.remove_from_parent()
		self.items = []
		self.score = 0
		self.score_label.text = '0'
		self.shield = 0
		self.shield_label.text = '100'
		self.walk_step = -1
		self.player.position = (self.size.w/2, 32)
		self.player.texture = standing_texture
		self.speed = 1.5
		# The game_over attribute is set to True when the alien gets hit by a meteor. We use this to stop player movement and collision checking (the update method simply does nothing when game_over is True).
		self.game_over = False
		self.powerups = [50, 0]
		sound.play_effect('arcade:Powerup_2', 0.2)
	
	def check_laser_collisions(self):
		for laser in list(self.lasers):
			if not laser.parent:
				self.lasers.remove(laser)
				continue
			for item in self.items:
				if not isinstance(item, Meteor):
					continue
				if item.destroyed:
					continue
				if laser.position in item.frame:
					self.score += 100
					self.destroy_meteor(item)
					self.lasers.remove(laser)
					laser.remove_from_parent()
					break
	
	def destroy_meteor(self, meteor):
		sound.play_effect('arcade:Explosion_5', 1)
		meteor.destroyed = True
		meteor.texture = Texture('shp:nova')
		for i in range(5):
			m = SpriteNode('spc:LaserRed10', parent=self)
			m.position = meteor.position + (random.uniform(-20, 20), random.uniform(-20, 20))
			angle = random.uniform(0, pi*2)
			dx, dy = cos(angle) * 80, sin(angle) * 80
			m.run_action(A.move_by(dx, dy, 0.6, TIMING_EASE_OUT))
			m.run_action(A.sequence(A.scale_to(0, 0.6), A.remove()))
	
	def player_hit(self, item):
		global hitcount
		if hitcount >= (self.powerups[1] + 100):
			self.game_over = True
			hitcount = 0
			sound.play_effect('arcade:Explosion_1')
			self.player.texture = hit_texture
			self.player.run_action(A.move_by(0, -150))
			self.run_action(A.sequence(A.wait(2*self.speed), A.call(self.end_game)))
		else:
			sound.play_effect('arcade:Explosion_7')
			hitcount = hitcount + item.damage
			self.shield = (100 + self.powerups[1]) - hitcount
			item.damage = 0
			
	def shield_strength(self):
		return self.shield
	
	def spawn_meteor(self):
		meteor = Meteor(parent=self)
		dm = int(self.shield_strength() / 2)
		meteor.damage = random.randint(1, max(2, dm))
		meteor.position = (random.uniform(20, self.size.w-20), self.size.h + 30)
		d = random.uniform(2.0, 4.0)
		actions = [A.move_to(random.uniform(0, self.size.w), -100, d), A.remove()]
		meteor.run_action(A.sequence(actions))
		self.items.append(meteor)
	
	def spawn_powerup(self):
		power = None
		if random.randint(1, 20) > 10 and self.shield_strength() < 100:
			power = Shield(parent=self)
		elif self.powerups[0] < 100:
			power = Power(parent=self)
		else:
			self.spawn_star()
		if power:
			power.position = (random.uniform(20, self.size.w-20), self.size.h + 30)
			d = random.uniform(2.0, 4.0)
			actions = [A.move_to(random.uniform(0, self.size.w), -100, d), A.remove()]
			power.run_action(A.sequence(actions))
			self.items.append(power)
			# print(power)
			
	def spawn_star(self):
		coin = Coin(parent=self)
		coin.position = (random.uniform(20, self.size.w-20), self.size.h + 30)
		d = random.uniform(2.0, 4.0)
		actions = [A.move_by(0, -(self.size.h + 60), d), A.remove()]
		coin.run_action(A.sequence(actions))
		self.items.append(coin)
			
	def spawn_item(self):
		self.spawn_star()
		if random.random() < 0.1 * self.speed:
			self.spawn_meteor()
		elif random.random() > 0.2 * self.speed:
			self.spawn_powerup()
		else:
			self.spawn_star()
		self.speed = min(3, self.speed + 0.005)
		
	def collect_item(self, item, value=10):
		if value == 10:
			sound.play_effect('arcade:Coin_3')
			self.powerups[0] += random.randint(1, 20)
		elif value == 30:
			sound.play_effect('arcade:Coin_1')
			self.powerups[1] += random.randint(1, 10)
		else:
			sound.play_effect('arcade:Coin_2')
		item.remove_from_parent()
		self.items.remove(item)
		self.score += value
		self.score_label.text = str(self.score)
		global hitcount
		if hitcount > 0:
			pass
			# hitcount = hitcount - 1
		
	def show_start_menu(self):
		self.paused = True
		self.menu = MenuScene('Space Blaster', 'Score to beat: %i' % self.highscore, ['Play'])
		self.present_modal_scene(self.menu)
		
	def menu_button_selected(self, title):
		if title in ('Continue', 'New Game', 'Play', 'Try Again'):
			self.dismiss_modal_scene()
			self.menu = None
			self.paused = False
			if title in ('New Game', 'Play', 'Try Again'):
				self.new_game()
		elif title in ('Press Me!'):
			sound.play_effect('rpg:KnifeSlice2')
		else:
			print(title)
			
	def shoot_laser(self):
		if len(self.lasers) >= 8:
			return
		if self.powerups[0] > 0:
			self.powerups[0] -= 1
		else:
			return
		laser = SpriteNode('spc:Fire4', parent=self)
		laser.x_scale = 2.5
		laser.y_scale = 2.5
		laser.position = self.player.position + (0, 30)
		laser.z_position = -1
		actions = [A.move_by(0, self.size.h, 1.2 * self.speed), A.remove()]
		laser.run_action(A.sequence(actions))
		self.lasers.append(laser)
		sound.play_effect('arcade:Laser_6')
	
	def touch_moved(self, touch):
		pass
		# self.shoot_laser()
			
	def load_highscore(self):
		try:
			with open('SpaceBlaster.highscore', 'r') as f:
				return int(f.read())
		except:
			return 0

	def save_highscore(self):
		with open('SpaceBlaster.highscore', 'w') as f:
			f.write(str(self.highscore))
			
	def show_game_over_menu(self):
		self.paused = True
		self.menu = MenuScene('You Crashed!', 'Score: %i' % (self.score), ['Try Again'])
		self.present_modal_scene(self.menu)
		
	def pause_menu(self):
		self.paused = True
		self.menu = MenuScene('Game Paused', 'Beat this score: %i' % self.highscore, ['Continue', 'New Game', 'Press Me!'])
		self.present_modal_scene(self.menu)

if __name__ == '__main__':
	run(Game(), PORTRAIT, show_fps=False, multi_touch=False)
