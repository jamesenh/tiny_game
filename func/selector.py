# -*- coding: UTF-8 -*-
# @author:jamesenh
# @file:selector.py
# @time:2021/12/24


def selector(choices: dict):
	while True:
		for key, value in choices.items():
			print('{} --> {}'.format(key, value))
		try:
			selected = int(input('输入你的选择: '))
		except:
			continue
		if selected in ('', None) or (selected not in choices):
			print('重新选择')
			continue
		return selected

		









