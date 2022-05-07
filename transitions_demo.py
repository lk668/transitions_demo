from transitions import Machine


class PoiExample(object):

    # 定义所有的状态
    states = ['init', 'solid', 'liquid', 'gas', 'plasma']

    """
    定义转移函数
    trigger：触发需要调用的函数
    source：源状态
    dest：触发以后的目标状态
    """
    transitions = [
        # 注意： 这里的source可以是一个列表，表示从列表的这几个状态，都可以到达目的状态

        # 转移函数1
        { 'trigger': 'from_init_to_liquid', 'source': 'init', 'dest': 'liquid' },
        # 转移函数2
        { 'trigger': 'from_liquid_to_gas', 'source': 'liquid', 'dest': 'gas', "before": "before_action", "after": "after_action"},
        # 转移函数3
        { 'trigger': 'from_solid_to_gas', 'source': 'solid', 'dest': 'gas', "after": "after_action" },
        # 转移函数4， 满足condition走1，不满足走2
        { 'trigger': 'from_gas_to_plasma', 'source': 'gas', 'dest': 'plasma', "conditions": ["is_true"] },
        { 'trigger': 'from_gas_to_plasma', 'source': 'gas', 'dest': 'liquid'},

        # 转移函数5
        # 不管当前状态是什么，调用了from_*_to_solid()，都会到达solid状态
        { 'trigger': 'from_*_to_solid', 'source': '*', 'dest': 'solid'}
    ]

    def __init__(self, name="", poi="", init_state=""):
        self.name, self.poi = name, poi
        # 如果不初始化状态，默认为init
        self.init_state = init_state if init_state else "init"
        # 初始状态为init
        # *** 注意：ignore_invalid_triggers 参数配置为True以后，非法调用不会抛异常，比如我当前在状态init，我调用函数from_gas_to_plasma(), 在该参数为True时，不会抛异常，在为False时，抛异常
        self.machine = Machine(model=self, states=PoiExample.states, transitions=PoiExample.transitions, initial=self.init_state, ignore_invalid_triggers=False)

    def before_action(self):
        print(f"Before: 执行函数之前的状态为 {self.state}")
    
    def after_action(self):
        # 某个状态执行完成以后的操作
        # 后面可以把数据库更新的操作，统一写到这个函数
        print(f"After: 执行函数之后的状态为 {self.state}")
    
    def on_enter_gas(self):
        # 到达某个状态执行的操作。
        print("I'm now in gas state")
    
    def is_true(self):
        return True