# -*- coding: UTF-8 -*-
# @author:jamesenh
# @file:humen.py
# @time:2021/12/23

import random
from model.base import Base
from model.date import Date
from func.compute import check_alive
from data_source import physical_attack_list, physical_health_list, physical_magic_list
import time, os


class Human(Base):
	def __init__(self, name: str, age: int, gender: int, physical: int):
		"""
		人物类
		:param name:名字
		:param age: 16 < 年纪 < 18
		:param gender: 性别 1男 0女
		:param physical: 体质 (0 - 9)
		"""
		self.physical_attack_num = 0    # 物攻
		self.magic_num = 0  # 当前蓝量
		self.name = name
		self.age = age
		self.gender = gender
		self.physical = physical    # 初始体质
		self.magic_num_max = 0  # 最大血量
		self.gold = 0
		self.life = Life(self)
		self.physical_init()
		self.information = {
			"姓名": self.name,
			"年龄": self.age,
			"血条": "{}/{}".format(self.health_num, self.health_num_max),
			"蓝条": "{}/{}".format(self.magic_num, self.magic_num_max),
			"物理攻击力": self.physical_attack_num,
			"金钱": self.gold,
			"护甲": self.protect_num,
			"装备": [],
			"技能": []
		}
	
	def show_information(self):
		""""""
		print('-' * 30)
		for k, v in self.information.items():
			print('【{}】=> {}'.format(k, v))
		print('-' * 30)
	
	def physical_init(self):
		"""
		根据初始体质初始化 物理攻击力、血量、蓝量
		:return:
		"""
		# 初始化物理攻击力
		self.physical_attack_num = random.randint(physical_attack_list[self.physical][0], physical_attack_list[self.physical][1])
		# 初始化血量
		self.health_num = random.randint(physical_health_list[self.physical][0], physical_health_list[self.physical][1])
		self.health_num_max = self.health_num
		# 初始化蓝量
		self.magic_num = random.randint(physical_magic_list[self.physical][0], physical_magic_list[self.physical][1])
		self.magic_num_max = self.magic_num

	def physical_attack(self, foe: Base):
		"""
		对人或怪发起物理攻击
		:param foe: 敌人
		:return:
		"""
		# 敌人血量降低
		foe.health_num -= self.physical_attack_num
		check_alive(foe)
	
	def skills(self):
		""""""
	
	def have_a_break(self):
		"""
		打坐休息（回蓝回血）
		:return:
		"""
		while self.health_num < self.health_num_max:
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
	
	def sleep(self):
		""""""


class Life:
	def __init__(self, obj: Base, is_test: int = 0):
		self.is_test = is_test
		# 创建目录
		dir_path = './life_history/'
		if not os.path.exists(dir_path):
			os.mkdir(dir_path)
		self.obj = obj
		self.f = open('{}{}的一生.life'.format(dir_path, self.obj.name), mode='a', encoding='utf-8')
	
	def born(self, date: Date):
		self.write('【{}】于{}开始了他传奇的一生'.format(self.obj.name, date.now_date()))
	
	def __del__(self):
		self.write('【{}】\t下辈子记得做个好人'.format(self.obj.name))
		self.f.close()
	
	def write(self, content: str):
		""""""
		print(content)
		if self.is_test:
			return
		self.f.write(content + '\n')
	
	def dead(self, date: Date):
		""""""
		if self.obj.is_alive == 0:
			self.write('【{}】于{}结束了他罪恶的一生'.format(self.obj.name, date.now_date()))


if __name__ == '__main__':
	p = Human('Dio', 5, 1, 9)
	print(p.physical_attack_num,p.health_num, p.magic_num)
