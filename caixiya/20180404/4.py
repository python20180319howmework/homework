'''
4. 回答一下问题
   1) python面向对象的特点是什么
   2) 继承给我带来什么好处
   3) super关键字有什么作用
   4) 定义类的__init__方法可以有返回值吗,自己尝试一下
   5) 当子类定义了与父类相同的方法的时候,会怎么样
   6) 实例化对象的时候,类的什么方法会自动调用
   7)一下几天语句体现了python的什么特性
         “i love python”.count('0')
        (1,2,3,2,1,5,6,2,9).count(2)
        [1,2,3,2,1,2,2,4,5,6,5,5].count(5)
    8) python类内部的self有什么作用,需要传递此参数吗
    9) 装饰器有什么作用,说说你知道的有哪些装饰器
    10) python允许多继承吗,自己的代码中大量出现多继承有哪些弊端

1)封装继承多态
2)当B类和A类有相同方法时，可以让B类去继承A类，这样避免重复操作，提高代码复用性
3)super关键字的好处是父类多次被调用时只执行一次，提高了执行效率
4)有 返回None值_
5)子类覆盖父类
6)__init__方法
7)动态
8)self就是用于代表初始化得到的实例,有self让所有的输入参数都显示地传递到方法/函数当中
9)python装饰器就是用于拓展原来函数功能的一种函数，这个函数的特殊之处在于它的返回值也是一个函数，使用python装饰器的好处就是在不改变原函数的前提下给原函数增加新的功能。@property getter方法 setter方法 @unique
使用@staticmethod或@classmethod，可以不需要实例化一个对象，直接类名.方法名()来调用
10)允许 ，传参混乱
'''