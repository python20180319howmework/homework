'''
4. 回答一下问题
   1) python面向对象的特点是什么
		继承 封装  多态
   2) 继承给我带来什么好处
		可以减少重复代码，父类提供的方法 子类可以直接使用，不用再去写实现这个功能的函数。继承是多态性的前提。当然使用继承的同事也提高了类的耦合起
    3) super关键字有什么作用
		解决多次继承时同一父类被多次调用的问题
   4) 定义类的__init__方法可以有返回值吗,自己尝试一下
	 	返回值为None
   5) 当子类定义了与父类相同的方法的时候,会怎么样
		子类方法会覆盖父类方法
   6) 实例化对象的时候,类的什么方法会自动调用
		init方法会被自动调用	
   7)一下几天语句体现了python的什么特性
         “i love python”.count('0')
        (1,2,3,2,1,5,6,2,9).count(2)
        [1,2,3,2,1,2,2,4,5,6,5,5].count(5)
		动态性
    8) python类内部的self有什么作用,需要传递此参数吗
		类初始化之后会得到实例，self就是用于代表初始化得到的实例。明确的写一个self 参数，是的类的放过发和普通的函数本质上没有差异，所有的输入参数都心事的传递到 方法/函数当中。  self不许奥传参
    9) 装饰器有什么作用,说说你知道的有哪些装饰器
			装饰器种类：被装饰的函数带参数，带参数的装饰器，系统内置装饰器
（staticmeth od  classmethod 和property）
    10) python允许多继承吗,自己的代码中大量出现多继承有哪些弊端
		允许多继承。代码大量出现多继承，同一父类可能会被多次调用，还可能造成 传参不易。
'''
