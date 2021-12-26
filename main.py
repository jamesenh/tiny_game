from model import humen, master, skill, equipment
from model.date import Date
import life_log
import random
from func.selector import selector


def test(name, gender):
	you = humen.Human(name, age=random.randint(1,10), gender=gender, physical=random.randint(0,9))
	life = life_log.Life(you)
	date = Date()
	life.born (date)
	life.dead(date)
	
	


if __name__ == '__main__':
	name = input('输入你的名字:\n ')
	gender = int(input('选择你的性别\n 0->女，1->男: \n'))
	test(name, gender)
	
