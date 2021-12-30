# -*- coding:utf-8 -*-
"""
__project_ = 'tiny_game'
__file_name__ = 'opportunity'
__author__ = 'jamesenh'
__time__ = '2021/12/24 20:05'
__product_name = PyCharm
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
from model.date import Date
from model.base import Base
from model.humen import Human
from func.tools import selector, wait
import time


class Event:
	"""事件类"""
	def __init__(self):
		""""""
	
	
class Cycle_event(Event):
	"""主循环事件"""
	obj: Human
	date: Date
	
	def __init__(self):
		super().__init__()
		
	def start(self, obj: Human, date: Date):
		self.obj = obj
		self.date = date
		while self.obj.is_alive:    # 进入主循环事件
			""""""
			self.main()

	def main(self):
		choices = {
			1: '原地休息（缓慢恢复状态）',
			2: '住店睡觉（花费5天及5软妹币）',
			3: '刷怪练级（）',
			4: 'Shopping',
			5: '跳过本条命（...）',
			6: '查看自身属性',
		}
		selected = selector(choices)
		if selected == 1:
			self.have_a_break()
		elif selected == 2:
			self.sleep_in_hotel()
		elif selected == 3:
			self.training()
		elif selected == 4:
			self.shopping()
		elif selected == 5:
			self.break_this_life()
		else:
			self.show_info()
		wait()
	
	def have_a_break(self):
		self.obj.have_a_break()
	
	def sleep_in_hotel(self):
		if self.obj.gold < 5:
			print('同福客栈老板【佟湘玉】：5块钱都没有还想住店，睡大街去吧！')
			self.obj.health_num -= 5
			print('【{}】被旅店老板赶了出来，并被痛打了一顿，生命值降低{}。'.format(self.obj.name, 5))
		else:
			self.obj.gold -= 5
			print('同福客栈老板【佟湘玉】：欢迎客人入住。\n客人需不需要特殊服务呀！（小声哔哔）')
			print('【{}】入住同福客栈。')
			for i in range(8):
				print('.', end='')
				time.sleep(0.8)
			print('5天后。')
			self.date.date_increase(5)
			self.obj.health_num = self.obj.health_num_max
			self.obj.magic_num = self.obj.magic_num_max
			self.obj.show_information()

	def training(self):
		print('抱歉，该功能暂未开发。。。')
	
	def shopping(self):
		print('抱歉，该功能暂未开发。。。')
	
	def break_this_life(self):
		self.obj.health_num = 0
		self.obj.is_alive = 0
		self.obj.life.dead(self.date)
	
	def show_info(self):
		self.obj.show_information()
