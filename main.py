from model import humen, monster, skill, equipment
from model.date import Date
import random
from func import event


def test(name, gender=1):
	me = humen.Human(name, age=random.randint(16,18), gender=gender, physical=random.randint(0,9))
	date = Date()
	me.life.born(date)
	event.Cycle_event().start(me, date)

	
	


if __name__ == '__main__':
	name = input('输入你的名字:\n')
	gender = int(input('选择你的性别\n0->女，1->男:\n'))
	test(name, gender)

