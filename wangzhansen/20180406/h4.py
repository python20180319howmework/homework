
1.继承,封装,多态
2.继承可以减少重复的代码。比如父类已经提供的方法，子类可以直接使用，不必再去  实现。继承是多态性的前提。当然使用继承的同时也提高了类的耦合。
3.解决多重继承时同一父类被多次调用的问题
4.__init__返回为None
5.子类方法会覆盖父类方法
6.__init__方法会自动调用
7.动态性
8.类初始化之后会得到实例，self就是用于代表初始化的到的实例。明确地写一个self  参数，使得类的方法和普通的函数本质上没有差异，所有的输入参数都显示地传递到  方法/函数当中。
  self不需要传参	
9.装饰器允许向一个现有的对象添加新的功能，同时又不改变其结构。
  装饰器种类：被装饰的函数带参数，带参数的装饰器，系统内置装饰器（staticmeth  od、classmethod 和property）
10.python允许多继承。代码大量出现多继承，同一父类可能被多次调用，还可能造成    传参不易。
