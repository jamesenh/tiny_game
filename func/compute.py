# -*- coding: UTF-8 -*-
# @author:jamesenh
# @file:compute.py
# @time:2021/12/24

from model.base import Base


def check_alive(obj: Base):
	if obj.health_num <= 0:
		obj.is_alive = 0



