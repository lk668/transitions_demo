# Python状态机Demo

本项目基于python transitions实现一个简单的状态机demo

## 1. 准备工作

1. 部署依赖

```bash
pip3 install -r requirements.txt
```

2. 部署生成流程图的依赖
如果想测试生成整个状态机的流程图，安装如下依赖
```bash
ubuntu机器执行如下命令

sudo apt-get install graphviz graphviz-dev 
```

## 2. 测试
执行如下命令
```bash
python3 test.py
```

输出结果如下：
```bash
test1 初始状态为 init
执行函数from_init_to_liquid
执行函数from_liquid_to_gas
Before: 执行函数之前的状态为 liquid
I'm now in gas state
After: 执行函数之后的状态为 gas
执行函数from_gas_to_plasma
测试condition后的状态为 plasma
重置后的状态 init
```