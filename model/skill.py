
from model.base import Base
from func.compute import check_alive


class Skill:
    def __init__(self, skill_name):
        self.skill_name = skill_name
        self.magic_expend_num = 0   # 耗蓝量
        self.skill_attack_num = 0   # 技能攻击力
        self.skill_attack_without_protect_num = 0   # 无视护甲攻击力
        self.recover_health_num = 0     # 回血量
        
    def use_this(self, operator: Base, foe: Base):
        """"""
        # 扣除蓝量
        operator.magic_num -= self.magic_expend_num
        if operator.magic_num < 0:
            operator.magic_num = 0
            print('蓝量不足，技能使用失败，蓝量归零')
        else:
            if self.skill_attack_num:
                self.skill_attack(operator, foe)
            elif self.skill_attack_without_protect_num:
                self.skill_attack_without_protect(operator, foe)
            elif self.recover_health_num:
                self.recover_health(operator, foe)

    def skill_attack(self, operator:Base, foe: Base):
        """技能攻击"""
        if foe.protect_num + foe.health_num <= self.skill_attack_num:
            foe.health_num = 0
            foe.is_alive = 0
            print('【{}】被击败，扑街！！！'.format(foe.name))
        elif foe.protect_num >= self.skill_attack_num:
            print('【{}】仅凭护甲硬抗住了【{}】的《{}》！'.format(foe.name, operator.name, self.skill_name))
        else:
            foe.health_num -= self.skill_attack_num - foe.protect_num
            print('【{}】扛住了【{}】的《{}》'.format(foe.name, operator.name, self.skill_name))

    def skill_attack_without_protect(self, operator: Base, foe: Base):
        """无视护甲的技能攻击"""
        foe.health_num -= self.skill_attack_without_protect_num
        check_alive(foe)

    def recover_health(self, operator: Base, foe: Base):
        """恢复血量"""
        



