from model.base import Base


class Monster(Base):
    """所有怪物的父类"""
    def __init__(self,):
        self.magic_num = 99999  # 怪默认无限蓝
        self.magic_num_max = self.magic_num   # 怪默认无限蓝

    def physical_attack(self, obj: Base):
        """"""
        if obj.health_num + obj.protect_num <= self.physical_attack_num:
            obj.health_num = 0
            obj.is_alive = 0
            print('【{0}】被【{1}】击败，【{0}】扑街！！！'.format(obj.name, self.name))
        elif obj.protect_num >= self.physical_attack_num:
            print('【{}】仅靠护甲就扛住了，硬！'.format(obj.name))
        else:
            obj.health_num -= self.physical_attack_num - obj.protect_num
            print('【{}】挨了【{}】一刀，血量降低 {}'.format(obj.name, self.name, self.physical_attack_num))
    

class Monster_qqr(Monster):
    def __init__(self):
        super().__init__()
        self.name = '丘丘人'
        self.physical_attack_num = 1
        self.health_num_max = 20
        self.health_num = 20

        










