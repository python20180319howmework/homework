'''
定义一个列表的操作类：
Listinfo  包括方法
列表元素添加：add_key(keyname)  [keyname:字符串或者整型]
列表元素取值：get_key(num) [num:整数类型]
列表合并: update_list(list) [list: 列表类型]
删除并且返回最后一个元素: dl_key()
'''


class Listinfo(object):
	def __init__(self, key, num):
		self.__key = key
	
	def get_key(self):
		return self.__num		
	def get_list(self, *list):
		self.__list = list
	def update_list(self,list1,list2):
		self.__list1 = list1
		self.__list2 = list2
		for item in list1:
			list_new.append(item)
		for item in list2:
			list_new.append(item)
		return list_new
	def dl_key(self,newlist, n):
		self.__newlist = newlist
		self.__n = n
		if n in range(len(newlist)):
			newlist1 = newlist.remove(n)
		return newlist1[-1]

if __name__ =="__main__":
	list1 = [1,2,3,1,3,2,3]
	list2 = [2,5,8,3,1,2,6]
	get_list(list1, list2)
	update_list(list1,list2)
	newlist = (update_list(list1,list2))
	dl_key(newlist,2)

		
		



