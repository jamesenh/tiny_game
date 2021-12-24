
from model.base import Base
from func.compute import check_alive


class Skill:
    def __init__(self, name):
        self.name = name
        self.magic_expend_num = 0   # 耗蓝量
        self.skill_attack_num = 0   # 技能攻击力
        self.skill_attack_without_protect_num = 0   # 无视护甲攻击力
        self.recover_health_num = 0     # 回血量
        
    def use_this(self, operator: Base):
        """"""
        operator.magic_num -= self.magic_expend_num
        if operator.magic_num < 0:
            operator.magic_num = 0
            print('蓝量不足，技能使用失败，蓝量归零')
            

    def skill_attack(self, operator:Base, foe: Base):
        """"""
        
        foe.health_num = foe.health_num + foe.protect_num - self.skill_attack_num
        check_alive(foe)

    def skill_attack_without_protect(self, foe: Base):
        """"""
        foe.health_num -= self.skill_attack_without_protect_num
        check_alive(foe)

    def recover_health(self, obj: Base):
        """"""
        



