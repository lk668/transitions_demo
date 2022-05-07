from transitions_demo import PoiExample
from transitions.extensions import GraphMachine


if __name__ == "__main__":
    test1 = PoiExample(name="test", poi="123")
    # 初始状态应该为init
    print(f"test1 初始状态为 {test1.state}")

    machine = GraphMachine(model=test1, states=test1.states, transitions=test1.transitions, initial=test1.init_state, show_conditions=True)
    # 生成流程转移图
    test1.get_graph().draw('my_state_diagram.png', prog='dot')
    
    # 测试condition
    print("执行函数from_init_to_liquid")
    test1.from_init_to_liquid()
    print("执行函数from_liquid_to_gas")
    test1.from_liquid_to_gas()
    print("执行函数from_gas_to_plasma")
    test1.from_gas_to_plasma()
    print(f"测试condition后的状态为 {test1.state}")

    # 如果设置了ignore_invalid_triggers=True，此处执行不会抛异常，如果设置为False，此处执行会MachineError抛异常
    # test1.from_init_to_liquid()

    # 重置状态，默认会封装 to_{state}的函数
    test1.to_init()
    print(f"重置后的状态 {test1.state}")