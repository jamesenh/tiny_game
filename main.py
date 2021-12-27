from model import humen, monster, skill, equipment
from model.date import Date
import random
from func.selector import selector


def test(name, gender=1):
	me = humen.Human(name, age=random.randint(16,18), gender=gender, physical=random.randint(0,9))
	date = Date()
	me.life.born(date)
	me.show_information()
	me.life.dead(date)
	
	


if __name__ == '__main__':
	name = input('输入你的名字:\n')
	gender = int(input('选择你的性别\n 0->女，1->男:\n'))
	test(name, gender)
	
