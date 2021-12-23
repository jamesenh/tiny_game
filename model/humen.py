# -*- coding: UTF-8 -*-
# @author:jamesenh
# @file:humen.py
# @time:2021/12/23

import random
from model.base import Base
from data_source import physical_attack_list, physical_health_list, physical_magic_list


class Human(Base):
	def __init__(self, name: str, age: int, gender: int, physical: int):
		"""
		人物类
		:param name:名字
		:param age: 0 < 年纪 < 10
		:param gender: 性别 1男 0女
		:param physical: 体质 (0 - 9)
		"""
		self.physical_attack_num = 0
		self.magic_num = 0
		self.name = name
		self.age = age
		self.gender = gender
		self.physical = physical
		self.physical_init()

	def physical_init(self):
		"""
		根据初始体质初始化 物理攻击力、血量、蓝量
		:return:
		"""
		# 初始化物理攻击力
		self.physical_attack_num = random.randint(physical_attack_list[self.physical][0], physical_attack_list[self.physical][1])
		# 初始化血量
		self.health_num = random.randint(physical_health_list[self.physical][0], physical_health_list[self.physical][1])
		# 初始化蓝量
		self.magic_num = random.randint(physical_magic_list[self.physical][0], physical_magic_list[self.physical][1])

	def physical_attack(self, foe: Base):
		"""
		对人或怪发起物理攻击
		:param foe: 敌人
		:return:
		"""
		# 敌人血量降低
		foe.health_num -= self.physical_attack_num
		# 判断敌人是否还活着
		if foe.health_num <= 0:
			foe.is_alive = 0


	
	def skill_attack(self):
		""""""
	
	def have_a_break(self):
		""""""
	
	def levelup(self):
		""""""
	
	def up_equipment(self):
		""""""
	
	def down_equipment(self):
		""""""
	
	def buy_something(self):
		""""""
	
	def sale_something(self):
		""""""
	
	def training(self):
		""""""
	
	

if __name__ == '__main__':
	p = Human('Dio', 5, 1, 9)
	print(p.physical_attack_num,p.health_num, p.magic_num)