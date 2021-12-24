
# 基础类

class Base:
    name: str
    is_alive: int = 1  # 1或者，0挂了
    health_num: int = 0  # 当前血量
    health_num_max: int = 0  # 总血量
    magic_num: int = 0
    magic_num_max: int = 0
    physical_attack_num: int = 0  # 物理攻击力
    protect_num = 0  # 护甲
