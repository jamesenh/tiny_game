# -*- coding: UTF-8 -*-
# @author:jamesenh
# @file:humen.py
# @time:2021/12/23

import random
from data_source import physical_list


class Human:
	def __init__(self, name: str, age: int, gender: int, physical: int):
		"""
		人物类
		:param name:名字
		:param age: 0 < 年纪 < 10
		:param gender: 性别 1男 0女
		:param physical: 体质 (0 - 9)
		"""
		self.name = name
		self.age = age
		self.gender = gender
		self.physical = physical
		
		self.physical_init()
		
	
	# 初始化体质
	def physical_init(self):
		""""""
		self.physical_attack_num = random.randint(physical_list[self.physical][0], physical_list[self.physical][1])

	def physical_attack(self):
		""""""
	
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
	p = Human('Dio', 5, 1, 1)
	print(p.physical_attack_num)
