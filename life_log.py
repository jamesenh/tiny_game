# -*- coding: UTF-8 -*-
# @author:jamesenh
# @file:life_log.py
# @time:2021/12/24

from model.base import Base
from model.date import Date
import os


class Life:
	def __init__(self, obj: Base):
		# 创建目录
		dir_path = './life_history/'
		if not os.path.exists(dir_path):
			os.mkdir(dir_path)
		self.obj = obj
		self.f = open('{}{}的一生.life'.format(dir_path, self.obj.name), mode='a', encoding='utf-8')
	
	def born(self, date: Date):
		self.write('【{}】于{}开始了他传奇的一生\n'.format(self.obj.name, date.now_date()))
	
	def __del__(self):
		self.write('【{}】，下辈子记得做个好人\n'.format(self.obj.name))
		self.f.close()
	
	def write(self, content: str):
		""""""
		self.f.write(content)
		print(content)
	
	def dead(self, date: Date):
		""""""
		if self.obj.is_alive == 0:
			self.write('【{}】于{}结束了他罪恶的一生\n'.format(self.obj.name, date.now_date()))
			