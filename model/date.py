# -*- coding: UTF-8 -*-
# @author:jamesenh
# @file:date.py
# @time:2021/12/24

from xpinyin import Pinyin
import math


class Date:
	year: int
	month: int
	day: int
	now_date_num = 0
	per_month = 30
	per_year = 360
	
	def __init__(self):
		""""""
		self.now_date_num = 1
		
	def now_date(self):
		""""""
		self.year = math.ceil(self.now_date_num / self.per_year)
		y = self.now_date_num % self.per_year
		y = self.per_year if y == 0 else y
		self.month = math.ceil(y / self.per_month)
		self.day = self.now_date_num % self.per_year % self.per_month
		self.day = self.per_month if self.day == 0 else self.day
		# return self.year, self.month, self.day
		# return '公元{}年{}月{}日'.format(convert(self.year), convert(self.month), convert(self.day))
		return '公元{}年{}月{}日'.format (self.year, self.month, self.day)
	
	def date_increase(self, num: int):
		""""""
		self.now_date_num += num

def convert(num):
	ch_num = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
	s_unit = ['', '十', '百', '千']
	b_unit = ['', '万', '亿', '兆', '京', '垓', '秭', '穣', '沟', '涧', '正', '载', '极', ['恒河沙'], ['阿僧祇'], ['那由他'], ['不可思议'],
	          ['无量大数']]
	
	numlist = list(map(int, str(num)))
	numlist.reverse()
	l = []
	j = 0
	for i in range(0, len(numlist), 4):
		p = []
		if sum(numlist[i:i + 4]):
			for ii in range(0, 4):
				if (i + ii) < len(numlist):
					if numlist[i + ii]:
						p.append([s_unit[ii], ch_num[numlist[i + ii]]])
					else:
						if p and p[-1] != ['零']:
							p.append(['零'])
			if j < len(b_unit):
				l.append([b_unit[j]] + p)
			else:
				return "数字太大,超出计量范围！！"
		else:
			if l and l[-1] != ['零'] and l[-1][-1] != ['零']:
				l.append(['零'])
		j += 1
	l = [c for a in l for b in a for c in b if c]
	l.reverse()
	l = ''.join(l)
	return l


if __name__ == '__main__':
	dd = Date()
	dd.now_date_num = 1
	print(dd.now_date())
	dd.date_increase(30)
	print(dd.now_date())


